# Specialist Environment Verification

Verification date: 2026-11-01. Workspace browser-QA packages and Chromium were installed; no user-level agent hooks or external agent skills were installed.

## Local results

| Capability | Result |
|---|---|
| Workspace-local GitHub Copilot skill | PRESENT at `.github/skills/panelforge-ai/` |
| Node.js | PRESENT — `/home/ihtesham-jahangir/.nvm/versions/node/v24.22.2/bin/node` |
| npm | PRESENT — version 11.19.1 |
| Python | PRESENT — version 3.14.4 |
| Docker | PRESENT — version 29.9.2 |
| Playwright CLI | PRESENT at `qa/browser/node_modules/.bin/playwright` |
| Lighthouse CLI | PRESENT at `qa/browser/node_modules/.bin/lighthouse` |
| OWASP ZAP CLI | ABSENT |
| Common user-level Claude/Codex/Cursor/Windsurf skill paths | ABSENT |
| Integrated browser QA | PASS — rendered UI, navigation, responsive resize, landmarks, accessible names, and horizontal-overflow checks |
| Playwright + axe-core suite | PASS — 12 desktop/mobile tests, including automated accessibility checks |
| Lighthouse | PASS — performance 100, accessibility 100, best practices 96, SEO 100 |

Run the reproducible check with:

```bash
python3 scripts/verify_specialists.py
```

Run the external-agent inventory without installing anything:

```bash
python3 scripts/verify_agent_runtimes.py
```

Run ZAP only from an authorized environment with an installed ZAP executable:

```bash
python3 scripts/run_zap_baseline.py https://authorized-test.example --authorized
```

## Official source verification

- [UI UX Pro Max repository](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill): official repository inspected; it advertises Python 3.x and an `ui-ux-pro-max-cli` npm package. No installation was performed.
- [gstack repository](https://github.com/garrytan/gstack): official README and install documentation inspected. It documents Claude Code, Git, Bun 1.4.2+, optional Node.js on Windows, and a setup script. No clone or setup was performed.
- [Playwright installation](https://playwright.dev/docs/intro): official docs inspected; workspace package and Chromium installed and executed.
- [Storybook installation](https://storybook.js.org/docs/get-started/install): official docs inspected; the Storybook CLI installs into a project and current requirements include Node.js 20+ and npm 10+. No install was performed.
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview): official docs inspected; workspace package executed using the Playwright-managed Chromium binary.
- [OWASP ZAP](https://www.zaproxy.org/): official site inspected; ZAP is an open-source web application scanner. No install or scan was performed.
- [axe-core repository](https://github.com/dequelabs/axe-core): official repository inspected; package/license references were visible. No install or scan was performed.

## Interpretation

The PanelForge fallback modules and adapters are available locally. External agent availability is not claimed based on documentation alone. Agent-skill installation remains opt-in because it may register hooks or modify user configuration.

## Browser QA evidence

The integrated browser served the reference app locally and verified:

- Overview and Pipeline navigation render successfully.
- Desktop and 390px responsive layouts have no horizontal overflow.
- `main`, primary navigation, and skip-link landmarks are present.
- All rendered images have alternative text and all buttons have accessible names.

The workspace contains an opt-in Playwright/axe-core/Lighthouse suite, and its local execution has passed. The default validation workflow does not download browser binaries; the manual workflow reproduces the full suite.
