# PanelForge AI Project Guidelines

## Architecture

This repository is a documentation-first, modular coding-agent skill. Keep the root [`SKILL.md`](../SKILL.md) as the canonical orchestrator and place domain guidance in the existing `core/`, `modules/`, `design-engine/`, `orchestration/`, and `quality/` directories.

## Content standards

- Preserve progressive loading: keep entry files concise and link to focused modules.
- Never claim an external skill, installation, test, or deployment was verified without evidence.
- Keep authorization, tenant isolation, accessibility, and responsive behavior explicit.
- Update [`TASK_TRACKER.md`](../TASK_TRACKER.md) and [`VALIDATION_REPORT.md`](../VALIDATION_REPORT.md) when implementation or verification status changes.

## Validation

Run `python3 tests/validate_docs.py` after documentation changes.
