"""Tests for the quick-start application's stack policy reporting."""

import unittest

from scripts.quick_start import DEFAULT_APPLICATION_STACK


class ApplicationStackPolicyTests(unittest.TestCase):
    def test_new_application_default_is_explicit(self) -> None:
        self.assertEqual(
            DEFAULT_APPLICATION_STACK["frontend"],
            ["Next.js", "React", "TypeScript", "Tailwind CSS"],
        )
        self.assertEqual(
            DEFAULT_APPLICATION_STACK["backend"],
            ["Python", "FastAPI", "Pydantic", "SQLAlchemy 2.0", "Alembic"],
        )
        self.assertEqual(DEFAULT_APPLICATION_STACK["database"], ["PostgreSQL"])

    def test_frontend_backend_boundary_is_separate_rest(self) -> None:
        self.assertIn("Separate applications", DEFAULT_APPLICATION_STACK["integration"])
        self.assertIn("REST APIs", DEFAULT_APPLICATION_STACK["integration"])
