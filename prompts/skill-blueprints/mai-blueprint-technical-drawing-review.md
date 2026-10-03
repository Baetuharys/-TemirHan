---
id: mai-blueprint-technical-drawing-review
title: Technical Drawing Review
type: blueprint
status: draft
version: 0.2.0
summary: Review a drawing for views, dimensions, tolerances, notes, title block and revision data.
tags: [technical-drawing, documentation]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary, mai-module-engineering-terminology]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Technical Drawing Review

## Scope
Review of a 2D drawing (PDF or image) for completeness and consistency. Does not redesign the part.

## Required inputs
The drawing, the intended manufacturing method, the governing standard if any (see `reference/standards-map.md`), the part's function if known.

## Workflow
1. Title block: part number, name, material, thickness, revision, scale, sheet size, projection method, general-tolerance note (e.g. ISO 2768 class), finish, units.
2. Views: enough to define the shape; flat pattern view present for sheet-metal parts; section/detail views where needed.
3. Dimensions: each feature fully defined once, no duplicated or conflicting dimensions, no closed chains that over-define, bend dimensions' convention stated.
4. Tolerances: general tolerance stated; tight tolerances only where functional; GD&T frames reference declared datums.
5. Notes: bend radius, K-factor/bend table reference, deburring, finish, welding symbols, inspection requirements.
6. Sheet-metal specifics: bend lines marked with direction, angle and radius; bend count matches the flat view.
7. Classify findings: **Error** (wrong or missing, blocks manufacturing), **Risk** (ambiguous), **Suggestion**.

## Required checks
- Findings cite the exact place on the drawing. - No standard clause quoted without naming the standard and edition to verify. - Image-read values flagged as read-from-image.

## Output format
Findings table: # | location | class | finding | proposed fix.

## Test cases
1. Drawing with no general-tolerance note: flagged as Error or Risk with reason.
2. Flat pattern missing on a bent part: flagged.
3. Poorly legible scan: model must say which values it could not read instead of guessing.
