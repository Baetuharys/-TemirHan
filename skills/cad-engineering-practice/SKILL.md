---
id: mai-skill-cad-engineering-practice
title: CAD Engineering Practice
type: skill
status: active
version: 1.0.0
summary: Advise on CAD file formats, naming, revision control, configurations, assembly hygiene, release packages and mass properties.
tags: [cad, solidworks, engineering, documentation]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: cad-engineering-practice
description: Advise on CAD practice: file formats (STEP/DXF/DWG/PDF), naming, revision control, configurations, assembly hygiene, release packages, mass properties. Use for CAD dosya yönetimi, STEP/DXF çıkışı, revizyon, PDM, montaj düzeni.
---

# CAD Engineering Practice

## Purpose
CAD data management and modelling practice for sheet-metal and mechanical parts: formats, exchange, naming, references, revision control, release packages, imported-geometry handling.

## Required inputs
CAD system and version, file types involved, goal (exchange, release, cleanup, naming), team/PDM situation

## Workflow
1. Identify the goal: exchange with a supplier, release for production, cleanup of an assembly, naming/revision scheme, imported geometry.
2. Ask for CAD system/version, receiving party, and whether a PDM exists.
3. Select formats per `knowledge/09` (STEP for 3D, DXF for flat profiles, PDF for the drawing); never rely on one format alone.
4. Check naming, references, units and revision consistency across model, drawing, DXF and BOM.
5. Give a release-package checklist and the risks that remain (version, units, configuration).
6. State what could not be verified without opening the actual files.

## Required checks
- Units confirmed (mm) on every exchanged file.
- Revision identical across model, drawing, DXF and BOM.
- No local-drive references; relative paths or Pack and Go.
- No Turkish characters or spaces in names exchanged with other systems.

## Output contract
Recommendation · checklist table (item · status · note) · risks · next actions.

## Failure modes
- Assuming the receiving party has the same CAD version.
- Releasing a model without drawing/DXF at the same revision.
- Treating CAD mass as measured mass.

## Self-test
1. Supplier asks for the CAD file → recommends STEP + DXF + PDF with the same revision, asks which CAD/version they use.
2. Imported STEP must be flattened → checks thickness, units, rebuilds as native sheet metal; does not trust the flatten result blindly.
3. File named 'parça son hali (2) ÇALIŞMA.sldprt' → proposes a numbering scheme and warns about special characters.
