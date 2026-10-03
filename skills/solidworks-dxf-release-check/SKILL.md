---
id: mai-skill-solidworks-dxf-release-check
title: SolidWorks DXF Release Check
type: skill
status: active
version: 0.3.0
summary: Review a SolidWorks sheet-metal DXF before laser/CAM release, including scale, geometry, cut/mark separation, and revision consistency.
tags: [solidworks, dxf, laser, release]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
input_contract: engineering context, design/manufacturing intent, available model/drawing/data, constraints
output_contract: structured result, assumptions, verification checklist, unresolved inputs, next action
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: solidworks-dxf-release-check
description: Check a SolidWorks flat-pattern DXF before release: export options, layers, units, bend lines, size vs model. Use for SolidWorks DXF çıkışı, açınım export kontrolü.
---
# SolidWorks DXF Release Check
## Trigger
Use before sending a SolidWorks-generated DXF to laser/CAM.

## Workflow
1. Confirm source configuration and flat pattern.
2. Confirm units and expected sheet thickness/material.
3. Check one-to-one correspondence between intended cut geometry and exported entities.
4. Check duplicate, open, self-intersecting, zero-length, construction, and hidden geometry where relevant to the CAM importer.
5. Check scale by comparing at least one known dimension after export/import.
6. Classify marking geometry separately from cutting geometry. A visible DXF entity is not automatically a marking instruction.
7. Confirm layer/color/entity conventions required by the actual laser/CAM software.
8. Re-open the exported file in the target CAM or a neutral DXF viewer when possible.
9. Record revision, filename convention, units, and source model/configuration.

## SolidWorks-specific rule
Do not claim a sketch without a Cut feature will be interpreted as marking. Export behavior and CAM interpretation are version- and workflow-dependent.

## Output
Return a pass/fail checklist with evidence, geometry exceptions, CAM-dependent items, and release recommendation.

## Knowledge to load
Paths are relative to the repository root.
- `knowledge/03-solidworks-sheet-metal.md`
- `knowledge/09-cad-engineering-practice.md`
