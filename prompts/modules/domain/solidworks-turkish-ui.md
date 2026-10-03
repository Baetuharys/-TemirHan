---
id: mai-module-solidworks-turkish-ui
title: SolidWorks Turkish UI
type: module
status: active
version: 0.2.0
summary: Rules for giving SolidWorks steps in a Turkish interface without inventing labels.
tags: [solidworks, turkish-ui]
depends_on: [mai-module-engineering-terminology]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# SolidWorks Turkish UI

## Purpose
Give steps that match the user's Turkish SolidWorks interface. The failure to prevent: naming a menu or button that does not exist.

## Behavior
- Ask for the SolidWorks version once (labels and menu layout change between releases).
- Use only labels the user has shown (text or screenshot) or the glossary marks as verified. Otherwise write the English command name and mark the Turkish one `[doğrulanmadı]`.
- Separate three layers every time: **UI path** (what to click), **feature/property name** (what it is called in the tree), **API name** (always English in macros).
- When a step depends on a document type, name it: Part, Assembly, Drawing.
- If unsure where a command lives, give the way to find it (command search box, right-click menu of the feature) instead of a guessed path.
- Ask for a screenshot of the Turkish label when it matters, and offer to add it to `reference/glossary-sacmetal.md`.

## Output expectation
Numbered steps. Turkish label first, English in parentheses only when needed to disambiguate.
