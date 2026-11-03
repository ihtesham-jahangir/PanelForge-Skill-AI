# Database and Multi-Tenancy

Use foreign keys, constraints, normalized relationships, purposeful indexes, migrations, transaction boundaries, soft-delete semantics, audit history, retention, backup, and recovery policies. Common entities include users, organizations, memberships, roles, permissions, notifications, audit logs, leads, contacts, companies, deals, pipelines, activities, tasks, subscriptions, transactions, and support tickets; do not create all of them by default.

For tenant-aware data, derive tenant context from authenticated server state, validate it on every read/write, include tenant-aware unique constraints and indexes, and test cross-tenant access explicitly. Consider database row-level security where it fits the deployment. Never trust a client-provided tenant ID.

Separate schema scaffolding, Alembic migrations, seed data, production
provisioning, backup/restore evidence, retention/deletion policy, and migration
cutover as distinct deliverables. Real-data migration requires an approved
mapping, reversible dry run, reconciliation, duplicate strategy, rollback
point, and sign-off; fabricated seed records are not migration evidence.

For customer portals, model ownership and visibility explicitly for documents,
invoices, subscriptions, transactions, and support tickets. Test that
cross-tenant and cross-user reads, writes, downloads, counts, searches, and
error responses do not disclose data. Treat PostgreSQL RLS as defense in depth;
application authorization and tests remain required.
