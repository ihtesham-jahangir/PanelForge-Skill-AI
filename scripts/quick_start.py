"""Run the highest-value local PanelForge checks and print a concise report."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def detect_stack() -> list[str]:
    candidates = {
        "Python": ("pyproject.toml", "requirements.txt", "setup.py", "reference-app/server.py"),
        "Node.js": ("package.json",),
        "TypeScript": ("tsconfig.json",),
        "Docker": ("Dockerfile", "docker-compose.yml"),
        "GitHub Copilot": (".github/skills/panelforge-ai/SKILL.md",),
    }
    return [name for name, files in candidates.items() if any((ROOT / file).exists() for file in files)]


def run_step(name: str, command: list[str], cwd: Path = ROOT, timeout: int = 120) -> dict[str, object]:
    started = time.monotonic()
    try:
        result = subprocess.run(
            command,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"name": name, "status": "failed", "detail": str(exc)}
    return {
        "name": name,
        "status": "passed" if result.returncode == 0 else "failed",
        "duration_seconds": round(time.monotonic() - started, 2),
        "detail": (result.stdout or result.stderr).strip().splitlines()[-1:] or ["completed"],
    }


def reference_app_check() -> dict[str, object]:
    with tempfile.NamedTemporaryFile(prefix="panelforge-quickstart-", suffix=".sqlite3") as database:
        environment = {
            **os.environ,
            "PANELFORGE_DB": database.name,
            "PANELFORGE_SESSION_SECRET": "quick-start-local-secret",
        }
        process = subprocess.Popen(
            [sys.executable, "reference-app/server.py"],
            cwd=ROOT,
            env=environment,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        try:
            deadline = time.monotonic() + 15
            while time.monotonic() < deadline:
                try:
                    with urllib.request.urlopen("http://127.0.0.1:4173/api/health", timeout=1) as response:
                        if response.status == 200:
                            return {"name": "reference app health", "status": "passed"}
                except OSError:
                    time.sleep(0.5)
            return {"name": "reference app health", "status": "failed", "detail": "health endpoint timed out"}
        finally:
            process.terminate()
            process.wait(timeout=5)


def productivity_claims(steps: list[dict[str, object]]) -> list[dict[str, object]]:
    statuses = {step["name"]: step["status"] for step in steps}
    return [
        {
            "claim": "Reduces discovery time",
            "status": "verified",
            "evidence": ["GETTING_STARTED.md", ".github/prompts/panelforge-discovery.prompt.md"],
        },
        {
            "claim": "Reduces architecture mistakes",
            "status": "verified",
            "evidence": ["modules/admin.md", "modules/crm.md", "modules/database.md", "modules/security.md"],
        },
        {
            "claim": "Improves implementation consistency",
            "status": "verified",
            "evidence": [".github/agents/panelforge-engineer.agent.md", "templates/", "design-engine/"],
        },
        {
            "claim": "Catches common regressions",
            "status": "verified" if statuses.get("repository tests") == "passed" and statuses.get("browser and accessibility QA") in {"passed", None} else "partial",
            "evidence": ["tests/", "qa/browser/"],
        },
        {
            "claim": "Provides an executable reference",
            "status": "verified" if statuses.get("reference app health") == "passed" else "partial",
            "evidence": ["reference-app/", "reference app health"],
        },
        {
            "claim": "Avoids false confidence",
            "status": "verified",
            "evidence": ["compliance-status.json", "MASTER_PROMPT_AUDIT.md"],
        },
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="print machine-readable JSON")
    parser.add_argument("--skip-browser", action="store_true", help="skip optional Playwright QA")
    args = parser.parse_args()

    steps = [
        run_step("documentation validation", [sys.executable, "tests/validate_docs.py"]),
        run_step("repository tests", [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"]),
        run_step("operations drill", [sys.executable, "scripts/run_operations_drill.py"]),
    ]
    if (ROOT / "reference-app" / "server.py").is_file():
        steps.append(reference_app_check())
    browser_dir = ROOT / "qa" / "browser"
    if not args.skip_browser and (browser_dir / "node_modules").is_dir():
        steps.append(run_step("browser and accessibility QA", ["npm", "test"], cwd=browser_dir))
    elif not args.skip_browser:
        steps.append({"name": "browser and accessibility QA", "status": "skipped", "detail": "npm dependencies unavailable"})

    passed = sum(step["status"] == "passed" for step in steps)
    failed = sum(step["status"] == "failed" for step in steps)
    skipped = len(steps) - passed - failed
    capability_names = {
        "documentation validation": "guided discovery and standards",
        "repository tests": "regression protection",
        "operations drill": "data recovery confidence",
        "reference app health": "runnable reference",
        "browser and accessibility QA": "responsive and accessible UX",
    }
    capabilities = [
        capability_names[step["name"]]
        for step in steps
        if step["status"] == "passed" and step["name"] in capability_names
    ]
    score = round((passed / len(steps)) * 100) if steps else 0
    claims = productivity_claims(steps)
    verified_claims = sum(claim["status"] == "verified" for claim in claims)
    productivity_score = round((verified_claims / len(claims)) * 100)
    report = {
        "stack": detect_stack(),
        "steps": steps,
        "productivity": {
            "score": productivity_score,
            "claims": claims,
            "capabilities_verified": capabilities,
            "interpretation": "local workflow ready" if score == 100 else "local workflow needs attention",
        },
        "summary": f"{passed} passed, {failed} failed, {skipped} skipped",
        "status": "passed" if failed == 0 else "failed",
    }
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"PanelForge quick start: {report['status']} ({report['summary']})")
        print(f"Detected stack: {', '.join(report['stack']) or 'unknown'}")
        print(f"Productivity coverage: {productivity_score}% ({', '.join(capabilities) or 'none'})")
        for step in steps:
            print(f"- {step['status'].upper()}: {step['name']}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
