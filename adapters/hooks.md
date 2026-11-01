# Validation Hook

The workspace includes `.github/hooks/panelforge-validation.json`, which runs the dependency-free documentation validator at `SessionStart`. It is intentionally non-destructive: it reads hook input, validates local files, and returns a structured message. It does not install packages, access the network, edit files, or delete data.

If the hook blocks session startup, run:

```bash
python3 tests/validate_docs.py
```

Fix the reported local link, JSON, or customization metadata issue, then retry. Remove or disable the workspace hook only when the consuming agent does not support hooks.
