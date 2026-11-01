# Admin Panel Engineering

Model dashboard, analytics, users, roles, permissions, organizations, content, subscriptions, billing, settings, audit logs, notifications, reports, and monitoring according to the actual business.

## Permission model

Use explicit permissions such as `users.read`, `users.create`, `users.update`, `users.delete`, `roles.read`, `roles.create`, `roles.update`, `roles.assign`, `analytics.read`, and `reports.export`. Enforce authorization on every server-side operation, including exports, bulk actions, background jobs, and direct object access.

Document role hierarchy, resource-level rules, sensitive-action confirmation, session re-authentication where needed, and immutable audit events containing actor, tenant, action, resource, timestamp, request correlation ID, and outcome. UI permission hiding is an optimization, never a security boundary.
