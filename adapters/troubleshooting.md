# Troubleshooting

- **Skill not discovered:** verify the native filename, metadata, scope, and restart/reload requirements.
- **Module not loaded:** check relative paths from `SKILL.md` and load the module explicitly.
- **Third-party tool unavailable:** use the PanelForge fallback module and report the limitation.
- **Conflicting advice:** apply the priority order in [`orchestration/compatibility.md`](../orchestration/compatibility.md).
- **Unexpected changes:** inspect Git status and restore only changes explicitly authorized by the user.
