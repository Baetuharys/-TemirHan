---
id: mai-blueprint-engineering-task-intake
title: Engineering Task Intake
type: blueprint
status: draft
version: 1.0.0
summary: Classify an engineering request, find blocking gaps and route it to the right skill chain.
tags: [core, engineering]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary]
last_reviewed: 2026-10-02
input_contract: user request in any form (text, drawing, photo, files)
output_contract: task summary, known/missing inputs, skill chain, first questions
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Engineering Task Intake

## Scope
First contact with any engineering request: classify it, find what is missing, route it to the right skill. Does not solve the task.

## Required inputs
The user's request in any form (text, drawing, photo, file list).

## Workflow
1. Classify the task family: bending/flat pattern · enclosure/IP · drawing review · GD&T · weight · cost/quote · documentation · SolidWorks UI/macro · image measurement · market research · visual generation.
2. Extract known facts (material, thickness, quantity, process, standard, software version, deadline).
3. List missing inputs; mark blocking vs non-blocking.
4. Ask at most three questions, or proceed with labelled assumptions.
5. Name the skill chain, e.g. `ip-enclosure-design → enclosure-gasket-review → sheet-metal-manufacturability-check`.
6. State the expected deliverable and its format.

## Required checks
- Task family is named explicitly.
- No work is started on a blocking gap.
- Confidential data is not copied into public places.

## Output format
Task summary · Known · Missing (blocking/non-blocking) · Proposed skill chain · First question(s).

## Test cases
1. "Kabin için IP65 lazım" → asks environment, door type, cable entries; routes to enclosure skills.
2. A photo with "ölçüsü kaç?" → asks for a reference object; routes to image-dimension-estimation.
3. "Bunu SolidWorks'te nasıl yaparım?" without version → asks version and UI language.
