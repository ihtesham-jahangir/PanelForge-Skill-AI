# Backend Engineering

For new web applications, use Python and FastAPI as a separate backend
application. Use Pydantic for request/response validation, SQLAlchemy 2.0 for
database access, Alembic for migrations, and PostgreSQL as the default
relational database. FastAPI must own business logic, authentication,
authorization, and persistence behind documented REST APIs.

Keep domain rules in application/domain services rather than controllers. Isolate external providers behind adapters, bound retries, make jobs idempotent, propagate correlation IDs, and log security-relevant outcomes without secrets or sensitive payloads. Define timeouts, failure handling, dead-letter/manual recovery, and health signals for every integration.
