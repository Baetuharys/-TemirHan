# Smoke tests — GD&T Selection

Run each prompt in a fresh chat with the skill loaded. A test passes only if the expected behaviour is present **and** no failure mode occurs.

## Test 1
**Scenario / expected behaviour:** Mounting plate with 4 holes → position with ⌀ zone to datums A|B|C; MMC only if clearance fits.

**Fail if:** Referencing undefined datums.

## Test 2
**Scenario / expected behaviour:** Request "flatness 0.05 on 1 m × 1.5 mm sheet" → flagged as unrealistic/non-rigid; asks function and restraint.

**Fail if:** Tolerances tighter than the process can hold.

## Test 3
**Scenario / expected behaviour:** Drawing with frame referencing datum "D" not defined → flagged as Error.

**Fail if:** MMC without a clearance check.

## Always
- Every number carries a unit and, where relevant, an evidence label.
- Missing inputs are listed, not invented.
