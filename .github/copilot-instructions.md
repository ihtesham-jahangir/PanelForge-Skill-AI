# PanelForge AI Project Guidelines

## Architecture

This repository is a documentation-first, modular coding-agent skill. Keep the root [`SKILL.md`](../SKILL.md) as the canonical orchestrator and place domain guidance in the existing `core/`, `modules/`, `design-engine/`, `orchestration/`, and `quality/` directories.

For new websites and web applications, apply the mandatory default stack:
Next.js/React/TypeScript/Tailwind CSS in a separate frontend; Python/FastAPI
with Pydantic, SQLAlchemy 2.0, and Alembic in a separate backend; and
PostgreSQL. Connect the applications with documented REST APIs and keep
business logic, authentication, authorization, and database operations in
FastAPI. Inspect existing projects first and explain migration implications;
only override this stack when the user explicitly asks.

## Content standards

- Preserve progressive loading: keep entry files concise and link to focused modules.
- Never claim an external skill, installation, test, or deployment was verified without evidence.
- Keep authorization, tenant isolation, accessibility, and responsive behavior explicit.
- Update [`TASK_TRACKER.md`](../TASK_TRACKER.md) and [`VALIDATION_REPORT.md`](../VALIDATION_REPORT.md) when implementation or verification status changes.

## Validation

Run `python3 tests/validate_docs.py` after documentation changes.
