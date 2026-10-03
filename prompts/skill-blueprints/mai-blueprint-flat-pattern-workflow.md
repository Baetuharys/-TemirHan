---
id: mai-blueprint-flat-pattern-workflow
title: Flat Pattern Workflow
type: blueprint
status: draft
version: 1.0.0
summary: From a bent sheet-metal model to a verified flat pattern and DXF with consistent K-factor/bend-table, relief and bend lines.
tags: [sheet-metal, engineering]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary, mai-module-sheet-metal-domain, mai-module-manufacturing-chain]
last_reviewed: 2026-10-02
input_contract: model/drawing, material, thickness, radii, bend method, process
output_contract: findings table, expected flat dimensions, open items
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Flat Pattern Workflow

## Scope
From a bent sheet-metal model to a trustworthy flat pattern and DXF. Covers flatten checks, K-factor/bend table consistency, relief, bend lines, bounding box.

## Required inputs
Model or drawing, material and thickness, inside radii, bend method (K-factor / bend table / allowance), cutting process, sheet format.

## Workflow
1. Confirm material, thickness, radii, and the bend method used by the **shop**, not only by CAD.
2. Flatten and check for errors (overlaps, failed bends, missing relief, closed corners).
3. Check feature-to-bend distances (see `knowledge/01`, `knowledge/02`).
4. Compute the expected flat length by hand for one or two bends as a sanity check (`knowledge/02`).
5. Verify bounding box against the sheet format and nesting.
6. Prepare bend lines on a separate layer; decide marking geometry.
7. Record method and revision in the drawing note; export DXF; open and inspect.
8. Recommend a test bend before series release.

## Required checks
- K-factor or bend table source recorded.
- Units mm, scale 1:1.
- Bend lines are not cut lines.
- Hole/slot distortion near bends considered.

## Output format
Findings table (item · status · note) · expected flat dimensions · open items.

## Test cases
1. No K-factor given → asks for source; offers labelled estimate range.
2. Hole 3 mm from a 2 mm-thick bend → flagged as risk with distance rule.
3. DXF with bend lines on the cut layer → flagged as Error.
