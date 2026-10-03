---
id: mai-knowledge-tolerance-stack
title: Tolerance Stack, Fits and Functional Clearances
category: tolerancing
evidence: formula-and-practice
last_reviewed: 2026-10-02
verify_before_release: [drawing standard, process capability, datum scheme, measurement method]
maturity: implemented
source_ids: [ISO-1101-2017, ISO-5459-2024, ASME-Y14.5-2018-R2024, ISO-2768-1-1989]
---

# Tolerance Stack, Fits and Functional Clearances

## 1. Separate three questions
- **Nominal geometry:** what is the intended size/location?
- **Allowed variation:** what tolerance is assigned and under which standard?
- **Functional result:** what clearance/interference/misalignment may occur at assembly?

A drawing can be dimensionally “within tolerance” and still fail function if the datum scheme or stack path is wrong.

## 2. 1-D worst-case stack
For a signed chain `R = ±A ±B ...`, use the same signs for nominals and calculate worst-case bounds from each contributor’s limits. The helper in `tools/calculators/tolerance.py` is appropriate only when the stack is genuinely one-dimensional.

## 3. RSS/statistical stack
RSS is **not** a magic tighter tolerance. Use it only if the statistical assumptions are justified by process data and the tolerances have been converted to compatible statistical quantities. Otherwise use worst-case or a process-capability model agreed with quality/manufacturing.

## 4. Sheet-metal realities
- bend angle/radius variation can convert into large edge-position error over long flanges;
- formed features may require profile/position concepts rather than very tight ± dimensions;
- welding adds distortion and fixture dependence;
- coating thickness affects tight fits, grounding points and gasket interfaces;
- laser-cut accuracy does not imply bent-assembly accuracy.

## 5. Datum selection
Datums should represent the functional locating interfaces and a realistic inspection setup. Do not choose a thin free edge as a primary datum simply because it is convenient on the drawing.

## 6. General tolerances
If a drawing references a general-tolerance standard, verify the **edition and scope**. The source registry notes that ISO 2768-1:1989 remained published while a replacement edition was under publication in 2026. Do not silently assume an old company title-block note is still current.

## 7. Output expected from the AI
A useful tolerance answer includes the stack path, signs, nominal result, worst-case result, any statistical assumption, the functional requirement being protected, and a recommendation for which dimensions should be controlled directly.
