# Installation

## GitHub Copilot workspace skill

From this repository, install into another project with:

```bash
python3 scripts/install_skill.py /path/to/target-project
```

Preview the destination without writing:

```bash
python3 scripts/install_skill.py /path/to/target-project --dry-run
```

The installer creates `.github/skills/panelforge-ai/` and refuses to replace an existing directory unless `--force` is supplied. It replaces only that named skill directory.

The installer copies the native skill entry and its local reference files. It does not install third-party tools, modify user-level settings, access credentials, or change the target project's source code.

## Other agents

Use the native location documented by the target agent and copy the root `SKILL.md` plus relevant modules. Verify discovery with a small, non-destructive task. Uninstallation is the reverse of the project-local copy or link; do not remove user-level files without explicit authorization.
