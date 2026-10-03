---
id: mai-knowledge-metrology-inspection-quality
title: Metrology, Inspection and Quality Planning
category: quality
evidence: engineering-practice
last_reviewed: 2026-10-02
verify_before_release: [critical characteristics, measurement method, gauge capability, sampling/acceptance plan, datum setup]
maturity: implemented
source_ids: [ISO-5459-2024, ISO-1101-2017]
---

# Metrology, Inspection and Quality Planning

## Design dimensions that can be verified
A dimension or GD&T control is only useful if manufacturing and inspection can establish the referenced features/datums. Avoid creating an elegant drawing that requires an unavailable measurement setup for every part.

## Characteristic classes
Separate:
- safety/regulatory or interface-critical characteristics;
- function-critical dimensions;
- process-control dimensions;
- reference/information-only dimensions.

This helps avoid inspecting every dimension with the same effort.

## Measurement planning
For each critical item state: nominal/tolerance, datum setup, tool or method, access/orientation, frequency or sampling rule, recording requirement and reaction plan. Match measurement uncertainty/capability to the tolerance being judged.

## Sheet-metal realities
Formed parts relax when unclamped; flexible panels can be distorted by the fixture. Define whether inspection is free-state, restrained or assembled when this changes the result. Measure hole patterns and interfaces from functional datums rather than accumulating chained dimensions where possible.

## First article / prototype
Use early builds to validate both the part and the measurement method. A repeated disagreement between CAD and inspection can be a datum/fixture problem, not only a fabrication problem.
