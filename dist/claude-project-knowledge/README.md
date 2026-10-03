# Source & Provenance Registry

This directory is the **source-of-truth for external provenance**. Knowledge files may summarize engineering principles, but release-critical claims must resolve to an entry in `registry.json` or to a project-specific source supplied by the user/fabricator.

## Rules

1. Do not store purchased ISO/IEC/ASME standard text in this repository.
2. Store only public metadata, official landing-page links, edition/status notes, and the internal claim-to-source mapping.
3. A source being listed does **not** mean every statement in a knowledge file has been clause-checked.
4. Project contracts, customer specifications, local regulations, and fabricator capability sheets override generic guidance where applicable.
5. Before a production release, run `python scripts/validate_sources.py` and re-check any entry flagged as `under-publication`, `to-be-revised`, `pending-replacement`, or software-version-specific.
6. For supplier values (density, gasket compression, coating cure, fastener torque, etc.), create a project source record rather than turning the value into a universal constant.

## Evidence labels

- `SUPPLIED` — explicitly provided by user/project data.
- `CALCULATED` — deterministic calculation from stated inputs.
- `SOURCE-BACKED` — traceable to a named source record.
- `PRACTICE` — engineering practice/heuristic; shop verification needed.
- `ASSUMED` — explicit temporary assumption.
- `ESTIMATED` — inferred/approximate value with uncertainty.
- `UNKNOWN` — unresolved; do not silently fill it.

The registry deliberately separates **provenance** from **authority**. A source can be real but still not be the governing source for a specific project.
