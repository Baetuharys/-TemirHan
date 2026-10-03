---
id: mai-skill-laser-dxf-marking-workflow
title: Laser DXF and Marking Workflow
type: skill
status: active
version: 0.2.0
summary: Prepare and review sheet-metal DXF workflows where cutting and marking geometry must remain distinct.
tags: [laser, dxf, marking, sheet-metal]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-sheet-metal-domain, mai-module-manufacturing-chain]
last_reviewed: 2026-10-02
input_contract: part geometry, manufacturing intent, cutting/marking requirements, CAD/SolidWorks workflow, machine constraints if known
output_contract: workflow, geometry classification, process mapping requirements, verification checklist
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: laser-dxf-marking-workflow
description: Prepare laser DXF with separated cut, marking/engraving and bend layers (stud positions, part IDs). Use for lazer kesim DXF, işaretleme, gravür, saplama konumu.
---
# Laser DXF and Marking Workflow
## Trigger
Use for laser-cut DXF, engraving/marking geometry, or geometry that must appear in DXF without being cut.
## Workflow
1. Classify geometry as CUT, MARK, REFERENCE, or OTHER.
2. Determine how the receiving laser/CAM distinguishes processes: layers, colors, entities, or machine convention.
3. Never assume a sketch entity is automatically a marking instruction.
4. For SolidWorks, give export/layer guidance only when supported by version or supplied evidence.
5. Check duplicates, scale, units, and separation of process geometry.
6. Require final confirmation in the actual CAM/laser software before production.
## Critical rule
DXF visibility alone does not prove cutting versus marking; the receiving CAM workflow determines process interpretation.

## Knowledge to load
Paths are relative to the repository root.
- `knowledge/03-solidworks-sheet-metal.md`
- `knowledge/01-sheet-metal-fundamentals.md`
- `knowledge/09-cad-engineering-practice.md`
