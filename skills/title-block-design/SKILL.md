---
id: mai-skill-title-block-design
title: Sheet Metal Technical Drawing Title Block Design
type: skill
status: active
version: 0.3.0
summary: Design and review a concise technical drawing title block for sheet-metal parts, with revision and manufacturing information.
tags: [technical-drawing, title-block, sheet-metal, solidworks]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
input_contract: engineering context, design/manufacturing intent, available model/drawing/data, constraints
output_contract: structured result, assumptions, verification checklist, unresolved inputs, next action
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: title-block-design
description: Design a drawing title block (antet) with release fields, revision table, tolerance and finish notes for sheet-metal drawings in SolidWorks. Use for antet tasarımı, çizim şablonu, revizyon tablosu.
---
# Sheet Metal Technical Drawing Title Block Design
## Design goals
Keep the title block compact while preserving the information needed to identify, manufacture, inspect, and revise a sheet-metal part.

## Recommended information groups
- Part identity: part number and/or part name according to the company convention.
- Assembly context: parent/main assembly identifier when needed.
- Material and thickness.
- Finish/coating when applicable.
- Revision number and revision date.
- Drawing scale, sheet size, units, projection method, and drawing number where used by the company system.
- Description area with enough space for manufacturing-critical notes.
- Approval/checking fields only if part of the company process.

## SolidWorks review points
1. Use linked custom properties where the value should follow the model automatically.
2. Do not assume a property exists under a universal Turkish label; verify the actual SolidWorks version/template/property mapping.
3. Keep text hierarchy readable; enlarge description and revision information before decorative fields.
4. Adjust border-zone numbering and line weights consistently with the drawing template standard.
5. Ensure revision table and title block cannot contradict each other.

## Output
Return field list, property-link strategy, layout recommendations, and template verification checklist.

## Knowledge to load
Paths are relative to the repository root.
- `knowledge/06-technical-drawing.md`
- `knowledge/09-cad-engineering-practice.md`
