# Agent Compatibility Matrix

| Agent | Native entry convention | Installation status | Notes |
|---|---|---|---|
| Claude Code | Project or user skill/customization directory | Not verified in this environment | Follow current vendor documentation |
| OpenAI Codex | Project instruction/skill configuration | Not verified in this environment | Use `SKILL.md` as portable source |
| Cursor | Project rules or agent configuration | Not verified in this environment | Adapt progressive-loading links |
| Windsurf | Project rules/skills configuration | Not verified in this environment | Do not assume Claude-compatible paths |
| GitHub Copilot | Repository or user custom instructions/skills | Not verified in this environment | Verify supported file names and scopes |
| Generic agents | Read `SKILL.md` directly | Portable fallback | Manually load relevant modules; hooks are optional |

Hooks are optional and only apply to agents that support the documented workspace hook format. The skill remains usable without them.

This matrix intentionally reports verification status rather than inventing installation paths.
