---
id: mai-skill-cad-modeling-review
title: CAD Modelling Review
type: skill
status: draft
maturity: drafted
version: 2.0.0
summary: Review a CAD part or assembly for design intent, feature-tree hygiene, configurations, references, material assignment and export readiness.
tags: [cad, solidworks, modeling, review]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management, mai-module-no-fabrication]
last_reviewed: 2026-10-02
input_contract: see 'Required inputs'
output_contract: see 'Output contract'
portability: provider-agnostic
adapter_support: [chatgpt, claude, codex, generic-llm]
name: cad-modeling-review
description: Review CAD parts or assemblies for design intent, feature-tree hygiene, references, configurations, material assignment, mass plausibility and export readiness before drawings or manufacturing data are released.
---

# CAD Modelling Review

## Purpose
Review a 3D CAD model (SolidWorks or similar) for robustness: design intent, sketch and feature order, references, configurations, material and mass, naming, and export formats, before drawings or manufacturing data are made.

## Use when
- a model will be handed to another person or to drawing/DXF production
- rebuild errors, broken references or slow files appear
- a library of standard parts or templates is being set up

## Required inputs
- the model or a description/screenshot of the feature tree
- intended downstream use: drawing, DXF, STEP exchange, simulation
- company naming and template rules, if any

## Workflow (details: `workflows/default-workflow.md`)
1. **State the design intent**: Which dimensions drive the part and which are derived; which features must update together.
2. **Check sketches and features**: Fully defined sketches, sensible feature order, no unnecessary dependency chains, meaningful names, no suppressed leftovers.
3. **Check references**: External references and in-context relations are intended; broken or dangling references are listed.
4. **Check configurations and properties**: Configuration names are purposeful; custom properties filled; material assigned; mass properties plausible.
5. **Check assemblies**: Mates are sensible, no over-definition, interference checked where needed, large assemblies handled with lightweight or simplified representations.
6. **Check exports**: Formats fit the need: STEP for neutral 3D exchange (ISO 10303), DXF/DWG for flat 2D, native for editing; units and revision recorded.

## Rules
- Review does not change the model; it lists findings.
- Rules on naming come from the company template, not from this library.
- Never claim a model is 'correct'; say which checks passed.
- Sheet-metal specifics go to the sheet-metal skills.
- Evidence labels (SUPPLIED / CALCULATED / SOURCE-BACKED / PRACTICE / ASSUMED / ESTIMATED / UNKNOWN) are used on every value; see `reference/market-and-evidence-labels.md`.

## Output contract
1. Findings table: # | location | class (Error/Risk/Suggestion) | finding | fix
2. Open questions

## Failure modes
- Fixing symptoms in the tree instead of the intent.
- Ignoring external references.
- Wrong material giving wrong mass.
- Exporting without units or revision.

## Repository references
- `skills/solidworks-sheet-metal-workflow/SKILL.md`
- `skills/weight-analysis/SKILL.md`

## Maturity
`drafted`: written with workflow, examples and tests; not yet run on a real project file. Promote to `field-tested` only after `tests/` pass on real work (see `docs/maturity-model.md`).
