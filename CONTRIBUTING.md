# Contributing

1. Branch from `main`; one topic per pull request.
2. Follow `docs/lifecycle.md` (Idea → Prompt → Module/Master → Blueprint → Skill → Adapter) and `docs/conventions.md`.
3. Add or update eval cases in `training/eval/cases.jsonl` for every new behaviour.
4. Run `python scripts/validate_all.py` — it must pass.
5. Update `CHANGELOG.md`. Use SemVer: patch = fixes, minor = new content, major = structure change.
6. No customer data. No invented UI labels, numbers or standards. Cite sources.
