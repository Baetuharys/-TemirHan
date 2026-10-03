---
id: mai-module-enclosure-ip-design
title: Enclosure and IP Design
type: module
status: active
version: 0.2.0
summary: Design reasoning for sheet-metal enclosures aimed at a target IP rating.
tags: [enclosure, ip-rating, sheet-metal]
depends_on: []
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Enclosure and IP Design

## Purpose
Reason about sheet-metal cabinets/enclosures against a target IP code. Reference: `reference/ip-codes.md`.

## Behavior
- Ask for the **target IP code**, environment (indoor/outdoor, washdown, dust, temperature swing), mounting (wall, floor, pole), and what goes inside (heat load, cable count).
- State clearly: a design can *target* an IP rating; the rating is confirmed by test (IEC 60529). Never write "this design is IP65" as a fact.
- Walk through every opening: door seam, cut-outs, cable entries, vents/fans, hinges, locks, mounting holes through the wall.
- For each opening, name the sealing method (gasket, gland, sealed plate, closed weld, sealant) and who owns it (design vs purchased part rating).
- Keep thermal and condensation notes separate from the IP rating; a vent or fan changes the rating.
- Do not equate NEMA types with IP codes.

## Output expectation
A table: opening | risk | sealing method | open question. Then assumptions.
