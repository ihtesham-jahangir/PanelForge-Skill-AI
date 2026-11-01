"""Create or restore a consistent SQLite backup for the reference application."""

from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("database", type=Path)
    parser.add_argument("backup", type=Path)
    parser.add_argument("--restore", action="store_true")
    args = parser.parse_args()
    args.database.parent.mkdir(parents=True, exist_ok=True)
    if args.restore:
        if not args.backup.is_file():
            parser.error(f"backup does not exist: {args.backup}")
        source = sqlite3.connect(args.backup)
        destination = sqlite3.connect(args.database)
        try:
            source.backup(destination)
        finally:
            destination.close()
            source.close()
        print(f"Restored {args.backup} -> {args.database}")
        return 0
    if not args.database.is_file():
        parser.error(f"database does not exist: {args.database}")
    source = sqlite3.connect(args.database)
    destination = sqlite3.connect(args.backup)
    try:
        source.backup(destination)
    finally:
        destination.close()
        source.close()
    print(f"Backed up {args.database} -> {args.backup}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
