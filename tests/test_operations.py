"""Static checks for deployment and operational safety artifacts."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class OperationsTests(unittest.TestCase):
    def test_container_requires_secret_and_non_root_user(self) -> None:
        dockerfile = (ROOT / "reference-app" / "Dockerfile").read_text(encoding="utf-8")
        self.assertIn("USER panelforge", dockerfile)
        self.assertIn("PANELFORGE_ENV=production", dockerfile)

    def test_compose_requires_runtime_secret(self) -> None:
        compose = (ROOT / "reference-app" / "docker-compose.yml").read_text(encoding="utf-8")
        self.assertIn("PANELFORGE_SESSION_SECRET: ${PANELFORGE_SESSION_SECRET", compose)
        self.assertIn("no-new-privileges:true", compose)

    def test_operations_runbook_has_restore_and_rollback(self) -> None:
        runbook = (ROOT / "reference-app" / "OPERATIONS.md").read_text(encoding="utf-8")
        self.assertIn("--restore", runbook)
        self.assertIn("run_operations_drill.py", runbook)
        self.assertIn("Rollback", runbook)
