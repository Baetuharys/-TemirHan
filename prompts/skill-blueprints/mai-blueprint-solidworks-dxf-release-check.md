---
id: mai-blueprint-solidworks-dxf-release-check
title: SolidWorks DXF Release Check
type: blueprint
status: active
version: 0.2.0
summary: Review a SolidWorks sheet-metal DXF before laser/CAM release, including scale, geometry, cut/mark separation, and revision consistency.
tags: [solidworks, dxf, laser, release]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---
# SolidWorks DXF Release Check

## Purpose
Review a SolidWorks sheet-metal DXF before laser/CAM release, including scale, geometry, cut/mark separation, and revision consistency.

## Skill implementation
See `skills/solidworks-dxf-release-check/SKILL.md`.

## Core rules
- Do not fabricate missing engineering or commercial inputs.
- Distinguish source-backed data, calculation, estimate, engineering practice, and assumption.
- End with verification and next action.
