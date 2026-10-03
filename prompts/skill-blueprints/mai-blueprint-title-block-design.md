---
id: mai-blueprint-title-block-design
title: Sheet Metal Technical Drawing Title Block Design
type: blueprint
status: active
version: 0.2.0
summary: Design and review a concise technical drawing title block for sheet-metal parts, with revision and manufacturing information.
tags: [technical-drawing, title-block, sheet-metal, solidworks]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---
# Sheet Metal Technical Drawing Title Block Design

## Purpose
Design and review a concise technical drawing title block for sheet-metal parts, with revision and manufacturing information.

## Skill implementation
See `skills/title-block-design/SKILL.md`.

## Core rules
- Do not fabricate missing engineering or commercial inputs.
- Distinguish source-backed data, calculation, estimate, engineering practice, and assumption.
- End with verification and next action.
