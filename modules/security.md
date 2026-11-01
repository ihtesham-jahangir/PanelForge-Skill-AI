# Security Engineering

Threat-model authentication, authorization, sessions, passwords, MFA, SQL injection, XSS, CSRF, IDOR, SSRF, file uploads, APIs, rate limits, secrets, dependencies, audit logging, and privacy. Apply OWASP guidance relevant to the stack.

Sensitive operations require server-side authorization tests, safe validation, bounded resource use, and explicit error handling that does not leak secrets or internal state. Security testing must target owned or explicitly authorized systems; do not place destructive payloads in production. Add regression tests for every fixed authorization or tenant-isolation defect.
