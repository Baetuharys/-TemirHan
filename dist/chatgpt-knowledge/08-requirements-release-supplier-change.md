# Compact Knowledge Bundle — 08-requirements-release-supplier-change.md


---

## SOURCE FILE: `knowledge/21-requirements-risk-and-release.md`

---
id: mai-knowledge-requirements-risk-release
title: Requirements, Risk and Engineering Release
category: engineering-governance
evidence: practice
last_reviewed: 2026-10-02
verify_before_release: [requirements baseline, unresolved assumptions, verification plan, revision state]
maturity: implemented
source_ids: []
---

# Requirements, Risk and Engineering Release

## 1. Requirement record
A useful requirement is identifiable, testable and tied to a source. Record: ID, statement, source/customer, priority, verification method, status and affected parts.

Bad: “make it strong.”  Better: “door shall not permanently deform under the project-defined service load; verify by agreed test/analysis.” The actual load must come from the project, not the AI.

## 2. Lightweight design-risk review
For each important requirement capture:
- failure mode;
- effect;
- likely causes;
- current prevention/detection;
- proposed action;
- owner/status.

The repository does not prescribe a universal risk score because company FMEA schemes differ. Use the organization’s method when one exists.

## 3. Assumption register
Every `ASSUMED`, `ESTIMATED` or `UNKNOWN` release-relevant item goes into an assumption register. Each row needs an owner and a closure action. “AI said so” is not closure evidence.

## 4. Release gates
A production release should confirm at minimum:
- material/thickness/finish;
- interfaces and critical dimensions;
- bend model/tooling source where flat size depends on it;
- weld/fastener definition;
- drawing standard and revision;
- DXF layer/entity review;
- ingress/thermal claims phrased correctly;
- unresolved deviations approved;
- BOM and quotation assumptions aligned with the released design.

## 5. Change control
When a design changes, identify affected CAD, drawings, DXF, BOM, cost, quotation, test plan and documentation. A revision is not complete when only the `.SLDPRT` changed.


---

## SOURCE FILE: `knowledge/27-bom-revision-pdm-and-change-control.md`

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


---

## SOURCE FILE: `knowledge/28-supplier-fabricator-rfq-and-handoff.md`

---
id: mai-knowledge-supplier-fabricator-handoff
title: Supplier/Fabricator RFQ and Manufacturing Handoff
category: procurement-manufacturing
evidence: engineering-practice
last_reviewed: 2026-10-02
verify_before_release: [revision package, quantities, materials, finishes, tolerances, commercial assumptions, supplier capability]
maturity: implemented
source_ids: []
---

# Supplier/Fabricator RFQ and Manufacturing Handoff

## A good handoff removes ambiguity
Send enough information for the supplier to quote and build the same intent you reviewed. Typical package: RFQ/quantity, drawing PDF, neutral CAD if appropriate, flat DXF for laser parts, BOM, material/finish specification, critical tolerances, weld/assembly notes and revision manifest.

## Ask the fabricator for real process data
For repeat work capture their preferred bend radii/tooling, validated bend deductions or bend table, minimum feature preferences, stocked material sizes, hardware installation capability, finish constraints, weld process and inspection capability. Put these in `project-profiles/` so the AI stops guessing.

## Quote clarification log
Resolve substitutions, excluded operations, tooling/NRE, minimum order quantities, packaging, test/certification, shipping terms and lead-time assumptions before comparing prices. Cheapest line price is not necessarily the lowest delivered project cost.

## Pre-production review
For new or high-risk parts review critical bends, inaccessible fasteners, weld distortion, coating masks, gasket lands, flat-pattern responsibility, revision and inspection points with the supplier before volume production.
