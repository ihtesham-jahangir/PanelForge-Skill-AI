# Database and Multi-Tenancy

Use foreign keys, constraints, normalized relationships, purposeful indexes, migrations, transaction boundaries, soft-delete semantics, audit history, retention, backup, and recovery policies. Common entities include users, organizations, memberships, roles, permissions, notifications, audit logs, leads, contacts, companies, deals, pipelines, activities, tasks, subscriptions, transactions, and support tickets; do not create all of them by default.

For tenant-aware data, derive tenant context from authenticated server state, validate it on every read/write, include tenant-aware unique constraints and indexes, and test cross-tenant access explicitly. Consider database row-level security where it fits the deployment. Never trust a client-provided tenant ID.
