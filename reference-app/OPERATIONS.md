# Operations Runbook

## Deploy

```bash
export PANELFORGE_SESSION_SECRET="$(python3 -c 'import secrets; print(secrets.token_urlsafe(48))')"
docker compose -f reference-app/docker-compose.yml up -d --build
```

The compose file binds the service to localhost, runs as a non-root user, uses a read-only container filesystem, and requires an explicit production secret.

## Health and logs

```bash
curl --fail http://127.0.0.1:4173/api/health
docker compose -f reference-app/docker-compose.yml logs --follow
```

Put a TLS reverse proxy and access controls in front of the service before exposing it beyond localhost.

## Authorized security scan

From an authorized test environment with OWASP ZAP installed:

```bash
python3 scripts/run_zap_baseline.py https://authorized-test.example --authorized
```

The wrapper refuses non-HTTP targets, requires an explicit authorization flag,
and does not install ZAP or select a target automatically.

## Backup and restore

Stop writes or use a maintenance window, then create a consistent backup:

```bash
python3 scripts/backup_reference_db.py /var/lib/panelforge/reference.sqlite3 backups/reference.sqlite3
```

Restore only after confirming the target and backup paths:

```bash
python3 scripts/backup_reference_db.py /var/lib/panelforge/reference.sqlite3 backups/reference.sqlite3 --restore
```

Verify the restored file with the API smoke and authorization tests before resuming traffic. Keep encrypted, access-controlled copies according to the retention policy.

Run the non-destructive local integrity drill before changing a deployment:

```bash
python3 scripts/run_operations_drill.py
```

The drill uses a temporary SQLite database, verifies backup creation, mutates the database, restores it, and checks that the original state is recovered.

## Rollback

1. Stop the service and record the deployed image/configuration.
2. Restore the last known-good image or source revision.
3. Restore the database only if the release changed data incompatibly; otherwise preserve forward-compatible data.
4. Start the service, run health, authentication, authorization, tenant-isolation, and audit checks.
5. Monitor errors and latency before reopening traffic.

This runbook is a procedure and has not been executed against a remote deployment in this environment.
