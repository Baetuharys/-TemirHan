# Smoke tests — Sheet Metal Manufacturability Check

Run each prompt in a fresh chat with the skill loaded. A test passes only if the expected behaviour is present **and** no failure mode occurs.

## Test 1
**Scenario / expected behaviour:** 3 mm thick part with 8 mm flange → Error: flange shorter than tooling minimum (typical).

**Fail if:** Quoting rules of thumb as universal limits.

## Test 2
**Scenario / expected behaviour:** Slot 2 mm from a bend → Risk with distance rule.

**Fail if:** Findings without a location.

## Test 3
**Scenario / expected behaviour:** Request without material → asks material and thickness before judging.

**Fail if:** Not naming the first process that may reject the part.

## Always
- Every number carries a unit and, where relevant, an evidence label.
- Missing inputs are listed, not invented.
