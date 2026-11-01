import { expect, test } from "@playwright/test";
import AxeBuilder from "@axe-core/playwright";

test("renders overview with accessible landmarks", async ({ page }) => {
  const consoleErrors = [];
  page.on("console", (message) => {
    if (message.type() === "error") consoleErrors.push(message.text());
  });

  await page.goto("/");
  await expect(page).toHaveTitle("Northstar Operations | PanelForge Reference");
  await expect(page.getByRole("main")).toBeVisible();
  await expect(page.getByRole("complementary", { name: "Primary navigation" })).toBeVisible();
  await expect(page.getByRole("link", { name: "Skip to content" })).toHaveAttribute("href", "#main-content");
  expect(consoleErrors).toEqual([]);
});

test("navigates through pipeline and keeps mobile content within viewport", async ({ page }) => {
  await page.goto("/");
  await page.getByRole("button", { name: "Pipeline", exact: true }).click();
  await expect(page.getByRole("region", { name: "Pipeline" })).toBeVisible();

  await page.setViewportSize({ width: 390, height: 844 });
  const overflow = await page.evaluate(
    () => document.documentElement.scrollWidth > document.documentElement.clientWidth,
  );
  expect(overflow).toBe(false);
});

test("renders named controls", async ({ page }) => {
  await page.goto("/");
  const unnamedButtons = await page.locator("button").evaluateAll((buttons) =>
    buttons.filter((button) => !button.textContent?.trim() && !button.getAttribute("aria-label")).length,
  );
  expect(unnamedButtons).toBe(0);
});

test("supports keyboard navigation to the primary content", async ({ page }) => {
  await page.goto("/");
  await page.keyboard.press("Tab");
  await expect(page.getByRole("link", { name: "Skip to content" })).toBeFocused();
  await page.keyboard.press("Enter");
  await expect(page.locator("#main-content")).toBeFocused();
});

test("shows permission feedback for member-only restricted actions", async ({ page }) => {
  await page.goto("/");
  const roleSelect = page.locator("#role-select");
  if (await roleSelect.isVisible()) {
    await roleSelect.selectOption("member");
  } else {
    await roleSelect.evaluate((select) => {
      select.value = "member";
      select.dispatchEvent(new Event("change", { bubbles: true }));
    });
  }
  await page.getByRole("button", { name: "Pipeline", exact: true }).click();
  await page.getByRole("button", { name: "New deal" }).click();
  await expect(page.getByRole("status")).toContainText("Permission denied");
});

test("has no automated accessibility violations on the overview", async ({ page }) => {
  await page.goto("/");
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toEqual([]);
});
