"""Run an OWASP ZAP baseline scan against an explicitly authorized target."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", help="authorized HTTP(S) target URL")
    parser.add_argument("--authorized", action="store_true", help="confirm authorization to scan")
    parser.add_argument("--output", type=Path, default=Path("artifacts/zap-baseline.html"))
    args = parser.parse_args()

    parsed = urlparse(args.url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        parser.error("url must be an absolute http:// or https:// URL")
    if not args.authorized:
        parser.error("refusing to scan without --authorized")

    executable = shutil.which("zap-baseline.py") or shutil.which("zap.sh")
    if not executable:
        parser.error("OWASP ZAP is unavailable; install it in the authorized scan environment")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    command = [executable, "-t", args.url, "-r", str(args.output)]
    if Path(executable).name == "zap.sh":
        command = [executable, "-cmd", "-quickurl", args.url, "-quickout", str(args.output)]
    subprocess.run(command, check=True)
    print(f"ZAP baseline report written to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
