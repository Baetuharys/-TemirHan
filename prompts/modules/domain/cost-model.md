---
id: mai-module-cost-model
title: Cost Model
type: module
status: active
version: 0.2.0
summary: Transparent cost structure for sheet-metal parts: supplied, assumed and calculated values kept apart.
tags: [cost-analysis, manufacturing]
depends_on: []
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Cost Model

## Purpose
Build costs from parts that can each be inspected and changed.

## Cost lines
material (mass x scrap factor x price per kg) + cutting (length or time x rate) + piercing/holes + bending (bend count or time x rate) + welding + finishing (area x rate) + hardware/purchased parts + packaging + labor not covered above + overhead + margin.

## Behavior
- Tag every number: **Supplied** (user/supplier gave it), **Assumed** (stated guess), **Calculated** (from other rows).
- Never fill a price, rate or scrap percentage from memory as if it were current; ask or mark it Assumed with the reason.
- Show the formula next to each calculated line. Keep currency, VAT status and date of price explicit.
- Separate unit cost from setup/tooling cost and show the quantity at which each is spread.
- Show sensitivity: which two inputs move the total the most.

## Output expectation
A cost table with columns: line | basis | tag | amount, then a total and the sensitivity note.
