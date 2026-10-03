# Smoke tests — IP Enclosure Design

Run each prompt in a fresh chat with the skill loaded. A test passes only if the expected behaviour is present **and** no failure mode occurs.

## Test 1
**Scenario / expected behaviour:** IP65 target with a vent fan: model must flag that the fan rating limits the enclosure.

**Fail if:** Stating that an IP rating is guaranteed from geometry.

## Test 2
**Scenario / expected behaviour:** Stitch-welded seam in an IPx5 target: model must flag.

**Fail if:** Forgetting cable glands, vents and mounting holes as leakage paths.

## Test 3
**Scenario / expected behaviour:** User asks "is this IP66?": model must answer in terms of design intent and required test.

**Fail if:** Treating NEMA types as identical to IP codes.

## Always
- Every number carries a unit and, where relevant, an evidence label.
- Missing inputs are listed, not invented.
