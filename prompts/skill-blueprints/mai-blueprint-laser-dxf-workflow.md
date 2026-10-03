---
id: mai-blueprint-laser-dxf-workflow
title: Laser DXF Workflow
type: blueprint
status: draft
version: 1.0.0
summary: Prepare a clean laser-cutting DXF with separated cut, marking and bend layers.
tags: [manufacturing, engineering]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary, mai-module-manufacturing-chain]
last_reviewed: 2026-10-02
input_contract: flat pattern, material, thickness, shop DXF rules, marking needs
output_contract: DXF checklist, layer table, open questions
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Laser DXF Workflow

## Scope
Prepare a DXF for laser cutting (and optional marking/engraving) from a sheet-metal model without separating mistakes into the shop.

## Required inputs
Flat pattern or sketch, material, thickness, machine/CAM requirements, marking requirements (studs, text, bend lines), quantity.

## Workflow
1. Confirm the shop's DXF requirements (units, version, layer names, line types, tolerance for closing contours).
2. Put geometry on separate layers: CUT, MARK/ENGRAVE, BEND (not cut), NOTES.
3. Check contours: closed, no duplicates, no zero-length segments, splines converted if the CAM requires, minimum feature sizes (`knowledge/01`).
4. Check the kerf and web between parts if nesting is done by the user.
5. Check marking features (stud positions, part ID) and their depth/process separation.
6. Export; re-open in a viewer; compare overall size with the model.
7. Name the file with part number + revision; keep the drawing revision identical.

## Required checks
- Bend lines are never on the cut layer.
- Units mm, scale 1:1, origin defined.
- No hidden/duplicate entities.
- Marking is not confused with cutting.

## Output format
DXF checklist (item · pass/fail) · layer table · open questions for the shop.

## Test cases
1. Stud-position marks mixed with cut layer → separated into MARK.
2. Splines in the outline → flagged if the shop CAM needs polylines.
3. DXF size differs from model bounding box → flagged as Error.
