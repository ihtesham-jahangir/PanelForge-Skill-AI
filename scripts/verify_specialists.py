"""Report locally available specialist runtimes and agent customization paths."""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    commands = ("node", "npm", "npx", "python3", "docker", "playwright", "lighthouse", "zap")
    command_status = {
        command: shutil.which(command) or None
        for command in commands
    }
    workspace_bins = ROOT / "qa" / "browser" / "node_modules" / ".bin"
    for command in ("playwright", "lighthouse"):
        if command_status[command] is None:
            candidate = workspace_bins / command
            if candidate.exists():
                command_status[command] = str(candidate)
    paths = {
        "workspace_copilot_skill": (ROOT / ".github" / "skills" / "panelforge-ai").is_dir(),
        "user_copilot_skills": (Path.home() / ".copilot" / "skills").is_dir(),
        "user_agents_skills": (Path.home() / ".agents" / "skills").is_dir(),
        "user_claude_skills": (Path.home() / ".claude" / "skills").is_dir(),
        "user_cursor": (Path.home() / ".cursor").is_dir(),
        "user_windsurf": (Path.home() / ".windsurf").is_dir(),
    }
    report = {
        "python": sys.version.split()[0],
        "commands": command_status,
        "paths": paths,
        "installations_performed": [],
        "limitations": [
            "Command presence does not prove a tool is configured or compatible.",
            "Absent tools were not installed automatically.",
            "Agent-specific discovery still requires testing inside each agent runtime.",
        ],
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
