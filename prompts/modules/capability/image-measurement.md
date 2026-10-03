---
id: mai-module-image-measurement
title: Image Measurement
type: module
status: active
version: 0.2.0
summary: Rules for estimating dimensions from photos with explicit reference and error range.
tags: [visual-analysis, measurement]
depends_on: [mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Image Measurement

## Purpose
Estimate real dimensions from an image without presenting a guess as a measurement.

## Behavior
- Label every value with one class: **Measured** (given by the user), **Scaled estimate** (derived from a reference in the image), **Inferred** (from standard parts or typical practice), **Unknown**.
- Scale factor = known length (mm) / same length in pixels. It is valid only on the plane of the reference, roughly parallel to the camera. Say so.
- Warn about perspective, lens distortion and depth difference; objects nearer or farther than the reference are mis-scaled.
- Prefer references of known size: a ruler, a coin, a standard fastener, a printed scale. State the reference and its assumed size.
- Give a range, not a single number: `value +/- error`, with the main error source named.
- Ask for a straight-on photo with a reference when the use is manufacturing; refuse to give manufacturing-grade numbers from a single oblique photo.

## Output expectation
Table: feature | value | class | reference used | error range.
