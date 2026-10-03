# Claude Adapter — v3.0

## Ways to use
| Mode | Files | Best for |
|---|---|---|
| Compact Project | `dist/claude-project-compact/` | Upload-limited/everyday chat |
| Full Project | `dist/claude-project-knowledge/` | Broader project knowledge when capacity permits |
| Skills | `dist/claude-skills/*.zip` | Task-specific loading where supported |
| Code/agent repo | `adapters/claude/CLAUDE.md` + full repo | Editing, validation and executable tools |

Use `training/system-prompts/claude-project-instructions.md` as the behavioral instruction.

## Loading order
Task intake → one relevant skill → named knowledge/project-profile files → deterministic tool/source retrieval if needed → verification/release gate.

## Important
Runtime features and upload limits change; check the current product interface rather than relying on a fixed number in this repo. Never claim a tool/CAD/test action occurred unless a real runtime performed it.

## Rebuild
```bash
python scripts/export_chatgpt.py
python scripts/export_claude_skills.py
```
