---
id: mai-skill-sheet-metal-terminology
title: Sheet-Metal Terminology
type: skill
status: active
version: 1.0.0
summary: Translate and explain sheet-metal and CAD terms between English and Turkish using a fixed term-selection policy and a glossary.
tags: [terminology, sheet-metal, solidworks, turkish-ui]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: sheet-metal-terminology
description: Translate and explain sheet-metal, CAD, GD&T and finishing terms between English and Turkish with a fixed term-selection policy and glossary; never invents Turkish SolidWorks labels. Use for terim çevirisi, sacmetal terimleri, Türkçe karşılık, Öztürkçe sözcük seçimi.
---

# Sheet-Metal Terminology

## Purpose
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

## Output contract
Table: EN · TR preferred · alternatives · where to use · note.

## Failure modes
- Inventing Turkish UI labels.
- Replacing a trade term with an unused coined word.
- Mixing markup and margin.

## Self-test
1. Bend deduction in Turkish → bükme düşümü / bükme kesintisi; context-dependent; no UI claim.
2. Turkish menu name of Edge Flange → level U: English name, [doğrulanmadı], how to find it.
3. Are punta kaynağı and nokta kaynağı the same → no; tack weld vs resistance spot weld.
