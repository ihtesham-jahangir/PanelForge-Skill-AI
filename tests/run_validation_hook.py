"""Run PanelForge validation as a non-destructive agent lifecycle hook."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    sys.stdin.read()
    result = subprocess.run(
        [sys.executable, str(ROOT / "tests" / "validate_docs.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    output = (result.stdout + result.stderr).strip()
    if result.returncode:
        print(
            json.dumps(
                {
                    "stopReason": "PanelForge documentation validation failed.",
                    "systemMessage": output or "Run tests/validate_docs.py for details.",
                }
            )
        )
        return 2
    print(json.dumps({"systemMessage": output or "PanelForge validation passed."}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
