"""Run a local backup/restore integrity drill without touching application data."""

from __future__ import annotations

import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BACKUP_TOOL = ROOT / "scripts" / "backup_reference_db.py"


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="panelforge-drill-") as directory:
        workdir = Path(directory)
        database = workdir / "reference.sqlite3"
        backup = workdir / "reference.backup.sqlite3"

        with sqlite3.connect(database) as connection:
            connection.execute("CREATE TABLE drill_events (name TEXT NOT NULL)")
            connection.execute("INSERT INTO drill_events VALUES (?)", ("before-restore",))
            connection.commit()

        subprocess.run(
            [sys.executable, str(BACKUP_TOOL), str(database), str(backup)],
            check=True,
        )

        with sqlite3.connect(database) as connection:
            connection.execute("DELETE FROM drill_events")
            connection.execute("INSERT INTO drill_events VALUES (?)", ("mutated",))
            connection.commit()

        subprocess.run(
            [sys.executable, str(BACKUP_TOOL), str(database), str(backup), "--restore"],
            check=True,
        )

        with sqlite3.connect(database) as connection:
            rows = connection.execute("SELECT name FROM drill_events").fetchall()
        if rows != [("before-restore",)]:
            raise RuntimeError(f"restore integrity check failed: {rows!r}")

        print("Operations drill passed: backup and restore preserved database state.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
