---
description: "Review a panel, portal, CRM, or SaaS change for authorization, tenant isolation, accessibility, and release risks"
name: "PanelForge Security and QA Review"
argument-hint: "Describe the change or select the files to review"
agent: "agent"
---

Review the requested change using [`modules/security.md`](../../modules/security.md), [`modules/database.md`](../../modules/database.md), and [`quality/verification-matrix.md`](../../quality/verification-matrix.md).

Return a severity-ranked table with:
- Finding and confidence.
- File and line when available.
- Exploit or failure condition.
- Minimal remediation.
- Regression test needed.

Also list verified checks, unverified checks, and release blockers. Review only systems and data the user is authorized to test. Do not claim tests passed unless you execute them.
