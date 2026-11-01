# Reference Application QA Report

- Application: `reference-app/`
- Environment: Python standard-library HTTP server and SQLite, localhost
- Date: 2026-11-01

| Test | Command | Expected | Actual | Result |
|---|---|---|---|---|
| Static smoke tests | `python3 -m unittest discover -s tests -p 'test_*.py' -v` | Three reference-app checks pass | 3 tests passed | PASS |
| HTTP serving | `PANELFORGE_DB=$(mktemp) python3 reference-app/server.py` plus `urllib.request` | `/` returns 200 and app title is present | HTTP 200; `Northstar Operations` found | PASS |
| Documentation graph | `python3 tests/validate_docs.py` | Local references and metadata validate | 83 Markdown files validated | PASS |
| API authorization and isolation | `python3 -m unittest discover -s tests -p 'test_*.py' -v` | Auth, role, audit, tenant, and security-header boundaries hold | 6 API tests passed | PASS |
| Operations artifacts | `python3 -m unittest discover -s tests -p 'test_*.py'` | Container, Compose, backup, restore, and rollback controls are present | Static operations checks pass | PASS |
| Container deployment smoke | `docker build ...` and hardened `docker run ...` | Healthy non-root service with read-only root filesystem serves API | Health status healthy; login API passed | PASS |

## Unverified

No browser automation, screenshot comparison, dependency scan, remote deployment, restore drill, rollback execution, or production performance test is claimed. The local container smoke test does not certify a remote production deployment.
