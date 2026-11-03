# Admin Panel Engineering

The Admin Panel is the CRM governance and operations command center. It
manages identity, authorization, tenant configuration, integrations, audit
evidence, security monitoring, and controlled data operations. It is not a
second sales workspace.

Use the same decoupled Next.js App Router and FastAPI architecture described in
the [CRM module](./crm.md). Restrict administrative routes with server-side
RBAC and tenant scope checks. Suggested `Admin` and `Super_Admin` roles are
defaults only: confirm role names, hierarchy, powers, approval boundaries, and
visibility rules through the [capability-gap preflight](../quality/capability-gaps.md).

## Identity and access management

Support only the approved identity lifecycle:

- invite staff with expiring, single-use email links;
- activate, suspend, deactivate, reset, and force-invalidate sessions;
- assign roles and granular permissions such as `users.read`,
  `users.invite`, `roles.assign`, `settings.update`, `audit_logs.read`,
  `data.import`, `data.export`, and `financial_metrics.read`; and
- require re-authentication, step-up MFA, dual approval, or a confirmation
  reason for sensitive changes according to policy.

Every action is authorized server-side, including exports, bulk actions,
background jobs, API keys, impersonation, and direct object access. Audit
events record actor, effective user, tenant, action, resource, timestamp,
correlation ID, request outcome, and reason where applicable.

### Impersonation

Impersonation is an optional high-risk capability, not a normal login feature.
If approved, require Super Admin authorization, a reason, explicit banner and
exit control, a short-lived scoped token, no credential access, no privilege
escalation, and immutable start/action/end audit events that identify both the
admin and impersonated user. Add tests proving the impersonated session cannot
exceed the target user's permissions.

## Workspace and tenant management

For multi-tenant SaaS, provide controlled views for active organizations,
membership, subscription tier, quotas, storage limits, and feature flags.
Tenant overrides must be scoped, auditable, reversible where possible, and
subject to billing and data-retention policy. Never let a client-supplied
tenant ID bypass the authenticated administrative scope.

Feature toggles such as AI scoring and advanced reporting need an owner,
default, rollout scope, kill switch, migration impact, and rollback behavior.
Do not claim a toggle changes backend authorization unless the API enforces it.

## System configuration and integrations

Settings may include SMTP/provider configuration, templates, localization,
currency, timezone, date formats, webhook endpoints, and API keys. Store
secrets through an approved secret manager or deployment environment; never
return raw secrets after creation or store plaintext credentials in
`system_settings`.

API keys must be displayed once, hashed at rest, scoped, expirable,
revocable, rate-limited, and audited. Webhooks require signed payload
verification, replay protection, idempotency, bounded retries, and visible
failure/recovery state. Provider accounts, sender reputation, DNS, OAuth
applications, and delivery evidence remain `unverified` until configured and
exercised.

## Audit and security monitoring

Treat the activity ledger as append-only from the application perspective.
Capture destructive changes, role changes, exports, imports, settings changes,
session revocation, impersonation, authentication failures, and security
events. Support bounded pagination, filtering, sorting, retention, export
authorization, and access review.

Authentication logs may include IP address and approximate geolocation only
when privacy policy, retention, regional requirements, and data minimization
are approved. Do not silently add tracking or claim compromise detection from
logging alone.

## Data operations

Imports require an approved source inventory, field mapping, normalization,
duplicate policy, safe sample, reversible dry run, row-level validation,
reconciliation report, rejected-row review, cutover plan, and sign-off.
Dispatch large or destructive work asynchronously and return `202 Accepted`
with an execution ID and status resource. Persist input metadata, actor,
tenant, progress, attempts, errors, idempotency key, and recovery state.

Exports and full backups require authorization, rate limits, scope
confirmation, encrypted delivery, expiry, audit events, and deletion policy.
Soft-delete recovery must distinguish restore from permanent deletion, require
confirmation or approval for irreversible actions, and preserve audit history.
Fabricated seed data is not migration or backup evidence.

## Data model baseline

Add only approved tables and tenant relationships. A starting point is:

| Entity | Representative fields |
|---|---|
| `roles` | `id`, `name`, `description`, timestamps |
| `role_permissions` | `role_id`, resource, action, scope |
| `audit_logs` | actor/effective user, tenant, action, entity, changes JSONB, IP, timestamp |
| `api_keys` | tenant, hashed key, scopes, expiry, active state, last-used timestamp |
| `system_settings` | scoped key, typed value reference, updater, timestamps |
| `admin_jobs` | execution ID, kind, status, progress, attempts, errors, idempotency key |

Use foreign keys, tenant-aware indexes, appropriate JSONB/GiN indexes only
after query evidence, retention controls, and migration tests. Indexes on
audit entity and timestamp may support common queries, but do not assume
performance without representative measurements.

## API contract

Admin routes should be versioned under `/api/v1/admin/` and use explicit
dependencies such as `verify_admin_permission` or
`verify_super_admin`. Every collection supports bounded pagination, filtering,
sorting, rate limits, authorization tests, tenant tests, audit events, and
visible error responses.

```text
GET   /api/v1/admin/users
POST  /api/v1/admin/users/invite
PATCH /api/v1/admin/users/{id}/role
POST  /api/v1/admin/users/{id}/impersonate
GET   /api/v1/admin/audit-logs
POST  /api/v1/admin/sessions/revoke-all
POST  /api/v1/admin/data/import
GET   /api/v1/admin/jobs/{execution_id}
```

Invitation, import, export, backup, session revocation, and other heavy or
destructive actions may enqueue a durable job and return `202 Accepted`.
The API must not report success before the job outcome is known. Missing
provider or queue configuration must produce an explicit failure, not a
success-shaped fallback.

## Frontend route and interaction structure

Use an isolated route group while sharing the authenticated shell:

```text
frontend/src/app/
├── (crm)/                  # Standard CRM workspace
└── (admin)/
    ├── layout.tsx          # Admin navigation and permission-aware shell
    ├── dashboard/
    ├── users/
    ├── audit-logs/
    ├── settings/
    └── data-operations/
```

Use server-side TanStack Table pagination, sorting, and filtering for large
user and audit datasets. Use React Hook Form and Zod for settings forms, and
React Query mutations with explicit invalidation and error handling. Dense
analytical layouts may use destructive-action warning cues, but visual cues
never replace authorization or confirmation.

Every admin route and module must implement loading, empty, error, retry,
partial-failure, timeout/offline where relevant, and permission-denied states.
Keyboard access, focus management, accessible names, responsive behavior,
long-running job progress, and safe confirmation flows require actual browser
and accessibility evidence.

## Verification and release gate

Test positive and negative RBAC, tenant isolation, impersonation boundaries,
audit immutability, session revocation, API-key hashing and scopes, import
validation/idempotency, export authorization, job retries/dead letters,
soft-delete recovery, and destructive-action confirmation. Verify audit query
performance with representative data rather than assuming an index is enough.

Do not describe the Admin Panel as secure, compliant, production-ready,
migrated, backed up, or integrated without executed evidence. External
credentials, cloud resources, provider webhooks, production PostgreSQL/Redis,
secret rotation, monitoring, restore drills, legal review, and penetration
testing remain separately tracked capability states.
