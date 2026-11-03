# Capability Gaps and Release Gate

This document is a boundary for what PanelForge may claim. Generated
scaffolding is not production evidence. Every capability must be marked
`implemented`, `unverified`, `blocked`, or `requires-human-decision`.

## Preflight questionnaire

Ask focused questions before choosing a data model, authorization model, or
irreversible workflow. Record answers and assumptions in the project brief.

- What are the required terminology, lifecycle states, fields, conversions,
  pipelines, stage exit criteria, forecasts, quotas, and commissions?
- What roles, teams, approval boundaries, visibility rules, administrator
  powers, ownership rules, and tenant hierarchy are required?
- What are the retention, legal hold, deletion, export, residency, and
  offboarding policies?
- How should duplicates be matched, merged, reconciled, and assigned, and
  which source is authoritative?
- What are the SLA, escalation, business-calendar, timezone, and notification
  requirements?
- What pricing, billing, usage, limits, entitlements, and metering behavior is
  required?
- Which external systems are required, and which system owns each record?
- Which deployment environments, operators, recovery targets, monitoring,
  rollback, browser, locale, and accessibility requirements apply?

Do not invent an answer when it changes security, legal obligations, billing,
data loss, or an irreversible migration. Mark the item
`requires-human-decision`.

## Evidence and capability matrix

Create a matrix for each deliverable. `implemented` means code or
documentation exists; it does not mean it ran in a representative environment.
Use `unverified` for cloud-dependent or environment-dependent work,
`blocked` when a prerequisite prevents implementation, and
`requires-human-decision` when product or policy input is missing.

| Area | Required evidence or decision | State |
|---|---|---|
| Product workflows | Approved terminology, lifecycle, pipeline, SLA, billing, and ownership rules | requires-human-decision until recorded |
| Authorization and tenancy | Server-side positive/negative tests and approved role/tenant model | unverified until executed and reviewed |
| Integrations | Explicit configuration, signed webhooks, idempotency, bounded retries, and provider evidence | unverified until exercised |
| Data and migration | Mapping, reversible dry run, reconciliation, duplicate strategy, cutover, rollback, and sign-off | requires-human-decision until approved |
| Operations | Production migrations, backups, restore drill, monitoring, alerts, deployment, rollback, and ownership | unverified until executed |
| Security and compliance | Threat model, regression tests, authorized testing, legal review, and policy evidence | unverified; never claim compliance by default |
| UI quality | Loading, empty, error, timeout, retry, offline, denied, keyboard, screen reader, responsive, locale, and browser evidence | unverified until exercised |
| Reporting | Reproducible definitions, permission-aware aggregates, exports, and scheduled-report evidence | unverified until tested |

## Mandatory implementation boundaries

- Treat migrations, seed data, tests, and production configuration as separate
  deliverables; CRUD scaffolding does not imply any of them.
- Every UI module needs explicit loading, empty, error, retry, partial-failure,
  offline/timeout where relevant, and permission-denied states.
- Every collection API needs pagination, filtering, authorization tests, audit
  events, and ownership/tenant tests.
- Integration adapters must fail visibly when required environment variables are
  absent. Never fabricate provider responses or commit credentials.
- Use signed webhooks, replay protection, idempotency keys, bounded retries,
  dead-letter/recovery state, and execution evidence for integrations and jobs.
- Generate a final implementation report listing completed work and known
  non-generated work.

## Release gate

Do not describe a system as production-ready, secure, compliant, migrated, or
integrated without executed evidence for the relevant environment. Review:

- accessibility, browser/responsive, localization, and performance evidence;
- security tests, dependency audit, threat-model review, and authorized testing;
- migration, backup/restore, retention, export/deletion, and rollback evidence;
- observability, alerting, deployment promotion, incident ownership, and
  recovery runbooks; and
- human approval for product, authorization, legal, billing, integration, and
  irreversible data decisions.

Fabricated records are never evidence that migration, reconciliation, provider
delivery, or recovery works.
