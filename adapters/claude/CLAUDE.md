# CLAUDE.md — Mechanical AI Engineering v3

Provider-neutral mechanical-engineering AI library focused on sheet metal, SolidWorks, enclosures, drawings/GD&T, Image→CAD, manufacturing and engineering documentation.

## Commands
```bash
python scripts/mai.py validate
python scripts/mai.py search "query"
python scripts/mai.py calc bend --t 2 --r 2 --angle 90 --k .40
python scripts/mai.py rebuild
python scripts/build_release.py
```

## Layout
`knowledge/` engineering knowledge · `sources/` provenance · `skills/` task contracts · `agents/` orchestration · `project-profiles/` real shop data · `design_patterns/` reusable concepts · `engineering_core/` evidence/data model · `tools/` deterministic calculations · `engines/` executable engines · `rag/` retrieval · `training/` prompt/data/eval · `adapters/` provider mapping · `dist/` generated packages.

## Change rules
1. Do not fabricate dimensions, tolerances, K/BD, machine capability, material properties, costs, standards, UI labels, API members or test results.
2. Shop/project data in `project-profiles/` outranks generic practice.
3. New behavior → eval case. New deterministic math → code test. New current fact → source registry/provenance.
4. IP/IK, certification, FEA and production approval remain evidence/test claims, not language-model claims.
5. Turkish SolidWorks UI labels remain unverified until checked on a real installation/version.
6. Image-derived geometry is estimated until calibrated/verified.
7. No customer data in `training/`.
8. Keep VERSION/CHANGELOG/README in sync.
