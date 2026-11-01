# Reference API Deployment Boundary

The standard-library server is suitable for local development and controlled smoke tests only. A production deployment must:

1. Set `PANELFORGE_ENV=production` and a high-entropy `PANELFORGE_SESSION_SECRET`.
2. Run behind a maintained WSGI/ASGI server and TLS-terminating reverse proxy. The bundled container binds internally on `0.0.0.0`; Compose publishes it only on localhost by default.
3. Use managed SQLite only for suitable single-writer workloads, or replace it with a supported transactional database.
4. Configure backups, restore drills, retention, migrations, monitoring, alerting, and rollback.
5. Add an identity provider, MFA, secret rotation, CSRF strategy if cookies are introduced, and centralized rate limiting.
6. Restrict database file permissions and keep it outside public/static paths.
7. Execute the release checklist before serving real users.

The reference API now refuses non-development default secrets when `PANELFORGE_ENV=production`.

Container and operational procedures are provided in [`Dockerfile`](./Dockerfile), [`docker-compose.yml`](./docker-compose.yml), and [`OPERATIONS.md`](./OPERATIONS.md). They are configuration artifacts; remote deployment and restore drills still require authorized infrastructure.
