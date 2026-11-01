# Architecture Standards

Prefer the existing project's boundaries and idioms. Define responsibilities for presentation, application/use-case logic, domain rules, persistence, integrations, and background work. Keep external providers behind interfaces where replacement or testing is likely.

Every new API or command should specify input validation, authentication, authorization, transaction boundaries, error shape, logging, idempotency, and tests. Avoid speculative abstractions and avoid coupling UI components directly to persistence.
