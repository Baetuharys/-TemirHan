# Smoke tests — Image Dimension Estimation

Run each prompt in a fresh chat with the skill loaded. A test passes only if the expected behaviour is present **and** no failure mode occurs.

## Test 1
**Scenario / expected behaviour:** Part photographed with a ruler beside it, straight-on: Scaled estimates with small error.

**Fail if:** Giving a single exact number without range and confidence.

## Test 2
**Scenario / expected behaviour:** Part photographed obliquely, no reference: model must refuse numbers and ask for a reference.

**Fail if:** Reference object not in the same plane.

## Test 3
**Scenario / expected behaviour:** Features at different depth than the reference: model must warn and widen the range.

**Fail if:** Using an estimate for manufacturing.

## Always
- Every number carries a unit and, where relevant, an evidence label.
- Missing inputs are listed, not invented.
