---
id: mai-blueprint-sheet-metal-weld-fastener-review
title: Sheet Metal Weld and Fastener Review
type: blueprint
status: active
version: 0.2.0
summary: Review welds, studs, PEM-style fasteners, screws, nuts, and assembly interfaces on sheet-metal designs and drawings.
tags: [sheet-metal, welding, fasteners, assembly]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---
# Sheet Metal Weld and Fastener Review

## Purpose
Review welds, studs, PEM-style fasteners, screws, nuts, and assembly interfaces on sheet-metal designs and drawings.

## Skill implementation
See `skills/sheet-metal-weld-fastener-review/SKILL.md`.

## Core rules
- Do not fabricate missing engineering or commercial inputs.
- Distinguish source-backed data, calculation, estimate, engineering practice, and assumption.
- End with verification and next action.
