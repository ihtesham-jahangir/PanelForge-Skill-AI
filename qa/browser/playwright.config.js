import { defineConfig, devices } from "@playwright/test";

export default defineConfig({
  testDir: "./tests",
  workers: 1,
  reporter: [["list"], ["html", { outputFolder: "artifacts/report", open: "never" }]],
  use: {
    baseURL: "http://127.0.0.1:4175",
    trace: "retain-on-failure",
    screenshot: "only-on-failure",
  },
  webServer: {
    command:
      "PANELFORGE_DB=/tmp/panelforge-playwright.sqlite3 PANELFORGE_SESSION_SECRET=playwright-test-secret PANELFORGE_RATE_LIMIT_MAX=500 python3 -c \"import sys; sys.path.insert(0, '../../reference-app'); import server; server.run(port=4175)\"",
    url: "http://127.0.0.1:4175/api/health",
    reuseExistingServer: false,
    timeout: 30_000,
  },
  projects: [
    { name: "desktop", use: { ...devices["Desktop Chrome"] } },
    { name: "mobile", use: { ...devices["Pixel 7"] } },
  ],
});
