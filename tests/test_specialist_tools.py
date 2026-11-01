"""Tests for safe specialist-tool wrappers."""

import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class SpecialistToolTests(unittest.TestCase):
    def test_zap_requires_explicit_authorization(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/run_zap_baseline.py", "https://example.com"],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("refusing to scan without --authorized", result.stderr)

    def test_agent_inventory_is_json(self) -> None:
        result = subprocess.run(
            [sys.executable, "scripts/verify_agent_runtimes.py"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        self.assertIn("claude_code", result.stdout)
        self.assertIn("codex", result.stdout)
        self.assertIn("cursor", result.stdout)
        self.assertIn("windsurf", result.stdout)
