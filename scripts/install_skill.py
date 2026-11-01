"""Install the PanelForge Copilot skill into a project-local .github directory."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".github" / "skills" / "panelforge-ai"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "target",
        type=Path,
        help="Target project directory that will receive .github/skills/panelforge-ai",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace an existing PanelForge skill directory",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show the destination without writing files",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    target = args.target.expanduser().resolve()
    destination = target / ".github" / "skills" / SOURCE.name

    if not SOURCE.is_dir() or not (SOURCE / "SKILL.md").is_file():
        print(f"Source skill is incomplete: {SOURCE}", file=sys.stderr)
        return 1
    if destination.exists() and not args.force:
        print(
            f"Destination already exists: {destination}. "
            "Use --force only when replacement is intentional.",
            file=sys.stderr,
        )
        return 2
    if args.dry_run:
        print(f"Would install {SOURCE} -> {destination}")
        return 0

    target.mkdir(parents=True, exist_ok=True)
    if destination.exists():
        shutil.rmtree(destination)
    shutil.copytree(SOURCE, destination)
    print(f"Installed PanelForge skill to {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
