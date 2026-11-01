import tempfile
import unittest
from pathlib import Path

from scripts.scaffold_project import FILES, main


class ScaffoldProjectTests(unittest.TestCase):
    def test_scaffold_creates_required_boundaries(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory) / "app"
            import sys

            original = sys.argv
            try:
                sys.argv = ["scaffold_project", str(target)]
                self.assertEqual(main(), 0)
            finally:
                sys.argv = original
            self.assertEqual(len([path for path in target.rglob("*") if path.is_file()]), len(FILES))
            self.assertIn("fastapi", (target / "backend/pyproject.toml").read_text())
            self.assertIn("postgres", (target / "docker-compose.yml").read_text())
            self.assertTrue((target / "frontend/tailwind.config.ts").is_file())
            self.assertTrue((target / "backend/alembic.ini").is_file())
            self.assertIn("GET /health", (target / "README.md").read_text())

    def test_scaffold_refuses_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            target = Path(directory)
            (target / "README.md").write_text("keep", encoding="utf-8")
            import sys

            original = sys.argv
            try:
                sys.argv = ["scaffold_project", str(target)]
                self.assertEqual(main(), 2)
            finally:
                sys.argv = original
