---
id: mai-skill-engineering-task-intake
title: Engineering Task Intake
type: skill
status: active
version: 1.0.0
summary: Convert an informal engineering request into requirements, missing inputs, assumptions and an actionable plan.
tags: [core, engineering, mechanical]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: engineering-task-intake
description: First-step triage for any mechanical or sheet-metal request: classify the task, list missing inputs, route to the right skill chain. Use when a request is vague or spans several topics.
---
# Engineering Task Intake

## Purpose
First contact with any engineering request: classify it, find what is missing, route it to the right skill. Does not solve the task.

## Trigger
First-step triage for any mechanical or sheet-metal request: classify the task, list missing inputs, route to the right skill chain. Use when a request is vague or spans several topics.

## Required inputs
The user's request in any form (text, drawing, photo, file list).

## Operating rules
1. Extract the user's actual requirement before proposing a solution.
2. Distinguish supplied facts, calculated results, engineering-practice guidance, assumptions, and estimates.
3. Never invent missing dimensions, material properties, standards, machine capabilities, SolidWorks menu paths, API behavior, or process parameters.
4. Use consistent units and show the governing relationship when a calculation is performed.
5. When the result depends on a machine, tool, CAM system, material grade, SolidWorks version, or customer standard, identify that dependency.
6. If critical input is missing, either ask for it or proceed with a clearly labeled assumption when a useful preliminary result is still possible.
7. Finish with verification checks and a concise action summary.

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

## Output contract
Task summary · Known · Missing (blocking/non-blocking) · Proposed skill chain · First question(s).

## Failure modes
- Starting the work while a blocking input is missing.
- Asking more than three questions at once.
- Not naming the downstream skill chain.

## Knowledge to load
Paths are relative to the repository root.
- `knowledge/README.md` (index)

## Self-test
1. "Kabin için IP65 lazım" → asks environment, door type, cable entries; routes to enclosure skills.
2. A photo with "ölçüsü kaç?" → asks for a reference object; routes to image-dimension-estimation.
3. "Bunu SolidWorks'te nasıl yaparım?" without version → asks version and UI language.

See also: `workflows/default-workflow.md`, `examples/example.md`, `tests/smoke.md`.
