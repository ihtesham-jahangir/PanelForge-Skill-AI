"""Authorization and tenant-isolation tests for the reference API."""

from __future__ import annotations

import json
import os
import tempfile
import threading
import unittest
import sys
from http.client import HTTPConnection
from pathlib import Path

from http.server import ThreadingHTTPServer

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "reference-app"))
import server as reference_app_server

APIHandler = reference_app_server.APIHandler
initialize_database = reference_app_server.initialize_database


class ReferenceAPITests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temp_dir = tempfile.TemporaryDirectory()
        cls.db = Path(cls.temp_dir.name) / "test.sqlite3"
        reference_app_server.DATABASE = cls.db
        initialize_database(cls.db)
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), APIHandler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.port = cls.server.server_address[1]

    @classmethod
    def tearDownClass(cls) -> None:
        cls.server.shutdown()
        cls.thread.join(timeout=3)
        cls.temp_dir.cleanup()

    def request(self, method: str, path: str, body: dict | None = None, token: str | None = None) -> tuple[int, dict]:
        connection = HTTPConnection("127.0.0.1", self.port)
        headers = {"Content-Type": "application/json"} if body is not None else {}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        connection.request(method, path, json.dumps(body).encode() if body is not None else None, headers)
        response = connection.getresponse()
        payload = json.loads(response.read())
        connection.close()
        return response.status, payload

    def login(self, email: str) -> str:
        status, payload = self.request("POST", "/api/login", {"email": email, "password": "demo-password"})
        self.assertEqual(status, 200)
        return payload["token"]

    def test_requires_authentication(self) -> None:
        status, payload = self.request("GET", "/api/deals")
        self.assertEqual((status, payload["error"]), (401, "authentication_required"))

    def test_tenant_isolation(self) -> None:
        status, payload = self.request("GET", "/api/deals", token=self.login("maya@northstar.example"))
        self.assertEqual(status, 200)
        self.assertTrue(all(deal["name"] != "Private Deal" for deal in payload["deals"]))

    def test_member_cannot_create_deal(self) -> None:
        status, payload = self.request("POST", "/api/deals", {"name": "Forbidden", "value": 1, "stage": "Qualified"}, self.login("jon@northstar.example"))
        self.assertEqual((status, payload["error"]), (403, "permission_denied"))

    def test_manager_can_create_and_audit(self) -> None:
        token = self.login("maya@northstar.example")
        status, payload = self.request("POST", "/api/deals", {"name": "New Account", "value": 1000, "stage": "Qualified"}, token)
        self.assertEqual(status, 201)
        status, audit = self.request("GET", "/api/audit", token=token)
        self.assertEqual(status, 200)
        self.assertTrue(any(event["action"] == "deal.create" for event in audit["events"]))

    def test_invalid_credentials_are_rejected(self) -> None:
        status, payload = self.request("POST", "/api/login", {"email": "maya@northstar.example", "password": "wrong"})
        self.assertEqual((status, payload["error"]), (401, "invalid_credentials"))

    def test_security_headers_are_present(self) -> None:
        connection = HTTPConnection("127.0.0.1", self.port)
        connection.request("GET", "/api/health")
        response = connection.getresponse()
        self.assertEqual(response.getheader("X-Content-Type-Options"), "nosniff")
        self.assertEqual(response.getheader("X-Frame-Options"), "DENY")
        connection.close()

    def test_production_rejects_default_secret(self) -> None:
        previous = os.environ.get("PANELFORGE_ENV")
        os.environ["PANELFORGE_ENV"] = "production"
        try:
            status, payload = self.request("GET", "/api/health")
        finally:
            if previous is None:
                os.environ.pop("PANELFORGE_ENV", None)
            else:
                os.environ["PANELFORGE_ENV"] = previous
        self.assertEqual((status, payload["error"]), (503, "secure_secret_required"))
