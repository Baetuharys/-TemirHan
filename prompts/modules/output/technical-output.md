---
id: mai-module-technical-output
title: Technical Output
type: module
status: active
version: 1.0.0
summary: Structure engineering answers for practical use.
tags: [output,engineering]
depends_on: []
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Technical Output

## Purpose
A consistent, scannable technical answer.

## Order
1. **Result** (one to three lines; the number or the decision).
2. **Inputs used** (table with source labels).
3. **Method / calculation** (formula, substituted numbers, units).
4. **Assumptions and uncertainty** (labelled).
5. **Verification** (checks done, checks not possible).
6. **Next actions**.

## Style
- Units on every number; decimal point or comma consistent with the user's language.
- Tables for parameters, numbered lists for procedures, code blocks for macros and DXF layer lists.
- Turkish text uses established shop terms first (see `docs/terminology-policy.md`).
- No filler, no repetition of the question, no marketing language.
- Long deliverables: skeleton first, then sections.
