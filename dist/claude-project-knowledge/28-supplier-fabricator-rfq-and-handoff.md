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
