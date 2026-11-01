# Optional browser QA

This suite uses Playwright to verify the reference application in desktop and
mobile projects. It checks page titles, landmarks, navigation, console errors,
accessible control names, and horizontal overflow.
It also verifies keyboard access to the main content and permission feedback for
restricted member actions.

Run it from this directory after installing dependencies:

```bash
npm install
npx playwright install chromium
npm test
```

The installed `axe-core` integration checks the overview for automated
accessibility violations. Lighthouse can be run while the reference server is
already running:

```bash
npm run lighthouse
```

The Lighthouse wrapper reuses the Playwright-managed Chromium binary through
`CHROME_PATH`, so it does not require a separate system Chrome installation.

The GitHub Actions workflow is manual-only at
[`../../.github/workflows/browser-qa.yml`](../../.github/workflows/browser-qa.yml)
because browser binaries are intentionally not installed by the default
documentation/API validation workflow.
