# Quality Assurance

Use project-native runners first. Playwright is appropriate for browser and responsive flows; Vitest, pytest, or equivalent for unit/API behavior; axe-core for automated accessibility checks; Lighthouse for performance; and OWASP ZAP only against authorized test environments.

## Visual QA

Start the app, visit relevant routes, capture desktop/tablet/mobile states, exercise loading/error/empty/focus states, inspect console errors, run accessibility checks, fix issues, and repeat. Keep screenshots and reports tied to a commit or build identifier.

See [`production-readiness.md`](./production-readiness.md), [`release-checklist.md`](./release-checklist.md), and [`verification-matrix.md`](./verification-matrix.md).
