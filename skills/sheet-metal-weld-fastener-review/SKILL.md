---
id: mai-skill-sheet-metal-weld-fastener-review
title: Sheet Metal Weld and Fastener Review
type: skill
status: active
version: 0.3.0
summary: Review welds, studs, PEM-style fasteners, screws, nuts, and assembly interfaces on sheet-metal designs and drawings.
tags: [sheet-metal, welding, fasteners, assembly]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
input_contract: engineering context, design/manufacturing intent, available model/drawing/data, constraints
output_contract: structured result, assumptions, verification checklist, unresolved inputs, next action
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: sheet-metal-weld-fastener-review
description: Review welds, self-clinching fasteners (PEM-type), rivets and screws on sheet-metal parts: access, distortion, datasheet limits, finish interaction. Use for kaynak, çakma somun, saplama, perçin incelemesi.
---
# Sheet Metal Weld and Fastener Review
## Workflow
1. Identify joint function: structural, locating, sealing, grounding, cosmetic, or temporary.
2. Identify joining method: weld, spot weld, stud, PEM-type fastener, screw/nut, rivet, adhesive, or other specified method.
3. Check accessibility, tool clearance, bend/flange interference, heat distortion risk, and sequence implications.
4. For welds, verify the drawing communicates weld type, size/length or extent where required, side/location, intermittent pattern where applicable, and all-around/field indicators only when actually intended.
5. For studs/fasteners, verify thread/diameter, length, material/finish if specified, insertion direction, edge distance, and mating-part clearance.
6. Check whether the joint information exists in the 3D model, drawing, BOM, or manufacturing note; do not assume one source contains everything.
7. Flag missing standards, customer specifications, or supplier-specific fastener constraints.

## Important distinction
A symbol or CAD feature represents design intent; it does not by itself prove the manufacturing process is feasible.

## Output
Return joint list, issue list, drawing-note requirements, manufacturing risks, and unresolved specifications.

## Knowledge to load
Paths are relative to the repository root.
- `knowledge/14-welding-fasteners-finishing.md`
- `knowledge/01-sheet-metal-fundamentals.md`
