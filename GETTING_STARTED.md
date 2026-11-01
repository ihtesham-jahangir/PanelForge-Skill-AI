# Getting started

Use the shortest path that matches your task.

## 1. Validate the workspace

```bash
python3 scripts/quick_start.py
```

Use `--json` for CI integrations or `--skip-browser` when browser dependencies
are unavailable.

## 2. Choose the workflow

| Need | Start here | Load next |
|---|---|---|
| New product or feature | `.github/prompts/panelforge-discovery.prompt.md` | `core/requirements.md`, `core/architecture.md` |
| Admin panel | `.github/agents/panelforge-engineer.agent.md` | `modules/admin.md`, `modules/security.md` |
| Customer/user portal | `.github/agents/panelforge-engineer.agent.md` | `modules/user.md`, `modules/security.md` |
| CRM workflow | `.github/agents/panelforge-engineer.agent.md` | `modules/crm.md`, `modules/database.md` |
| UI/design system | `.github/prompts/panelforge-design-system.prompt.md` | `design-engine/README.md`, `modules/ui-ux.md` |
| Security and QA | `.github/prompts/panelforge-security-qa.prompt.md` | `modules/security.md`, `quality/README.md` |
| Release readiness | `quality/production-readiness.md` | `quality/release-checklist.md` |

## 3. Apply the non-negotiables

- Preserve the existing stack unless migration is approved.
- Enforce authorization and tenant ownership server-side.
- Define loading, empty, error, permission, and success states.
- Add focused tests with implementation changes.
- Report executed evidence separately from unverified work.

## 4. Run targeted verification

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
cd qa/browser && npm test
```

Use the browser command only when its dependencies and Chromium are installed.
The complete evidence summary is in [`VALIDATION_REPORT.md`](./VALIDATION_REPORT.md).
