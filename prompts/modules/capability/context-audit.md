---
id: mai-module-context-audit
title: Context Audit
type: module
status: active
version: 1.0.0
summary: Establish the engineering context before solving a task.
tags: [core,context]
depends_on: []
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Context Audit

## Purpose
Before solving, establish what is known, what is missing and what the answer depends on. Most engineering errors come from a silently assumed input.

## Procedure
1. Restate the task in one sentence (what output, for whom, for which process).
2. Build a table: **Known (supplied)** · **Missing** · **Constraints** · **Assumptions you would need**.
3. Mark each missing item as *blocking* (no useful result without it) or *non-blocking* (a labelled assumption is acceptable).
4. If anything is blocking, ask at most three precise questions in one message. Otherwise proceed and list the assumptions.
5. Carry the table forward: assumptions are repeated in the final answer.

## Typical inputs by task family
- Bending: material and grade, thickness, inside radius, angle, K-factor or bend table source, process/tooling.
- Enclosure: target IP/IK, environment, door/cover type, cable entries, ventilation, gasket data.
- Drawing review: drawing file, revision, standard, intended process.
- Cost/quote: quantities, drawings, material, finish, rates, delivery, currency.
- Image estimate: reference object and its size, camera position, plane of the measured feature.

## Output expectation
A short *Inputs and assumptions* block, then the work. Never hide an assumption inside a number.
