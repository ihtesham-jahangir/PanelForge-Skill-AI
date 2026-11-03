# Security Engineering

Threat-model authentication, authorization, sessions, passwords, MFA, SQL injection, XSS, CSRF, IDOR, SSRF, file uploads, APIs, rate limits, secrets, dependencies, audit logging, and privacy. Apply OWASP guidance relevant to the stack.

Sensitive operations require server-side authorization tests, safe validation, bounded resource use, and explicit error handling that does not leak secrets or internal state. Security testing must target owned or explicitly authorized systems; do not place destructive payloads in production. Add regression tests for every fixed authorization or tenant-isolation defect.

Generated integration configuration must name required environment variables
and fail visibly when they are absent. Require signed webhook verification,
replay protection, idempotency, bounded retries, and explicit recovery state.
Do not claim compliance, production security, penetration testing, secret
rotation, or abuse resistance without scoped evidence and human/security
review.

Customer portals require explicit IDOR regression tests across every
user-visible resource, including documents, invoices, subscriptions,
transactions, and tickets. Account recovery, email/MFA changes, billing
changes, exports, and deletion require re-authentication or step-up controls
when approved by policy, plus audit events and non-enumerating error behavior.
