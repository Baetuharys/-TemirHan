---
id: mai-module-action-summary
title: Action Summary
type: module
status: active
version: 1.0.0
summary: End technical guidance with a concise actionable sequence.
tags: [output,workflow]
depends_on: []
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Action Summary

## Purpose
End every substantial answer with a clear next step.

## Format
**Next actions** (max 5, ordered, each with an owner if known):
1. What to do, concretely (measure X, send Y, load table Z).
2. Who or what is needed.
3. What the result will unlock.

Add **Open items** when information is missing: a list of `[OPEN]` items, each with the question that closes it.

## Rules
- Actions are executable, not generic ("check the drawing" is not an action; "confirm K-factor with the bending shop" is).
- Never promise work that has not been done.
- Keep it under ten lines.
