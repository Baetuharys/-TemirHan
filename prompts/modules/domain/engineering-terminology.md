---
id: mai-module-engineering-terminology
title: Engineering Terminology
type: module
status: active
version: 0.2.0
summary: Term-selection order: UI labels, standards, shop-floor terms, then Turkic-rooted words.
tags: [terminology, engineering]
depends_on: []
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Engineering Terminology

## Purpose
Keep terms consistent and understandable. Full rule set: `docs/terminology-policy.md`.

## Behavior
- Order of choice: (1) exact SolidWorks UI label, (2) term from the cited standard, (3) established shop-floor term, (4) Turkic-rooted word in prose when it is already in real use, (5) coined words only as a marked suggestion.
- In Turkish prose prefer words like *açınım, büküm, kesim, kaynak, delik* when they are the established term anyway.
- Never replace a standard term or a UI label with a purer word.
- When two Turkish terms compete (e.g. *punta* vs *nokta kaynağı*), define which one the document uses, once.
- Use `reference/glossary-sacmetal.md` as the lookup; add new terms there, not inline.
