---
id: mai-blueprint-sheet-metal-manufacturability-check
title: Sheet Metal Manufacturability Check
type: blueprint
status: draft
version: 1.0.0
summary: Design-for-manufacturing review of a sheet-metal part, with Error/Risk/Suggestion findings per process step.
tags: [sheet-metal, engineering]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary, mai-module-sheet-metal-domain, mai-module-manufacturing-chain]
last_reviewed: 2026-10-02
input_contract: model/drawing, material, thickness, quantity, process
output_contract: findings table with location, class, fix and cost effect
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Sheet-Metal Manufacturability Check

## Scope
Design-for-manufacturing review of a sheet-metal part or assembly before release or quotation. Finds features the shop will reject, re-quote or struggle with.

## Required inputs
Model/drawing, material and thickness, quantity, process (laser/punch/bend/weld/finish), tolerance class, shop capability data if available.

## Workflow
1. Cutting: min hole/slot, web, corner radii, edge distances, nesting friendliness.
2. Forming: radius vs tooling, flange length, hole-to-bend, relief, bend sequence and collisions, springback, grain direction.
3. Joining: weld access and distortion, hardware datasheet limits, galvanised/stainless considerations.
4. Finishing: coating thickness vs fits, masking, hanging marks, drain holes.
5. Assembly/inspection: tolerance stack, datum accessibility.
6. Cost drivers: extra setups, special tools, secondary operations.
7. Classify each finding as **Error / Risk / Suggestion**, cite location, give a fix.

## Required checks
- Rules of thumb are labelled *typical*; shop values override.
- No finding without a location.
- The first process that could reject the part is named.

## Output format
Findings table: # · location · class · finding · proposed fix · cost/time effect.

## Test cases
1. 3 mm thick part with 8 mm flange → Error: flange shorter than tooling minimum (typical).
2. Slot 2 mm from a bend → Risk with distance rule.
3. Request without material → asks material and thickness before judging.
