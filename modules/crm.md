# Universal CRM Engineering

Build the CRM as a decoupled, multi-tenant B2B/B2C platform only when those
requirements are confirmed. It has three deliberately separated interfaces:
the sales/workspace panel, the admin panel, and the customer User Panel. It
manages leads, contacts, companies, sales opportunities, communications,
activities, support, billing, and reporting across the customer lifecycle.
Use the [capability-gap preflight](../quality/capability-gaps.md)
before inventing terminology, stages, roles, ownership, retention, billing, or
integration behavior.

## Architecture

For a new application, use the repository default:

- **Frontend:** Next.js App Router, React, TypeScript, Tailwind CSS, Zustand
  for client state, React Query for server-state synchronization, and React
  Hook Form with Zod validation.
- **Backend:** Python, asynchronous FastAPI REST endpoints, Pydantic schemas,
  SQLAlchemy 2.0 async ORM, Alembic migrations, and OAuth2-compatible bearer
  authentication with short-lived JWT access tokens and an explicit refresh
  and revocation policy.
- **Infrastructure:** PostgreSQL, Redis for explicitly bounded caching,
  sessions, rate limits, and coordination, Docker Compose for local services,
  and a documented reverse-proxy/TLS boundary.
- **Jobs and realtime:** use a durable worker system such as Celery only when
  its broker, retry, idempotency, dead-letter, and recovery operations are
  configured. Treat WebSockets and semantic caching as optional capabilities,
  not implied features.

Keep frontend and backend separate. FastAPI owns business logic,
authentication, authorization, validation, and database operations. Document
the REST contract under `/api/v1/`. Preserve an existing stack after
inspection; do not force this architecture onto an existing project.

## Core product modules

### Identity and access management

Implement login, registration only when required, token refresh/revocation,
password recovery, MFA policy, RBAC, tenant membership, and immutable audit
events. Suggested roles are Super Admin, Sales Manager, Sales Representative,
and Support Agent, but role names and powers require human confirmation.
Enforce permissions server-side for every object, export, bulk action, job, and
webhook. Never treat route protection or hidden UI controls as authorization.

### Leads and contacts

Support configured lead capture endpoints for landing pages and external forms,
contact profiles, company affiliation, communication history, social links,
ownership, and lead scoring. Scoring rules must be explicit and versioned;
labels such as Hot, Warm, and Cold are product decisions. Lead conversion must
record source lead, resulting contact/company/deal, actor, timestamp, and
conversion outcome.

### Pipeline and opportunities

Provide a board grouped by configured stages and safe stage transitions. A deal
may include expected value, probability, forecast category, expected close
date, owner, company, contact, lead, activities, and lost reason. Drag-and-drop
is a UI interaction; the API must validate the actor, source stage, target
stage, required fields, ownership, and audit event.

### Activities and communication

Model calls, emails, meetings, tasks, notes, reminders, and internal events as
an auditable timeline with explicit visibility. Do not claim email, SMS,
calendar, or voice delivery without configured provider adapters, credentials,
signed webhooks, idempotency, bounded retries, and observed delivery evidence.

### Analytics and reporting

Dashboard metrics must define their time zone, period, filters, ownership
scope, and calculation. Reports require permission-aware aggregates,
reproducible definitions, pagination, CSV/PDF export authorization, and
scheduled-report recovery behavior. “Real time” requires an exercised
invalidation or subscription design; polling or cached data must be labeled.

## Lifecycle and automation

Define lead qualification and conversion, contact/company relationships, deal
stage transitions, assignment and reassignment history, duplicate detection,
follow-up scheduling, activity history, and ownership boundaries. Every
transition specifies actor, allowed source states, validation, side effects,
notification behavior, and audit event.

Use `TRIGGER -> CONDITIONS -> ACTIONS`. Persist an execution ID, input
snapshot, attempt count, status, timestamps, and error details. Actions must be
idempotent, retried with bounded backoff where safe, dead-lettered when
necessary, and manually recoverable. Keep automation logs separate from
user-facing activity history when their audiences differ.

## Data model baseline

