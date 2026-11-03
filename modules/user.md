# User Panel Engineering

The User Panel is the secure client portal in a three-interface CRM:

1. **Sales/workspace panel:** internal representatives manage leads, pipelines,
   communications, and activities.
2. **Admin panel:** authorized administrators manage IAM, tenants, settings,
   audit evidence, and data operations.
3. **User panel:** customers track interactions, submit support tickets, manage
   billing, and access permitted documents.

Use the shared Next.js frontend and FastAPI backend boundary, but enforce
client-portal authorization and ownership in FastAPI. A client must never infer
another user's identifiers, tenant metadata, documents, billing records, or
support tickets through IDs, counts, errors, search, exports, or timing.

## Lifecycle and capabilities

Define only the required flows for registration, invitation, verification,
password recovery, session revocation, email or MFA change, account deletion,
reactivation, billing, document access, and ticket submission. Sensitive
changes require explicit confirmation, recent authentication or step-up MFA
where approved, and immutable audit events.

Possible portal modules include dashboards, profiles, security, preferences,
notifications, invoices, subscriptions, transactions, documents, support
tickets, and activity history. Confirm which are in scope, what data is
customer-visible, and whether customer actions require staff approval.

## UI and API contract

Every portal screen provides actionable loading, empty, error, retry, timeout,
permission-denied, and success states. Forms use server-side validation in
addition to client validation; errors are specific, recoverable, and do not
reveal whether another account or resource exists.

Collections and document/ticket endpoints require bounded pagination,
filtering, rate limits, tenant ownership checks, audit events, and positive and
negative authorization tests. Account deletion, exports, billing changes, and
document downloads require explicit scope and confirmation. Never use UI route
guards as the sole security boundary.

## Verification

Test IDOR resistance, cross-tenant access, session invalidation, recovery and
MFA changes, billing/document ownership, ticket visibility, rate limiting,
accessible names and focus behavior, responsive layouts, and all failure
states. Mark payment providers, identity providers, email delivery, cloud
storage, legal retention, and production security evidence as unverified until
they are configured and exercised in the relevant environment.
