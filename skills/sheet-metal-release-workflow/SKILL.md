---
id: mai-skill-sheet-metal-release-workflow
title: Sheet Metal Manufacturing Release Workflow
type: skill
status: active
version: 0.3.0
summary: End-to-end release from SolidWorks sheet-metal model through drawing, DXF, laser marking, bending, welding, assembly, cost, and documentation.
tags: [sheet-metal, solidworks, release, manufacturing]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
input_contract: engineering context, design/manufacturing intent, available model/drawing/data, constraints
output_contract: structured result, assumptions, verification checklist, unresolved inputs, next action
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: sheet-metal-release-workflow
description: Gate a sheet-metal part for release: model, drawing, flat pattern, DXF, BOM and revision consistency. Use for üretime çıkış, release kontrolü, revizyon tutarlılığı.
---
# Sheet Metal Manufacturing Release Workflow
## Trigger
Use when a sheet-metal part or enclosure must move from design intent to a controlled manufacturing release.

## Workflow
1. Intake: identify part/assembly, revision, material/grade, thickness, finish, quantity, manufacturing route, customer requirements, and required outputs.
2. Model audit: confirm sheet-metal definition, material, thickness, bend features, reliefs, suppression/configuration state, and manufacturability assumptions.
3. Flat-pattern audit: verify flat pattern exists, bend directions are coherent, no self-intersections or unintended overlaps exist, and the developed size is plausible.
4. Drawing audit: verify views, dimensions, tolerances, material/thickness, revision, weld/fastener notes, and manufacturing-critical characteristics.
5. DXF release: export only the intended flat pattern geometry; preserve units/scale and separate cut/mark intent according to the receiving CAM convention.
6. Production-process review: map cut/mark → bend → weld/fastener → finish → assembly. Check that each operation has sufficient information.
7. Cost handoff: collect material area/weight, cut length or machine time if available, marking, bend count, weld/assembly effort, finish, quantity, and scrap assumptions.
8. Documentation: generate release notes, inspection criteria, and revision record without inventing unavailable values.
9. Final gate: every released artifact must reference the same part identity and revision.

## Release gates
- Model, drawing, DXF, and documentation agree on part identity and revision.
- Manufacturing intent is explicit; CAD visibility is not treated as proof of a production process.
- Missing machine/CAM/tool/customer data are flagged rather than guessed.
- Any calculated dimension or cost has inputs and assumptions recorded.

## Output
Return: release status, artifact checklist, detected risks, unresolved inputs, verification evidence, and next action.

## Knowledge to load
Paths are relative to the repository root.
- `knowledge/06-technical-drawing.md`
- `knowledge/09-cad-engineering-practice.md`
- `knowledge/03-solidworks-sheet-metal.md`
