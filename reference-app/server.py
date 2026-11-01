"""Dependency-free reference API with tenant-scoped sessions and SQLite storage."""

from __future__ import annotations

import hashlib
import hmac
import json
import os
import secrets
import sqlite3
import mimetypes
import time
from collections import defaultdict, deque
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parent
DATABASE = Path(os.environ.get("PANELFORGE_DB", ROOT / "reference.sqlite3"))
SESSION_SECRET = os.environ.get("PANELFORGE_SESSION_SECRET", "development-only-change-me").encode()
SESSION_TTL = 3600
RATE_LIMIT_WINDOW = 60
RATE_LIMIT_MAX = int(os.environ.get("PANELFORGE_RATE_LIMIT_MAX", "30"))
_REQUESTS: dict[str, deque[float]] = defaultdict(deque)


def password_digest(password: str, salt: bytes) -> str:
    return hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 120_000).hex()


def initialize_database(path: Path = DATABASE) -> None:
    with sqlite3.connect(path) as connection:
        connection.executescript(
            """
            PRAGMA foreign_keys = ON;
            CREATE TABLE IF NOT EXISTS organizations (
                id TEXT PRIMARY KEY, name TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY, email TEXT UNIQUE NOT NULL, name TEXT NOT NULL,
                role TEXT NOT NULL CHECK (role IN ('manager', 'member')),
                organization_id TEXT NOT NULL REFERENCES organizations(id),
                password_salt BLOB NOT NULL, password_hash TEXT NOT NULL
            );
            CREATE TABLE IF NOT EXISTS deals (
                id INTEGER PRIMARY KEY AUTOINCREMENT, organization_id TEXT NOT NULL REFERENCES organizations(id),
                name TEXT NOT NULL, value INTEGER NOT NULL CHECK (value >= 0),
                stage TEXT NOT NULL, owner_id TEXT NOT NULL REFERENCES users(id)
            );
            CREATE TABLE IF NOT EXISTS audit_events (
                id INTEGER PRIMARY KEY AUTOINCREMENT, organization_id TEXT NOT NULL REFERENCES organizations(id),
                actor_id TEXT NOT NULL REFERENCES users(id), action TEXT NOT NULL,
                resource TEXT NOT NULL, created_at INTEGER NOT NULL
            );
            """
        )
        if connection.execute("SELECT COUNT(*) FROM organizations").fetchone()[0]:
            return
        salt = secrets.token_bytes(16)
        digest = password_digest("demo-password", salt)
        connection.executemany("INSERT INTO organizations VALUES (?, ?)", [
            ("northstar", "Northstar Labs"), ("other-tenant", "Other Tenant")
        ])
        connection.executemany("INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?)", [
            ("maya", "maya@northstar.example", "Maya Chen", "manager", "northstar", salt, digest),
            ("jon", "jon@northstar.example", "Jon Bell", "member", "northstar", salt, digest),
            ("other", "other@example.test", "Other User", "manager", "other-tenant", salt, digest),
        ])
        connection.executemany(
            "INSERT INTO deals (organization_id, name, value, stage, owner_id) VALUES (?, ?, ?, ?, ?)",
            [("northstar", "Acme Logistics", 84000, "Negotiation", "maya"),
             ("northstar", "Brightside Health", 52500, "Proposal", "jon"),
             ("other-tenant", "Private Deal", 90000, "Qualified", "other")],
        )


def encode_session(user_id: str) -> str:
    payload = f"{user_id}:{int(time.time()) + SESSION_TTL}"
    signature = hmac.new(SESSION_SECRET, payload.encode(), hashlib.sha256).hexdigest()
    return f"{payload}:{signature}"


def decode_session(token: str) -> str | None:
    parts = token.split(":")
    if len(parts) != 3:
        return None
    user_id, expiry, signature = parts
    payload = f"{user_id}:{expiry}"
    if not hmac.compare_digest(signature, hmac.new(SESSION_SECRET, payload.encode(), hashlib.sha256).hexdigest()):
        return None
    try:
        if int(expiry) < int(time.time()):
            return None
    except ValueError:
        return None
    return user_id


