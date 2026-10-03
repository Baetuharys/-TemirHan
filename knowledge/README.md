# Knowledge Index

Human-readable engineering knowledge for people and AI retrieval. Every numbered file carries front matter including evidence, review date, maturity, source IDs and release-verification needs. **Project/shop data overrides generic practice.**

| # | File | Topic |
|---:|---|---|
| 01 | `01-sheet-metal-fundamentals.md` | Sheet-metal fundamentals, cutting and DFM |
| 02 | `02-bending-and-flat-pattern.md` | Bend allowance/deduction, K-factor, flat pattern, press brake |
| 03 | `03-solidworks-sheet-metal.md` | SolidWorks sheet-metal workflow and DXF |
| 04 | `04-solidworks-turkish-ui-and-terminology.md` | Turkish UI terminology and verification levels |
| 05 | `05-enclosures-ip-ik.md` | Cabinets/enclosures, IP/IK, leakage paths |
| 06 | `06-technical-drawing.md` | Technical drawing and production drawing review |
| 07 | `07-gdt-and-tolerancing.md` | GD&T, datums and general tolerancing |
| 08 | `08-image-dimension-estimation.md` | Image-based dimensional estimation and uncertainty |
| 09 | `09-cad-engineering-practice.md` | CAD intent, file formats, release hygiene |
| 10 | `10-engineering-documentation.md` | Technical documentation patterns |
| 11 | `11-quotation-and-commercial.md` | RFQ/quotation structure and commercial assumptions |
| 12 | `12-cost-analysis.md` | Manufacturing cost model and margin/markup |
| 13 | `13-solidworks-macros-api.md` | Safe SolidWorks macro/API generation |
| 14 | `14-welding-fasteners-finishing.md` | Welding, fasteners and finishing basics |
| 15 | `15-materials-reference.md` | Material/density/weight reference |
| 16 | `16-design-troubleshooting-and-decision-support.md` | Recovering a stuck design and comparing concepts |
| 17 | `17-tolerance-stack-and-fits.md` | 1-D tolerance stack and fit reasoning |
| 18 | `18-enclosure-thermal-management.md` | Enclosure heat and first-pass airflow reasoning |
| 19 | `19-manufacturing-process-selection-and-dfma.md` | Process selection and DFMA |
| 20 | `20-image-to-cad-geometry-reconstruction.md` | Image→geometry→DXF reconstruction model |
| 21 | `21-requirements-risk-and-release.md` | Requirements, risk, assumptions and release gate |
| 22 | `22-structural-stiffness-and-load-paths.md` | Sheet-metal stiffness, reinforcement and load paths |
| 23 | `23-joints-fasteners-hinges-and-hardware.md` | Joints, hinges, latches and hardware selection |
| 24 | `24-sealing-gaskets-and-ingress-details.md` | Gasket path/compression and ingress details |
| 25 | `25-corrosion-finishing-and-material-compatibility.md` | Corrosion, coatings and material compatibility |
| 26 | `26-metrology-inspection-and-quality-planning.md` | Measurement, FAI/inspection and flexible parts |
| 27 | `27-bom-revision-pdm-and-change-control.md` | BOM, revision, PDM and change control |
| 28 | `28-supplier-fabricator-rfq-and-handoff.md` | Fabricator/RFQ package and capability feedback |
| 29 | `29-electrical-enclosure-layout-and-serviceability.md` | Mechanical packaging/serviceability of electrical enclosures |
| 30 | `30-engineering-sanity-checks-and-calculation-discipline.md` | Units, assumptions, model limits and sanity checks |

## Related assets
- `reference/`: quick cards, glossary and UI tables.
- `sources/`: official-source metadata and lifecycle status.
- `design_patterns/`: reusable concept cards, never certification claims.
- `project-profiles/`: real shop/project capability; highest-value customization layer.
- `tools/`: deterministic calculations.
- `skills/`: workflows that decide how to use this knowledge.

## Editing rules
1. Keep front matter current; update `last_reviewed` after a real review.
2. Deterministic numbers belong in code/tests rather than prose memory.
3. Name standard/software source and edition/status; do not paste copyrighted standard text.
4. Add project-specific manufacturing values to `project-profiles/`, not universal knowledge.
5. Run `python scripts/validate_all.py` and rebuild RAG/exports after changes.
