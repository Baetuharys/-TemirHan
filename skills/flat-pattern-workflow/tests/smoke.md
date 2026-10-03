# Smoke tests — Flat Pattern Workflow

Run each prompt in a fresh chat with the skill loaded. A test passes only if the expected behaviour is present **and** no failure mode occurs.

## Test 1
**Scenario / expected behaviour:** No K-factor given → asks for source; offers labelled estimate range.

**Fail if:** Presenting a flat length as verified without a K-factor source.

## Test 2
**Scenario / expected behaviour:** Hole 3 mm from a 2 mm-thick bend → flagged as risk with distance rule.

**Fail if:** Mixing inside/outside dimension conventions.

## Test 3
**Scenario / expected behaviour:** DXF with bend lines on the cut layer → flagged as Error.

**Fail if:** Leaving bend lines on the cut layer.

## Always
- Every number carries a unit and, where relevant, an evidence label.
- Missing inputs are listed, not invented.
