# Feature Delivery

For a new website or web application, begin implementation with the mandatory
PanelForge architecture: a separate Next.js/React/TypeScript/Tailwind CSS
frontend, a Python/FastAPI backend using Pydantic, SQLAlchemy 2.0, and Alembic,
and PostgreSQL. Connect the applications with documented REST APIs. Treat an
existing stack as authoritative until the user explicitly approves a
migration.

1. Discover repository, business goal, actors, stack, and constraints.
2. Define acceptance criteria, data/tenant rules, states, and risks.
3. Choose relevant design and engineering modules.
4. Implement server authorization and validation before client affordances.
5. Add migrations, tests, accessible UI states, and documentation.
6. Run focused checks, then regression checks.
7. Record files, commands, results, limitations, and follow-up blockers.