class APIHandler(BaseHTTPRequestHandler):
    server_version = "PanelForgeReference/1.0"

    def _json(self, status: int, payload: dict[str, Any], headers: dict[str, str] | None = None) -> None:
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("X-Frame-Options", "DENY")
        self.send_header("Referrer-Policy", "no-referrer")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        for key, value in (headers or {}).items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(body)

    def _rate_limited(self) -> bool:
        now = time.monotonic()
        requests = _REQUESTS[self.client_address[0]]
        while requests and now - requests[0] >= RATE_LIMIT_WINDOW:
            requests.popleft()
        if len(requests) >= RATE_LIMIT_MAX:
            self._json(HTTPStatus.TOO_MANY_REQUESTS, {"error": "rate_limit_exceeded"})
            return True
        requests.append(now)
        return False

    def _secure_configuration(self) -> bool:
        return os.environ.get("PANELFORGE_ENV", "development") == "development" or SESSION_SECRET != b"development-only-change-me"

    def _body(self) -> dict[str, Any] | None:
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length > 16_384:
                return None
            value = json.loads(self.rfile.read(length) or b"{}")
            return value if isinstance(value, dict) else None
        except (ValueError, json.JSONDecodeError):
            return None

    def _user(self) -> dict[str, str] | None:
        token = self.headers.get("Authorization", "").removeprefix("Bearer ").strip()
        user_id = decode_session(token)
        if not user_id:
            return None
        with sqlite3.connect(DATABASE) as connection:
            row = connection.execute(
                "SELECT id, email, name, role, organization_id FROM users WHERE id = ?", (user_id,)
            ).fetchone()
        return dict(zip(("id", "email", "name", "role", "organization_id"), row)) if row else None

    def _require_user(self) -> dict[str, str] | None:
        user = self._user()
        if not user:
            self._json(HTTPStatus.UNAUTHORIZED, {"error": "authentication_required"})
        return user

    def do_GET(self) -> None:
        if self._rate_limited():
            return
        if not self._secure_configuration():
            self._json(HTTPStatus.SERVICE_UNAVAILABLE, {"error": "secure_secret_required"})
            return
        route = urlparse(self.path).path
        if route == "/api/health":
            self._json(HTTPStatus.OK, {"status": "ok"})
            return
        if not route.startswith("/api/"):
            relative = "index.html" if route == "/" else route.removeprefix("/")
            requested = (ROOT / relative).resolve()
            if ROOT not in requested.parents and requested != ROOT:
                self._json(HTTPStatus.NOT_FOUND, {"error": "not_found"})
                return
            if not requested.is_file():
                self._json(HTTPStatus.NOT_FOUND, {"error": "not_found"})
                return
            body = requested.read_bytes()
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", mimetypes.guess_type(requested.name)[0] or "application/octet-stream")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        user = self._require_user()
        if not user:
            return
        with sqlite3.connect(DATABASE) as connection:
            if route == "/api/session":
                self._json(HTTPStatus.OK, {"user": user})
            elif route == "/api/deals":
                rows = connection.execute(
                    "SELECT id, name, value, stage, owner_id FROM deals WHERE organization_id = ? ORDER BY id",
                    (user["organization_id"],),
                ).fetchall()
                self._json(HTTPStatus.OK, {"deals": [dict(zip(("id", "name", "value", "stage", "owner_id"), row)) for row in rows]})
            elif route == "/api/members":
                rows = connection.execute(
                    "SELECT id, email, name, role FROM users WHERE organization_id = ? ORDER BY name",
                    (user["organization_id"],),
                ).fetchall()
                self._json(HTTPStatus.OK, {"members": [dict(zip(("id", "email", "name", "role"), row)) for row in rows]})
            elif route == "/api/audit":
                rows = connection.execute(
                    "SELECT actor_id, action, resource, created_at FROM audit_events WHERE organization_id = ? ORDER BY id DESC",
                    (user["organization_id"],),
                ).fetchall()
                self._json(HTTPStatus.OK, {"events": [dict(zip(("actor_id", "action", "resource", "created_at"), row)) for row in rows]})
            else:
                self._json(HTTPStatus.NOT_FOUND, {"error": "not_found"})

    def do_POST(self) -> None:
        if self._rate_limited():
            return
        if not self._secure_configuration():
            self._json(HTTPStatus.SERVICE_UNAVAILABLE, {"error": "secure_secret_required"})
            return
        route = urlparse(self.path).path
        body = self._body()
        if body is None:
            self._json(HTTPStatus.BAD_REQUEST, {"error": "invalid_json"})
            return
        if route == "/api/login":
            email, password = body.get("email"), body.get("password")
            if not isinstance(email, str) or not isinstance(password, str):
                self._json(HTTPStatus.BAD_REQUEST, {"error": "email_and_password_required"})
                return
            with sqlite3.connect(DATABASE) as connection:
                row = connection.execute(
                    "SELECT id, email, name, role, organization_id, password_salt, password_hash FROM users WHERE email = ?",
                    (email,),
                ).fetchone()
            if not row or not hmac.compare_digest(password_digest(password, row[5]), row[6]):
                self._json(HTTPStatus.UNAUTHORIZED, {"error": "invalid_credentials"})
                return
            self._json(HTTPStatus.OK, {"user": dict(zip(("id", "email", "name", "role", "organization_id"), row[:5])), "token": encode_session(row[0])})
            return
        user = self._require_user()
        if not user:
            return
        if route == "/api/deals":
            if user["role"] != "manager":
                self._json(HTTPStatus.FORBIDDEN, {"error": "permission_denied"})
                return
            name, value, stage = body.get("name"), body.get("value"), body.get("stage")
            if not isinstance(name, str) or not name.strip() or not isinstance(value, int) or value < 0 or not isinstance(stage, str):
                self._json(HTTPStatus.BAD_REQUEST, {"error": "invalid_deal"})
                return
            with sqlite3.connect(DATABASE) as connection:
                cursor = connection.execute(
                    "INSERT INTO deals (organization_id, name, value, stage, owner_id) VALUES (?, ?, ?, ?, ?)",
                    (user["organization_id"], name.strip(), value, stage, user["id"]),
                )
                connection.execute(
                    "INSERT INTO audit_events (organization_id, actor_id, action, resource, created_at) VALUES (?, ?, ?, ?, ?)",
                    (user["organization_id"], user["id"], "deal.create", f"deal:{cursor.lastrowid}", int(time.time())),
                )
            self._json(HTTPStatus.CREATED, {"id": cursor.lastrowid})
            return
        if route == "/api/invitations":
            if user["role"] != "manager":
                self._json(HTTPStatus.FORBIDDEN, {"error": "permission_denied"})
                return
            email = body.get("email")
            if not isinstance(email, str) or "@" not in email:
                self._json(HTTPStatus.BAD_REQUEST, {"error": "invalid_email"})
                return
            with sqlite3.connect(DATABASE) as connection:
                connection.execute(
                    "INSERT INTO audit_events (organization_id, actor_id, action, resource, created_at) VALUES (?, ?, ?, ?, ?)",
                    (user["organization_id"], user["id"], "member.invite", email, int(time.time())),
                )
            self._json(HTTPStatus.ACCEPTED, {"status": "queued"})
            return
        self._json(HTTPStatus.NOT_FOUND, {"error": "not_found"})

    def log_message(self, format: str, *args: Any) -> None:
        return


def run(host: str = "0.0.0.0", port: int = 4173) -> None:
    initialize_database()
    ThreadingHTTPServer((host, port), APIHandler).serve_forever()


if __name__ == "__main__":
    run()
