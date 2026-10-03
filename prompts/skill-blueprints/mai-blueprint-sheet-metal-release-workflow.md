---
id: mai-blueprint-sheet-metal-release-workflow
title: Sheet Metal Manufacturing Release Workflow
type: blueprint
status: active
version: 0.2.0
summary: End-to-end release from SolidWorks sheet-metal model through drawing, DXF, laser marking, bending, welding, assembly, cost, and documentation.
tags: [sheet-metal, solidworks, release, manufacturing]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---
# Sheet Metal Manufacturing Release Workflow

## Purpose
End-to-end release from SolidWorks sheet-metal model through drawing, DXF, laser marking, bending, welding, assembly, cost, and documentation.

## Skill implementation
See `skills/sheet-metal-release-workflow/SKILL.md`.

## Core rules
- Do not fabricate missing engineering or commercial inputs.
- Distinguish source-backed data, calculation, estimate, engineering practice, and assumption.
- End with verification and next action.
