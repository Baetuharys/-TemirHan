---
id: mai-skill-solidworks-turkish-ui
title: SolidWorks Turkish UI Guidance
type: skill
status: active
version: 0.2.0
summary: Guide SolidWorks users through the Turkish interface while preserving English command names for disambiguation.
tags: [solidworks, turkish-ui, cad]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-solidworks-turkish-ui]
last_reviewed: 2026-10-02
input_contract: SolidWorks task, UI language, version when known, workspace/context
output_contract: Turkish menu/command path, alternatives, version caveat, verification step
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: solidworks-turkish-ui
description: Give SolidWorks steps for a Turkish interface using verified (V), common (C) or unverified (U) labels and never inventing menu names. Use for SolidWorks Türkçe arayüz, komut adı, menü yolu, terim doğrulama.
---
# SolidWorks Turkish UI Guidance
## Workflow
1. Identify Part, Sheet Metal, Assembly, Drawing, or other workspace.
2. Give the Turkish UI path first.
3. Add the English command name only for disambiguation.
4. Mark version-dependent labels instead of inventing them.
5. Treat screenshots as primary evidence when supplied.
6. Give the shortest actionable sequence plus a verification check.
## Rules
- Never fabricate Turkish labels.
- Do not silently switch to an English-interface workflow.
- Distinguish command, PropertyManager field, feature-tree item, and document property.

## Knowledge to load
Paths are relative to the repository root.
- `knowledge/04-solidworks-turkish-ui-and-terminology.md`
- `reference/solidworks-ui-labels.csv` (V/C/U label levels)
- `reference/glossary-sacmetal.md`
