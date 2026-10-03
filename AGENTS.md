# AGENTS.md — Mechanical AI Engineering v3

For any coding/AI agent working in this repository:

1. Read `CLAUDE.md` and `docs/ARCHITECTURE.md`.
2. Treat `knowledge/`, `sources/`, `skills/`, `engineering_core/`, `tools/` and `engines/` as source-of-truth; `dist/` is generated.
3. Never invent production values, standard clauses, Turkish SolidWorks labels or execution/test results.
4. New behavior needs an eval; deterministic equations need tests; source-sensitive facts need provenance.
5. Never add customer/confidential data to training seeds.
6. Run `python scripts/validate_all.py` before finishing; for a release run `python scripts/build_release.py`.
