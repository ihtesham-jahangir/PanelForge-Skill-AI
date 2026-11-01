# Architecture Standards

## Default application boundary

For a newly generated website or web application, use separate applications:
`frontend/` with Next.js, React, TypeScript, and Tailwind CSS; `backend/` with
Python, FastAPI, Pydantic, SQLAlchemy 2.0, and Alembic; and PostgreSQL as the
default relational database. Connect the frontend to FastAPI through documented
REST APIs. FastAPI owns business logic, authentication, authorization,
validation, and database operations.

For an existing project, inspect and preserve its architecture first. Explain
migration implications before changing its stack, and change technologies only
after an explicit user override.

Prefer the existing project's boundaries and idioms. Define responsibilities for presentation, application/use-case logic, domain rules, persistence, integrations, and background work. Keep external providers behind interfaces where replacement or testing is likely.

Every new API or command should specify input validation, authentication, authorization, transaction boundaries, error shape, logging, idempotency, and tests. Avoid speculative abstractions and avoid coupling UI components directly to persistence.
