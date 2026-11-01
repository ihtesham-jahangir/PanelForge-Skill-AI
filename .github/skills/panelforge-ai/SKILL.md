---
name: panelforge-ai
description: 'Design and engineer production-oriented admin panels, user portals, CRM applications, and SaaS management systems. Use for dashboard architecture, design systems, RBAC, multi-tenancy, CRM workflows, security, accessibility, QA, or production readiness.'
argument-hint: 'Describe the panel, portal, CRM, or SaaS feature to design or implement.'
user-invocable: true
disable-model-invocation: false
---

# PanelForge AI

Use this skill for production-oriented admin panels, user portals, CRM applications, and SaaS management systems.

## Procedure

1. Inspect the target repository, stack, existing patterns, tests, and current changes.
2. Convert the request into business workflows, acceptance criteria, ownership rules, and measurable verification.
3. Load the relevant PanelForge module from the repository root:
   - `core/` for discovery, requirements, architecture, and delivery.
   - `design-engine/` and `modules/ui-ux.md` for visual and interaction work.
   - `modules/admin.md`, `modules/user.md`, or `modules/crm.md` for product domains.
   - `modules/full-stack.md`, `modules/database.md`, and `modules/security.md` for implementation.
   - `quality/` for verification and release decisions.
4. Preserve the existing stack and design tokens; do not force a migration.
5. Enforce authorization and tenant ownership server-side. UI hiding is not security.
6. Implement focused changes, including directly related tests and documentation.
7. Run the narrowest meaningful validation command and report actual evidence.

The canonical expanded documentation is [`../../../SKILL.md`](../../../SKILL.md). External specialists are optional; follow [`../../../orchestration/README.md`](../../../orchestration/README.md) and never fabricate availability.
