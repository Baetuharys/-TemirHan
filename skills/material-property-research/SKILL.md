---
id: mai-skill-material-property-research
title: Engineering Material Property Research
type: skill
status: active
version: 0.3.0
summary: Research and normalize material properties for engineering calculations while separating standard data, manufacturer data, and assumptions.
tags: [materials, research, density, mechanical-properties]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
input_contract: engineering context, design/manufacturing intent, available model/drawing/data, constraints
output_contract: structured result, assumptions, verification checklist, unresolved inputs, next action
portability: provider-agnostic
adapter_support: [chatgpt, claude]
name: material-property-research
description: Look up and cite material properties and grade equivalences with source and condition, never from memory alone. Use for malzeme özellikleri, DC01/S235/304/316/5754 karşılaştırma, yoğunluk, mekanik değerler.
---
# Engineering Material Property Research
## Workflow
1. Identify exact material designation, temper/condition, product form, and applicable standard.
2. Define required properties: density, yield strength, tensile strength, elastic modulus, thermal data, etc.
3. Prefer primary standards, manufacturer datasheets, and recognized technical databases; record source and date.
4. Compare multiple sources and explain differences caused by alloy, temper, product form, or test condition.
5. Normalize units and avoid mixing values from different conditions.
6. For weight calculations, explicitly state the density used and its source; if only an approximate density is available, label the result accordingly.
7. Do not substitute a similar alloy or temper without disclosure.

## Output
Return a property table, exact material designation, sources, unit conversions, uncertainty notes, and recommended value for the stated calculation.

## Knowledge to load
Paths are relative to the repository root.
- `knowledge/15-materials-reference.md`
