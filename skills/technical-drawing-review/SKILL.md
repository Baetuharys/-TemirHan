---
id: mai-skill-technical-drawing-review
title: Technical Drawing Review
type: skill
status: active
version: 0.2.0
summary: Review mechanical drawings for completeness, consistency, manufacturability communication, and traceable missing information.
tags: [technical-drawing, drawing-review, gd-t]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-source-validation, mai-module-no-fabrication]
last_reviewed: 2026-10-02
input_contract: drawing image/PDF or textual drawing data, manufacturing process, standards if known
output_contract: findings, evidence, missing information, recommendations, verification status
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: technical-drawing-review
description: Review a technical drawing for title block, views, flat pattern, dimensions, tolerances, notes and revision, classifying findings Error/Risk/Suggestion. Use for teknik resim kontrolü, antet, ölçülendirme, genel tolerans.
---
# Technical Drawing Review
## Review order
1. Identity, revision, material, scale, units.
2. Views, sections, details, manufacturing-critical geometry.
3. Dimensions and references; missing, duplicate, or conflicting dimensions.
4. General and specific tolerances.
5. GD&T and datum scheme when present or required.
6. Surface finish, weld symbols, bend notes, hardware, manufacturing notes.
7. Title block and revision traceability.
8. Consistency with the stated manufacturing process.
## Rules
- Do not claim a dimension exists if it is not visible or supplied.
- Separate observation from recommendation.
- If a standard is needed, identify the standard question instead of inventing a requirement.
- Do not redesign silently; report the issue and reason.

## Knowledge to load
Paths are relative to the repository root.
- `knowledge/06-technical-drawing.md`
- `knowledge/07-gdt-and-tolerancing.md`
- `reference/standards-map.md`
