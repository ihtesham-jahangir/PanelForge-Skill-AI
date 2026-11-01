"""Report external coding-agent runtimes without installing or modifying them."""

from __future__ import annotations

import json
import shutil
from pathlib import Path


AGENTS = {
    "claude_code": ("claude", (Path.home() / ".claude",)),
    "codex": ("codex", (Path.home() / ".codex", Path.home() / ".agents")),
    "cursor": ("cursor", (Path.home() / ".cursor",)),
    "windsurf": ("windsurf", (Path.home() / ".windsurf",)),
}


def main() -> int:
    report = {}
    for name, (command, paths) in AGENTS.items():
        report[name] = {
            "command": shutil.which(command),
            "known_paths_present": [str(path) for path in paths if path.exists()],
            "status": "available" if shutil.which(command) else "unverified",
        }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
