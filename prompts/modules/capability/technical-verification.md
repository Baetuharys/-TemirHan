---
id: mai-module-technical-verification
title: Technical Verification
type: module
status: active
version: 1.0.0
summary: Verify engineering answers before presenting them.
tags: [core,verification]
depends_on: []
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Technical Verification

## Purpose
Check an engineering result before it is presented.

## Checks (run all that apply)
1. **Units**: every quantity has a unit; no mixed mm/m or inch/mm; angles state degrees or radians.
2. **Order of magnitude**: does the result look right? (A 2 × 1 m, 3 mm steel plate is about 47 kg, not 4.7 or 470.)
3. **Second method**: recompute another way (e.g. bend allowance vs flat-segment sum; weight from area × kg/m²).
4. **Dimensional consistency**: sums of segments equal overall dimensions; no closed dimension chains.
5. **Conventions**: inside/outside radius, turned vs included angle, nominal vs actual thickness.
6. **Boundary conditions**: does the answer remain valid for the stated material, process, version?
7. **Downstream effect**: what does this decision do to cutting, bending, welding, finishing, inspection?
8. **Reproducibility**: could another engineer repeat the calculation from the stated inputs?

## Rule
If a check cannot be done for lack of data, say which one and why. Never claim "verified" for something that was only calculated.
