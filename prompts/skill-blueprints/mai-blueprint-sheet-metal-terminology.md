---
id: mai-blueprint-sheet-metal-terminology
title: Sheet-Metal Terminology
type: blueprint
status: draft
version: 1.0.0
summary: Translate and explain sheet-metal and CAD terms between English and Turkish using a fixed term-selection policy and a glossary.
tags: [terminology, sheet-metal, solidworks, turkish-ui]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
input_contract: term(s) or text to translate/explain, audience (shop floor, drawing, documentation, SolidWorks UI), language direction
output_contract: term table with preferred Turkish term, alternatives and notes; UI labels only at level V/C
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Sheet-Metal Terminology

## Scope
EN-TR sheet-metal, CAD, GD&T, finishing and commercial terminology, applying `docs/terminology-policy.md`: UI label > standard term > established shop term > Öztürkçe word in real use > coined word only as a marked suggestion.

## Required inputs
term(s) or text to translate/explain, audience (shop floor, drawing, documentation, SolidWorks UI), language direction

## Workflow
1. Identify the audience and where the text will be used (UI step, drawing note, shop instruction, document prose).
2. Look the term up in `reference/glossary.csv`; for UI labels use `reference/solidworks-ui-labels.csv` and its level (V/C/U).
3. Apply the policy order; show the established term first and an Öztürkçe alternative in brackets once if it is in real use.
4. Flag ambiguities (punta vs nokta kaynağı; markup vs margin; açınım vs gelişim).
5. If a term is missing, say so, propose a candidate marked `öneri`, and offer to add it to the glossary.
6. Never present a Turkish SolidWorks label as verified without level V.

## Required checks
- Every UI label has a level (V/C/U).
- Coined words are marked `öneri`.
- Ambiguous pairs are disambiguated.

## Output format
Table: EN · TR preferred · alternatives · where to use · note.

## Test cases
1. Bend deduction in Turkish → bükme düşümü / bükme kesintisi; context-dependent; no UI claim.
2. Turkish menu name of Edge Flange → level U: English name, [doğrulanmadı], how to find it.
3. Are punta kaynağı and nokta kaynağı the same → no; tack weld vs resistance spot weld.
