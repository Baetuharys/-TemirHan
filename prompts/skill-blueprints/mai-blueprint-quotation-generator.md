---
id: mai-blueprint-quotation-generator
title: Manufacturing Quotation Generator
type: blueprint
status: active
version: 0.2.0
summary: Convert a reviewed manufacturing scope and cost basis into a structured technical-commercial quotation without inventing commercial assumptions.
tags: [quotation, cost, commercial, manufacturing]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---
# Manufacturing Quotation Generator

## Purpose
Convert a reviewed manufacturing scope and cost basis into a structured technical-commercial quotation without inventing commercial assumptions.

## Skill implementation
See `skills/quotation-generator/SKILL.md`.

## Core rules
- Do not fabricate missing engineering or commercial inputs.
- Distinguish source-backed data, calculation, estimate, engineering practice, and assumption.
- End with verification and next action.
