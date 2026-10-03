---
id: mai-knowledge-bom-revision-change-control
title: BOM, Revision, PDM and Engineering Change Control
category: engineering-governance
evidence: engineering-practice
last_reviewed: 2026-10-02
verify_before_release: [released CAD/drawing revision, BOM alignment, file references, change approvals, downstream exports]
maturity: implemented
source_ids: []
---

# BOM, Revision, PDM and Engineering Change Control

## One change affects many artifacts
Changing a hole, thickness or finish can affect part CAD, assembly, drawing, DXF, STEP, BOM, mass, cost, quotation, work instruction, inspection plan and stock. Release is a synchronized set, not one saved CAD file.

## Minimum item identity
Each manufactured/bought item should have a stable part number or identifier, description, revision/state, quantity/unit and make/buy classification. Avoid using filenames as the only identity system.

## Revision discipline
Distinguish work-in-progress from released data. Record why a revision changed and what downstream artifacts were regenerated. Do not silently overwrite an issued DXF or PDF with a new geometry under the same released identifier.

## PDM-safe automation
Macros/scripts that rename or move referenced SolidWorks files can break assemblies when used outside the approved PDM/rename workflow. Prefer reporting and controlled exports over bulk destructive changes.

## ECO/ECN checklist
Problem/reason → affected items → proposed change → technical review → cost/schedule impact → verification → approval → release → downstream notification/stock disposition.
