---
id: mai-blueprint-enclosure-gasket-review
title: Sheet Metal Enclosure Gasket Review
type: blueprint
status: active
version: 0.2.0
summary: Review gasket, cover, flange, cable-entry, ventilation, drainage, and joint features against an enclosure sealing requirement.
tags: [enclosure, ip, gasket, sheet-metal]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---
# Sheet Metal Enclosure Gasket Review

## Purpose
Review gasket, cover, flange, cable-entry, ventilation, drainage, and joint features against an enclosure sealing requirement.

## Skill implementation
See `skills/enclosure-gasket-review/SKILL.md`.

## Core rules
- Do not fabricate missing engineering or commercial inputs.
- Distinguish source-backed data, calculation, estimate, engineering practice, and assumption.
- End with verification and next action.
