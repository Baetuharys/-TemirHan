---
id: mai-blueprint-solidworks-sheet-metal-workflow
title: SolidWorks Sheet Metal Workflow
type: blueprint
status: draft
version: 1.0.0
summary: Guide SolidWorks sheet-metal modelling, flattening and release without inventing UI labels.
tags: [solidworks, engineering]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary, mai-module-solidworks-turkish-ui]
last_reviewed: 2026-10-02
input_contract: SolidWorks version and language, goal, material, thickness, bend method
output_contract: numbered steps with UI path, feature name, API name and a verification step
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# SolidWorks Sheet-Metal Workflow

## Scope
Guide a user through modelling, flattening and releasing a sheet-metal part in SolidWorks, in English or a Turkish interface, without inventing UI labels.

## Required inputs
SolidWorks version and UI language, part geometry or goal, material, thickness, bend method (K-factor/bend table/gauge table), downstream output (drawing, DXF, assembly).

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

## Output format
Numbered steps with the three layers (UI path · feature name · API name where relevant) and a verification step at the end.

## Test cases
1. User asks "Edge Flange'in Türkçe adı ne?" → English name + [doğrulanmadı] + how to search; asks for a screenshot.
2. Flatten fails → asks for the error text; lists likely causes in order.
3. User gives no version → asks version and language before steps.
