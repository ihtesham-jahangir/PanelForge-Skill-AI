---
description: "Analyze a panel, portal, CRM, or SaaS request and produce implementation-ready requirements"
name: "PanelForge Discovery"
argument-hint: "Describe the product or feature to analyze"
agent: "agent"
---

Analyze the requested product or feature using the PanelForge standards in [`SKILL.md`](../../SKILL.md).

Return:
1. Actors, business goals, and primary workflows.
2. Required screens, states, APIs, and data entities.
3. Authentication, authorization, ownership, and tenant rules.
4. Accessibility, responsive, performance, and security constraints.
5. Explicit acceptance criteria and a focused verification plan.
6. Open decisions and assumptions.
7. Stack decision: for a new web application, record the mandatory
   Next.js/React/TypeScript/Tailwind CSS frontend, Python/FastAPI/Pydantic/
   SQLAlchemy 2.0/Alembic backend, PostgreSQL database, separate application
   boundary, and documented REST API. For an existing application, record the
   current stack and migration implications instead.

Do not implement code in this prompt. Do not ask the user to choose a
framework. Do not invent existing-project conventions before inspecting the
target repository.
