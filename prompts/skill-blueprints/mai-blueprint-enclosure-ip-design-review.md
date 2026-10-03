---
id: mai-blueprint-enclosure-ip-design-review
title: Enclosure IP Design Review
type: blueprint
status: draft
version: 0.2.0
summary: Review a sheet-metal enclosure design against a target IP code, opening by opening.
tags: [enclosure, ip-rating, sheet-metal]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary, mai-module-enclosure-ip-design, mai-module-sheet-metal-domain]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Enclosure IP Design Review

## Scope
Design review of a sheet-metal cabinet against a target IP code. Output is design risk, not certification.

## Required inputs
Target IP code, environment, mounting, door/seam description or model/drawing, list of cut-outs and cable entries, purchased parts' own ratings (glands, switches, fans).

## Workflow
1. Restate the target and what each digit demands (`reference/ip-codes.md`).
2. List every opening and seam. For each: sealing method, owner (design / purchased part), risk.
3. Check the weakest element: the rating of the whole enclosure is limited by its weakest opening.
4. Check door seal: gasket type, compression stop, overlap or labyrinth, hinge side, lock pull-in.
5. Check weld/seam closure, drain/vent decisions, and how they change the rating.
6. List test or evidence needed (lab test, supplier certificates) and what the design can and cannot claim.

## Required checks
- Never states a rating as achieved. - Every opening listed. - Purchased parts' ratings taken from supplied data, not assumed.

## Output format
Table: opening | risk | sealing method | owner | open question. Then verdict wording that stays at "targets".

## Test cases
1. IP65 target with a vent fan: model must flag that the fan rating limits the enclosure.
2. Stitch-welded seam in an IPx5 target: model must flag.
3. User asks "is this IP66?": model must answer in terms of design intent and required test.
