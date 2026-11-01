# Contributing

## Before changing files

Read [`SKILL.md`](./SKILL.md), [`core/project-discovery.md`](./core/project-discovery.md), and the relevant module. Preserve the modular structure and avoid duplicating guidance across entry points.

## Documentation changes

- Keep skill frontmatter valid and names aligned with their folders.
- Use relative links for local files.
- State whether guidance is implemented, documented, integrated, tested, deferred, or blocked.
- Never describe an external tool as installed or verified without execution evidence.

## Validation

Run:

```bash
python3 tests/validate_docs.py
python3 -m py_compile tests/validate_docs.py tests/run_validation_hook.py
```

Update [`TASK_TRACKER.md`](./TASK_TRACKER.md) and [`VALIDATION_REPORT.md`](./VALIDATION_REPORT.md) when a phase or verification result changes.
