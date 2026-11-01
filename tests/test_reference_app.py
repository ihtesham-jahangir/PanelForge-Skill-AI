"""Static smoke checks for the PanelForge reference application."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1] / "reference-app"


class ReferenceAppTests(unittest.TestCase):
    def test_assets_exist(self) -> None:
        self.assertTrue(all((ROOT / name).is_file() for name in ("index.html", "styles.css", "app.js", "README.md")))

    def test_has_accessible_structure(self) -> None:
        html = (ROOT / "index.html").read_text(encoding="utf-8")
        for required in ('lang="en"', 'id="main-content"', 'aria-label="Primary navigation"', 'aria-live="polite"', 'rel="stylesheet"'):
            self.assertIn(required, html)

    def test_has_permission_preview(self) -> None:
        javascript = (ROOT / "app.js").read_text(encoding="utf-8")
        self.assertIn("Permission denied", javascript)
        self.assertIn("roleSelect.value", javascript)
