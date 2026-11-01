# Reference API

Start the application API and static UI from the repository root:

```bash
python3 reference-app/server.py
```

Demo credentials use the password `demo-password`:

- `maya@northstar.example` — manager, Northstar Labs
- `jon@northstar.example` — member, Northstar Labs
- `other@example.test` — manager, Other Tenant

## Endpoints

- `POST /api/login` — returns a short-lived signed bearer token.
- `GET /api/session` — returns the authenticated user and tenant.
- `GET /api/deals` — returns only deals for the authenticated tenant.
- `POST /api/deals` — manager-only, validates name/value/stage, and writes an audit event.
- `GET /api/members` — returns only members of the authenticated tenant.
- `POST /api/invitations` — manager-only, validates email, and records an audit event.
- `GET /api/audit` — returns only audit events for the authenticated tenant.
- `GET /api/health` — unauthenticated health check.

This is a reference implementation. Production deployments must replace the demo secret, use secure secret management, add HTTPS, rate limiting, CSRF strategy where cookies are used, operational logging, and a real identity provider.
