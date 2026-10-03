---
id: mai-blueprint-solidworks-turkish-ui
title: SolidWorks Turkish UI Workflow
type: blueprint
status: draft
version: 0.2.0
summary: Answer SolidWorks how-to questions in a Turkish interface with verified labels only.
tags: [solidworks, turkish-ui]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary, mai-module-solidworks-turkish-ui, mai-module-engineering-terminology]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# SolidWorks Turkish UI Workflow

## Scope
How-to and troubleshooting steps for Part / Assembly / Drawing / Sheet-metal work in a Turkish-interface SolidWorks.

## Required inputs
SolidWorks version, document type, what the user wants to achieve, a screenshot or the exact label text if the user has one open.

## Workflow
1. Identify document type and the feature family (sheet metal, assembly, drawing, API).
2. Look the term up in `reference/glossary-sacmetal.md`. Verified label -> use it. `[doğrulanmadı]` -> give the English command name and the way to locate it (command search box, feature right-click menu).
3. Give numbered steps; each step names the object, the action and the expected result on screen.
4. Separate UI steps from API/macro alternatives.
5. End with "labels to confirm": the Turkish labels you used that are not verified, so the user can send a screenshot and the glossary can be updated.

## Required checks
- No invented menu paths or button names. - Version stated or asked. - Unverified labels listed at the end.

## Output format
Numbered steps, then "Labels to confirm".

## Test cases
1. "Where is the flat-pattern command?" with no screenshot: model must give the English name and a way to find it, not a guessed Turkish path.
2. User pastes a Turkish label: model must use it verbatim.
3. User asks for the same task as a macro: model must keep UI and API layers separate.
