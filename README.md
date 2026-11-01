<div align="center">
  <img src="./logo.png" alt="PanelForge AI logo" width="520">
  <h1>PanelForge AI</h1>
  <p><strong>A production-minded engineering skill for admin panels, portals, CRM systems, and SaaS products.</strong></p>
  <p>
    <a href="./GETTING_STARTED.md">Get started</a> ·
    <a href="./SKILL.md">Read the skill</a> ·
    <a href="./reference-app/">Run the reference app</a> ·
    <a href="./MASTER_PROMPT_AUDIT.md">View audit</a>
  </p>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/status-local%20workflow%20verified-16a34a" alt="Local workflow verified">
  <img src="https://img.shields.io/badge/tests-15%20passed-2563eb" alt="15 tests passed">
  <img src="https://img.shields.io/badge/browser%20QA-12%20passed-7c3aed" alt="12 browser tests passed">
  <img src="https://img.shields.io/badge/license-see%20repository-64748b" alt="License information">
</p>

## What it is

PanelForge AI is a modular, progressive-loading engineering skill that helps
coding agents build reliable business software without skipping the difficult
parts: requirements, architecture, design systems, RBAC, tenancy, security,
accessibility, testing, operations, and release evidence.

It is designed to be useful in an existing repository, not just for greenfield
mockups. The skill preserves the current stack, loads only relevant guidance,
and reports verified work separately from assumptions or environment blockers.

## Why teams use it

| Productivity outcome | How PanelForge delivers it |
|---|---|
| Faster discovery | Structured project inspection, business workflows, acceptance criteria, and a short task-to-module route |
| Fewer architecture mistakes | Admin, user, CRM, full-stack, database, tenancy, security, and delivery contracts |
| Consistent implementation | Reusable prompts, agent instructions, templates, style records, and engineering standards |
| Fewer regressions | API auth/RBAC/tenant tests, browser/axe tests, operations drills, container health checks, and Lighthouse |
| Executable confidence | A dependency-light reference admin/CRM application with SQLite API and hardened container artifacts |
| Honest delivery | Machine-readable compliance status plus verified, partial, unverified, and blocked states |

## Quick start

```bash
# Clone or copy the repository, then run the complete local workflow
python3 scripts/quick_start.py
```

The workflow detects the stack, validates documentation, runs the test suite,
executes backup/restore checks, verifies the reference app health endpoint, and
runs Playwright/axe browser QA when the optional workspace dependencies exist.

For CI integrations:

```bash
python3 scripts/quick_start.py --json
```

For environments without browser dependencies:

```bash
python3 scripts/quick_start.py --skip-browser
```

See [`GETTING_STARTED.md`](./GETTING_STARTED.md) for the shortest route from a
feature request to the right PanelForge modules.

## Reference application

The included [reference app](./reference-app/) demonstrates a responsive,
enterprise-style CRM workspace with:

- Overview, pipeline, people, and audit activity views.
- SQLite-backed API with signed sessions and PBKDF2 password hashing.
- Server-side roles, tenant-scoped queries, audit events, request limits, and security headers.
- Non-root Docker runtime, read-only filesystem support, health checks, backup/restore, and rollback guidance.

Run it locally:

```bash
python3 reference-app/server.py
```

Open <http://127.0.0.1:4173>.

## Design examples

PanelForge supports deliberate visual direction instead of generic dashboards.
These repository-owned examples show how the design engine can guide different
product contexts:

<table>
  <tr>
    <td align="center"><img src="./docs/images/glassmorphism-dashboard.svg" alt="Glassmorphism dashboard example" width="100%"><br><strong>Glassmorphism</strong><br><sub>High-signal analytics and premium product surfaces</sub></td>
    <td align="center"><img src="./docs/images/bento-saas-dashboard.svg" alt="Bento SaaS dashboard example" width="100%"><br><strong>Bento SaaS</strong><br><sub>Modular metrics and fast operational scanning</sub></td>
  </tr>
  <tr>
    <td align="center" colspan="2"><img src="./docs/images/enterprise-crm-dashboard.svg" alt="Enterprise CRM dashboard example" width="76%"><br><strong>Enterprise CRM</strong><br><sub>Dense workflows, pipeline visibility, and role-aware actions</sub></td>
  </tr>
</table>

Browse the complete [style catalog](./design-engine/style-catalog.md).

## Repository map

| Directory | Purpose |
|---|---|
| [`core/`](./core/) | Discovery, requirements, architecture, and delivery |
| [`modules/`](./modules/) | UI/UX, admin, user, CRM, full-stack, database, and security |
| [`design-engine/`](./design-engine/) | Style selection, design tokens, and visual direction |
| [`engineering/`](./engineering/) | Implementation contracts and quality boundaries |
| [`workflows/`](./workflows/) | Repeatable discovery, build, QA, and release workflows |
| [`quality/`](./quality/) | Verification, production readiness, and release evidence |
| [`adapters/`](./adapters/) | Copilot, Claude, Codex, Cursor, Windsurf, and generic guidance |
| [`templates/`](./templates/) | Reusable plans, matrices, briefs, and handoff artifacts |
| [`.github/`](./.github/) | Native Copilot skill, prompts, agent, hooks, and CI |
| [`scripts/`](./scripts/) | Installer, validation, quick-start, operations, and specialist wrappers |
| [`qa/browser/`](./qa/browser/) | Optional Playwright, axe-core, and Lighthouse QA |

## Native Copilot integration

This repository includes a project-local skill at
[`.github/skills/panelforge-ai/SKILL.md`](./.github/skills/panelforge-ai/SKILL.md),
a focused [PanelForge Engineer agent](./.github/agents/panelforge-engineer.agent.md),
reusable [prompts](./.github/prompts/), and a non-destructive
[validation hook](./.github/hooks/panelforge-validation.json).

To install the skill into another project:

```bash
python3 scripts/install_skill.py /path/to/target-project
```

## Verification and boundaries

Current local evidence:

- Documentation validation: 88 Markdown files.
- Repository tests: 15 passed.
- Playwright/axe browser QA: 12 desktop/mobile tests passed.
- Lighthouse: performance 100, accessibility 100, best practices 96, SEO 100.
- Container health, non-root runtime, read-only filesystem, and backup/restore verified.

Read the complete [validation report](./VALIDATION_REPORT.md) and
[machine-readable compliance status](./compliance-status.json). External agent
invocation, OWASP ZAP scanning, HTTPS deployment, monitoring, and remote
rollback remain environment-dependent and are not claimed as completed.

## Contributing

Please read [CONTRIBUTING.md](./CONTRIBUTING.md) and [SECURITY.md](./SECURITY.md).
Keep changes focused, add directly related tests, preserve existing patterns,
and include actual verification evidence.

## License

No license file is currently declared. Add an appropriate `LICENSE` file before
redistributing this repository.
