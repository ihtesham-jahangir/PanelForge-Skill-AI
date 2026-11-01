"""Validate PanelForge's documentation graph and machine-readable registry."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IGNORED_PARTS = {"node_modules", "artifacts", "test-results"}
LINK_RE = re.compile(r"\]\(([^)#]+)(?:#[^)]+)?\)")
FRONTMATTER_NAME_RE = re.compile(r"^name:\s*([a-z0-9-]+)\s*$", re.MULTILINE)
FRONTMATTER_DESCRIPTION_RE = re.compile(r"^description:\s*.+$", re.MULTILINE)


def markdown_files() -> list[Path]:
    return sorted(
        path for path in ROOT.rglob("*.md") if not IGNORED_PARTS.intersection(path.parts)
    )


def check_links() -> list[str]:
    errors: list[str] = []
    for path in markdown_files():
        for target in LINK_RE.findall(path.read_text(encoding="utf-8")):
            if "://" in target or target.startswith("mailto:"):
                continue
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)} -> missing {target}")
    return errors


def check_json_examples() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*.json"):
        if IGNORED_PARTS.intersection(path.parts):
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
    return errors


def check_skill_metadata() -> list[str]:
    errors: list[str] = []
    for path in ROOT.glob(".github/skills/*/SKILL.md"):
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"{path.relative_to(ROOT)}: missing frontmatter")
            continue
        match = FRONTMATTER_NAME_RE.search(text.split("---\n", 2)[1])
        expected = path.parent.name
        if not match or match.group(1) != expected:
            errors.append(f"{path.relative_to(ROOT)}: name must match folder {expected!r}")
    return errors


def check_customization_metadata() -> list[str]:
    errors: list[str] = []
    for pattern in (".github/prompts/*.prompt.md", ".github/agents/*.agent.md"):
        for path in ROOT.glob(pattern):
            text = path.read_text(encoding="utf-8")
            if not text.startswith("---\n") or "---\n" not in text[4:]:
                errors.append(f"{path.relative_to(ROOT)}: missing frontmatter")
                continue
            frontmatter = text.split("---\n", 2)[1]
            if not FRONTMATTER_DESCRIPTION_RE.search(frontmatter):
                errors.append(f"{path.relative_to(ROOT)}: missing description")
    return errors


def check_hook_configs() -> list[str]:
    errors: list[str] = []
    for path in ROOT.glob(".github/hooks/*.json"):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"{path.relative_to(ROOT)}: {exc}")
            continue
        hooks = data.get("hooks")
        if not isinstance(hooks, dict):
            errors.append(f"{path.relative_to(ROOT)}: hooks must be an object")
            continue
        for event, commands in hooks.items():
            if not isinstance(commands, list):
                errors.append(f"{path.relative_to(ROOT)}: {event} must be a list")
                continue
            for command in commands:
                if command.get("type") != "command" or not command.get("command"):
                    errors.append(f"{path.relative_to(ROOT)}: invalid command in {event}")
    return errors


def check_registry_yaml() -> list[str]:
    path = ROOT / "orchestration" / "skills-registry.yaml"
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    if not text.startswith("skills:\n"):
        errors.append("orchestration/skills-registry.yaml: missing skills root")
    entries = text.count("  - id: ")
    if entries == 0:
        errors.append("orchestration/skills-registry.yaml: no skill entries")
    for line_number, line in enumerate(text.splitlines(), 1):
        if "\t" in line:
            errors.append(f"orchestration/skills-registry.yaml:{line_number}: tabs are not allowed")
        if line.startswith("    status: ") and not line.removeprefix("    status: ").strip():
            errors.append(f"orchestration/skills-registry.yaml:{line_number}: empty status")
    return errors


def check_compliance_status() -> list[str]:
    path = ROOT / "compliance-status.json"
    if not path.exists():
        return ["missing required file: compliance-status.json"]
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"compliance-status.json: {exc}"]
    errors: list[str] = []
    if data.get("schema_version") != 1:
        errors.append("compliance-status.json: schema_version must be 1")
    areas = data.get("areas")
    if not isinstance(areas, dict) or not areas:
        return ["compliance-status.json: areas must be a non-empty object"]
    allowed = {"verified", "partial", "unverified", "blocked"}
    for name, area in areas.items():
        if not isinstance(area, dict):
            errors.append(f"compliance-status.json: {name} must be an object")
            continue
        if area.get("status") not in allowed:
            errors.append(f"compliance-status.json: {name} has an invalid status")
        if not isinstance(area.get("evidence"), list) or not area["evidence"]:
            errors.append(f"compliance-status.json: {name} needs evidence")
    return errors


def main() -> int:
    errors = (
        check_links()
        + check_json_examples()
        + check_skill_metadata()
        + check_customization_metadata()
        + check_hook_configs()
        + check_registry_yaml()
        + check_compliance_status()
    )
    required = [
        ROOT / "SKILL.md",
        ROOT / "GETTING_STARTED.md",
        ROOT / "orchestration" / "skills-registry.yaml",
    ]
    errors.extend(f"missing required file: {path.relative_to(ROOT)}" for path in required if not path.exists())
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(markdown_files())} Markdown files and registry presence.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