Use only confirmed entities and add tenant keys to every tenant-owned record.
The following is a starting point, not a complete schema:

| Entity | Representative fields |
|---|---|
| `users` | `id`, `email`, `password_hash`, `is_active`, timestamps |
| `organizations` | `id`, `name`, policy and lifecycle fields |
| `memberships` | `organization_id`, `user_id`, role and ownership scope |
| `companies` | `id`, `organization_id`, `name`, industry, website, revenue tier |
| `contacts` | `id`, `company_id`, names, email, phone, position |
| `leads` | `id`, `contact_id`, assigned user, status, source, score |
| `pipelines` and `stages` | tenant, ordering, transition and forecast rules |
| `opportunities` | company, lead, owner, value, stage, close date, lost reason |
| `activities` | opportunity/contact, actor, type, notes, timestamp, visibility |
| `audit_events` | actor, tenant, action, resource, correlation ID, outcome |

Use foreign keys, tenant-aware unique constraints and indexes, transactions,
soft-delete semantics where approved, retention controls, and audit history.
Derive tenant context from authenticated server state; never trust a
client-provided tenant ID. Schema scaffolding, Alembic migrations, seed data,
production provisioning, and real-data migration are separate deliverables.

## API contract

All routes except explicitly approved authentication and signed webhook
endpoints require a valid bearer token. Every collection supports bounded
pagination, filtering, sorting, authorization, ownership/tenant tests, audit
events, and explicit error responses.

```text
POST  /api/v1/auth/token
GET   /api/v1/users/me
GET   /api/v1/contacts?cursor=&limit=&company_id=
POST  /api/v1/leads
PATCH /api/v1/leads/{id}/status
GET   /api/v1/opportunities/board
PUT   /api/v1/opportunities/{id}/stage
```

Creating a lead may enqueue a notification only if the worker and provider
configuration exist; otherwise return a visible, actionable configuration
failure. Stage changes and conversions must be transactional with their audit
events or expose a documented consistency model.

## Suggested project structure

```text
backend/
├── app/
│   ├── api/v1/endpoints/       # auth, leads, contacts, opportunities
│   ├── core/                   # configuration and security
│   ├── crud/                   # query operations
│   ├── models/                # SQLAlchemy models
│   ├── schemas/               # Pydantic request/response models
│   ├── services/              # scoring, conversion, reporting, automation
│   ├── db/                    # sessions and Alembic integration
│   └── main.py
├── requirements.txt
├── Dockerfile
└── alembic.ini

frontend/
├── src/
│   ├── app/                   # auth, dashboard, pipeline, layout/providers
│   ├── components/            # reusable UI and CRM feature components
│   ├── lib/                   # API client and Zustand stores
│   ├── types/                 # API-aligned TypeScript types
│   └── middleware.ts          # UX route protection, never sole authorization
├── tailwind.config.ts
├── package.json
└── Dockerfile
```

## Deployment and operations

Local Compose may orchestrate frontend, FastAPI, PostgreSQL, Redis, and
workers, with Uvicorn reload and `alembic upgrade head` for development.
Production topology may use a managed frontend host and Dockerized backend
services behind Nginx or an equivalent proxy with TLS, health checks, bounded
worker concurrency, and process supervision. These are manifests and options,
not evidence that any provider, VPS, DNS, certificate, database, queue, or
secret manager exists.

Require strict CORS origins, Redis-backed rate limits only when Redis
availability and failure behavior are defined, Pydantic validation, parameter
binding through the ORM, and secrets outside source control. Add backups,
restore drills, migration rollback, logs, metrics, tracing, alerts, and
runbooks before claiming operational readiness.

## Verification gate

Verify unit, API, authorization, cross-tenant, audit, migration, worker,
browser, accessibility, responsive, performance, and failure-state behavior
with the project-native tools. Test loading, empty, partial failure, timeout,
retry, offline, and permission-denied states for every CRM route. Mark
provider integrations, cloud deployment, compliance, penetration testing,
backup/restore, localization, and real-data migration `unverified` until
executed in the relevant environment and reviewed by the responsible human.
