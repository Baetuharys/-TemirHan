# Smoke tests — Cost Analysis

Run each prompt in a fresh chat with the skill loaded. A test passes only if the expected behaviour is present **and** no failure mode occurs.

## Test 1
**Scenario / expected behaviour:** Fully supplied rates: all rows Supplied/Calculated, no Assumed.

**Fail if:** Using illustrative rates as if they were market prices.

## Test 2
**Scenario / expected behaviour:** No bending rate: model must ask or mark Assumed, not fill from memory.

**Fail if:** Confusing markup with margin.

## Test 3
**Scenario / expected behaviour:** Quantity changes from 10 to 1000: model must show how setup cost per piece changes.

**Fail if:** Costing the finished part mass instead of the blank for material.

## Always
- Every number carries a unit and, where relevant, an evidence label.
- Missing inputs are listed, not invented.
