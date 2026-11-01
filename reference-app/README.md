# PanelForge Reference Application

This dependency-free application demonstrates a production-oriented admin/CRM surface:

- Responsive overview, pipeline, people, and audit activity views.
- Loading-free but explicit success and permission-denied feedback.
- Manager/member permission preview and tenant context.
- Accessible landmarks, labels, table captions, skip link, focus styles, and reduced-motion behavior.
- Data-dense enterprise visual language with semantic tokens and responsive layouts.
- A SQLite-backed API with signed sessions, server-side role checks, tenant filtering, and audit events.

## Run

From the repository root:

```bash
python3 reference-app/server.py
```

Open `http://127.0.0.1:4173`. See [`API.md`](./API.md) for demo credentials and endpoints.

This is a reference application, not a production system. The API demonstrates server-side controls, but production deployments still require hardened secrets, HTTPS, rate limiting, identity-provider integration, operational controls, and deployment verification.

See [`DEPLOYMENT.md`](./DEPLOYMENT.md) for the production boundary.
