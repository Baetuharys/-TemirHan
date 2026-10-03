---
id: mai-skill-solidworks-sheet-metal-workflow
title: SolidWorks Sheet Metal Workflow
type: skill
status: active
version: 1.0.0
summary: Guide a Turkish-UI SolidWorks sheet-metal workflow from model setup through flattening and drawing handoff.
tags: [solidworks, engineering, mechanical]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: solidworks-sheet-metal-workflow
description: Guide SolidWorks sheet-metal modelling, flattening and release in English or Turkish UI without inventing labels. Use for SolidWorks sac metal, Edge Flange, Base Flange, Flat-Pattern, bend table, gauge table.
---
# SolidWorks Sheet Metal Workflow

## Purpose
Guide a user through modelling, flattening and releasing a sheet-metal part in SolidWorks, in English or a Turkish interface, without inventing UI labels.

## Trigger
Guide SolidWorks sheet-metal modelling, flattening and release in English or Turkish UI without inventing labels. Use for SolidWorks sac metal, Edge Flange, Base Flange, Flat-Pattern, bend table, gauge table.

## Required inputs
SolidWorks version and UI language, part geometry or goal, material, thickness, bend method (K-factor/bend table/gauge table), downstream output (drawing, DXF, assembly).

## Operating rules
1. Extract the user's actual requirement before proposing a solution.
2. Distinguish supplied facts, calculated results, engineering-practice guidance, assumptions, and estimates.
3. Never invent missing dimensions, material properties, standards, machine capabilities, SolidWorks menu paths, API behavior, or process parameters.
4. Use consistent units and show the governing relationship when a calculation is performed.
5. When the result depends on a machine, tool, CAM system, material grade, SolidWorks version, or customer standard, identify that dependency.
6. If critical input is missing, either ask for it or proceed with a clearly labeled assumption when a useful preliminary result is still possible.
7. Finish with verification checks and a concise action summary.

## Workflow
1. Ask version and language once (`knowledge/04`).
2. Choose the start: Base Flange/Tab (native) or Convert to Sheet Metal (imported solid).
3. Set the `Sheet-Metal` parameters: thickness, default radius, bend method, auto-relief.
4. Add features in manufacturing-aware order (flanges → corners → hems → cuts → forming tools → hardware holes) (`knowledge/03`).
5. Flatten; diagnose errors using the error table in `knowledge/03`.
6. Set custom properties; create drawing (bent + flat views) and export DXF.
7. Give each step with the English command name and the Turkish label **only if level V/C**; otherwise `[doğrulanmadı]` plus how to find the command.

## Required checks
- Method (K-factor/table) matches the shop.
- Normal Cut used for cuts across bends where needed.
- DXF export options include/exclude bend lines deliberately.
- No invented menu path.

## Output contract
Numbered steps with the three layers (UI path · feature name · API name where relevant) and a verification step at the end.

## Failure modes
- Inventing Turkish menu labels or paths.
- Not asking the SolidWorks version.
- Using a K-factor different from the shop's without saying so.

## Knowledge to load
Paths are relative to the repository root.
- `knowledge/03-solidworks-sheet-metal.md`
- `knowledge/04-solidworks-turkish-ui-and-terminology.md`
- `reference/solidworks-ui-labels.csv` (V/C/U label levels)
- `reference/glossary-sacmetal.md`

## Self-test
1. User asks "Edge Flange'in Türkçe adı ne?" → English name + [doğrulanmadı] + how to search; asks for a screenshot.
2. Flatten fails → asks for the error text; lists likely causes in order.
3. User gives no version → asks version and language before steps.

See also: `workflows/default-workflow.md`, `examples/example.md`, `tests/smoke.md`.
