# Full-Stack Project Blueprint

Use this blueprint when creating a new website or web application. Do not
replace these defaults unless the user explicitly requests another stack.

## Required architecture

- [ ] `frontend/` is a separate Next.js application using React, TypeScript,
  and Tailwind CSS.
- [ ] `backend/` is a separate Python application using FastAPI.
- [ ] Backend validation uses Pydantic.
- [ ] Database access uses SQLAlchemy 2.0.
- [ ] Schema changes use Alembic migrations.
- [ ] PostgreSQL is the default relational database.
- [ ] `frontend/` communicates with `backend/` through documented REST APIs.
- [ ] Business logic, authentication, authorization, and database operations
  remain in `backend/`.

## Expected project files

```text
project/
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/api/
│   ├── package.json
│   ├── tsconfig.json
│   └── tailwind.config.ts
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── services/
│   ├── alembic/
│   │   └── env.py
│   ├── pyproject.toml
│   └── tests/
├── database/
│   └── README.md
├── docker-compose.yml
├── .env.example
└── README.md
```

## API contract

- [ ] Every endpoint documents method, path, actor, authorization, request
  schema, response schema, error shape, and status codes.
- [ ] Authentication and authorization are enforced in FastAPI.
- [ ] Tenant and resource ownership are checked server-side.
- [ ] CORS, CSRF/session or token handling, rate limits, and security headers
  are configured for the deployment model.
- [ ] OpenAPI output is reviewed and the frontend client uses typed responses.

## Database and operations

- [ ] PostgreSQL connection settings come from environment variables.
- [ ] SQLAlchemy sessions have explicit transaction boundaries.
- [ ] Alembic migrations support upgrade and documented rollback strategy.
- [ ] Foreign keys, unique constraints, tenant keys, and indexes are defined.
- [ ] Secrets are excluded from source control and logs.
- [ ] Health checks, structured errors, backups, and restore evidence are
  documented before production release.

## Verification

- [ ] Backend unit and API authorization tests pass.
- [ ] Frontend type-check, lint, and component tests pass.
- [ ] Tenant-isolation tests cover direct object access and bulk operations.
- [ ] Browser checks cover keyboard access, responsive behavior, loading,
  empty, error, and permission states.
- [ ] Docker Compose starts the separate services and PostgreSQL health check.
- [ ] Delivery report separates verified, partial, unverified, and blocked work.
