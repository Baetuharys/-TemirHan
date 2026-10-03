---
id: mai-blueprint-sheet-metal-bend-analysis
title: Sheet-Metal Bend Analysis
type: blueprint
status: draft
version: 0.2.0
summary: Calculate bend allowance, deduction and flat length, and flag bends that may not be feasible.
tags: [sheet-metal, bending]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary, mai-module-sheet-metal-domain]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Sheet-Metal Bend Analysis

## Scope
One part or one bend at a time: flat length, bend allowance/deduction, feasibility flags.

## Required inputs
Material/grade, T, R (inside), bend angle, K-factor source, dimension convention (inside / outside / mid), tooling or shop bend table if available.

## Workflow
1. Confirm the dimension convention of every length that crosses a bend.
2. Take K from the supplied table; if none, state the assumed K and its source, and mark the result **Assumed**.
3. Compute `BA = theta(rad) x (R + K*T)`, `OSSB = (R+T) x tan(theta/2)`, `BD = 2*OSSB - BA`.
4. Sum the flat length; show each segment.
5. Flag: R below what the shop supports, holes/slots near the bend line, flange shorter than the die allows, bend sequence collisions.
6. Report the result with units and the single input that would change it most.

## Required checks
- Inside vs outside radius not mixed. - Angle in the right unit. - K-factor source stated. - No minimum-distance number quoted without a source.

## Output format
Table: segment | type | length | BA/BD | note. Then flags and open questions.

## Test cases
1. 2 mm steel, R 2, 90 deg, K from supplied table: expected result with each term shown.
2. Same part, no K supplied: model must state the assumption, not silently pick one.
3. Hole 3 mm from bend line: model must flag distortion risk and ask for the shop rule instead of inventing a limit.
