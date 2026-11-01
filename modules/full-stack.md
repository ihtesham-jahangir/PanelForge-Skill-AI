# Full-Stack Engineering

## Default generated stack

New websites and web applications use this stack unless the user explicitly
requests an override:

```text
project/
├── frontend/                 # Next.js, React, TypeScript, Tailwind CSS
├── backend/                  # Python, FastAPI, Pydantic, SQLAlchemy 2.0, Alembic
├── database/                 # PostgreSQL integration and operational notes
├── docker-compose.yml
├── .env.example
└── README.md
```

Use [`templates/full-stack-blueprint.md`](../templates/full-stack-blueprint.md)
as the implementation and verification checklist for this architecture.

Keep frontend and backend as separate applications. The frontend communicates
with FastAPI through documented REST APIs. FastAPI owns business logic,
authentication, authorization, validation, and all database operations.
PostgreSQL is the default relational database. Use responsive, reusable,
accessible Tailwind components and generate executable code with tests,
security/error handling, and production-oriented configuration.

For existing projects, detect and preserve the current stack. Supported
patterns include Next.js/React/Vue/Angular, FastAPI/Django/NestJS/Express/Laravel,
PostgreSQL/MySQL/SQLite/MongoDB, and native ORM or query tooling. Do not force a
migration: inspect the project first and explain migration implications before
changing architecture.

For each feature define project structure, API contract, validation, authentication, authorization, transactions, error shape, logging, background jobs, external integrations, and tests. Keep domain rules out of presentation code and keep provider failures explicit. Use the repository's package manager and lockfile.
