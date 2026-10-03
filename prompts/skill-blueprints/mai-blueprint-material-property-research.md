---
id: mai-blueprint-material-property-research
title: Engineering Material Property Research
type: blueprint
status: active
version: 0.2.0
summary: Research and normalize material properties for engineering calculations while separating standard data, manufacturer data, and assumptions.
tags: [materials, research, density, mechanical-properties]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---
# Engineering Material Property Research

## Purpose
Research and normalize material properties for engineering calculations while separating standard data, manufacturer data, and assumptions.

## Skill implementation
See `skills/material-property-research/SKILL.md`.

## Core rules
- Do not fabricate missing engineering or commercial inputs.
- Distinguish source-backed data, calculation, estimate, engineering practice, and assumption.
- End with verification and next action.
