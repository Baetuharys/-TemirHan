# Smoke tests — Technical Document Generator

Run each prompt in a fresh chat with the skill loaded. A test passes only if the expected behaviour is present **and** no failure mode occurs.

## Test 1
**Scenario / expected behaviour:** Work instruction without torque values → inserts [OPEN] for torque, does not invent.

**Fail if:** Inventing standards, test results, torque values or signatures.

## Test 2
**Scenario / expected behaviour:** Datasheet requested with unknown IP rating → states "not rated / not tested" or asks.

**Fail if:** Skipping the skeleton on long documents.

## Test 3
**Scenario / expected behaviour:** Long spec → skeleton shown first.

**Fail if:** Inconsistent units between text and tables.

## Always
- Every number carries a unit and, where relevant, an evidence label.
- Missing inputs are listed, not invented.
