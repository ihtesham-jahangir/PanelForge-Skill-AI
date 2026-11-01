# Verification Matrix

| Area | Evidence required | Status |
|---|---|---|
| Functional behavior | Executed tests and acceptance results | VERIFIED locally — 15 repository tests and reference-app smoke coverage |
| Authorization | Positive and negative server-side tests | VERIFIED locally — API auth/RBAC tests |
| Tenant isolation | Cross-tenant access tests | VERIFIED locally — tenant-scoped API tests |
| Accessibility | Keyboard, semantic, contrast, and automated checks | VERIFIED locally — Playwright + axe-core, 12 desktop/mobile tests |
| Responsive UI | Mobile, tablet, desktop evidence | VERIFIED locally — browser responsive checks; tablet remains covered by layout rules, not a dedicated snapshot |
| Data integrity | Migration, constraints, transaction tests | VERIFIED locally — SQLite constraints and backup/restore drill |
| Performance | Measured budget and environment | VERIFIED locally — Lighthouse performance score 100 |
| Security | Threat model and authorized testing | PARTIAL — local security tests passed; ZAP requires an authorized target |
| Operations | Logging, monitoring, backup, rollback evidence | PARTIAL — local container/health and backup/restore verified; remote monitoring and rollback unavailable |
