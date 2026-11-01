const views = [...document.querySelectorAll(".view")];
const navItems = [...document.querySelectorAll(".nav-item")];
const statusMessage = document.querySelector("#status-message");
const roleSelect = document.querySelector("#role-select");

function showStatus(message) {
  statusMessage.textContent = message;
  window.setTimeout(() => {
    if (statusMessage.textContent === message) statusMessage.textContent = "";
  }, 3500);
}

function showView(name) {
  views.forEach((view) => view.classList.toggle("hidden", view.id !== `view-${name}`));
  navItems.forEach((item) => item.classList.toggle("is-active", item.dataset.view === name));
  const heading = document.querySelector(`#view-${name} h2`);
  if (heading) heading.focus({ preventScroll: true });
}

navItems.forEach((item) => item.addEventListener("click", () => showView(item.dataset.view)));
document.querySelectorAll("[data-view-link]").forEach((item) => item.addEventListener("click", () => showView(item.dataset.viewLink)));
document.querySelector("#export-button").addEventListener("click", () => showStatus("Report export queued for the Northstar Labs tenant."));
document.querySelector("#notifications-button").addEventListener("click", () => showStatus("3 notifications: 1 overdue follow-up, 1 approval, 1 sync completed."));
document.querySelector("#new-deal-button").addEventListener("click", () => {
  if (roleSelect.value !== "manager") {
    showStatus("Permission denied: only managers can create deals.");
    return;
  }
  showStatus("New deal flow opened. Server-side authorization is required in production.");
});
document.querySelector("#invite-button").addEventListener("click", () => {
  if (roleSelect.value !== "manager") {
    showStatus("Permission denied: only managers can invite members.");
    return;
  }
  showStatus("Invitation flow opened for the Northstar Labs tenant.");
});
roleSelect.addEventListener("change", () => showStatus(`Preview role changed to ${roleSelect.options[roleSelect.selectedIndex].text}.`));
