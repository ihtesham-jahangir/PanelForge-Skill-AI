import { spawn } from "node:child_process";
import { chromium } from "playwright";

const lighthouse = spawn(
  process.platform === "win32" ? "npx.cmd" : "npx",
  [
    "lighthouse",
    "http://127.0.0.1:4175/",
    "--output=json",
    "--output-path=artifacts/lighthouse.json",
    "--chrome-flags=--headless",
  ],
  {
    stdio: "inherit",
    env: { ...process.env, CHROME_PATH: chromium.executablePath() },
  },
);

lighthouse.on("exit", (code) => process.exit(code ?? 1));
