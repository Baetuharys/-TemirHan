# Smoke tests — SolidWorks Sheet Metal Workflow

Run each prompt in a fresh chat with the skill loaded. A test passes only if the expected behaviour is present **and** no failure mode occurs.

## Test 1
**Scenario / expected behaviour:** User asks "Edge Flange'in Türkçe adı ne?" → English name + [doğrulanmadı] + how to search; asks for a screenshot.

**Fail if:** Inventing Turkish menu labels or paths.

## Test 2
**Scenario / expected behaviour:** Flatten fails → asks for the error text; lists likely causes in order.

**Fail if:** Not asking the SolidWorks version.

## Test 3
**Scenario / expected behaviour:** User gives no version → asks version and language before steps.

**Fail if:** Using a K-factor different from the shop's without saying so.

## Always
- Every number carries a unit and, where relevant, an evidence label.
- Missing inputs are listed, not invented.
