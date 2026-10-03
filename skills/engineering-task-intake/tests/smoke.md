# Smoke tests — Engineering Task Intake

Run each prompt in a fresh chat with the skill loaded. A test passes only if the expected behaviour is present **and** no failure mode occurs.

## Test 1
**Scenario / expected behaviour:** "Kabin için IP65 lazım" → asks environment, door type, cable entries; routes to enclosure skills.

**Fail if:** Starting the work while a blocking input is missing.

## Test 2
**Scenario / expected behaviour:** A photo with "ölçüsü kaç?" → asks for a reference object; routes to image-dimension-estimation.

**Fail if:** Asking more than three questions at once.

## Test 3
**Scenario / expected behaviour:** "Bunu SolidWorks'te nasıl yaparım?" without version → asks version and UI language.

**Fail if:** Not naming the downstream skill chain.

## Always
- Every number carries a unit and, where relevant, an evidence label.
- Missing inputs are listed, not invented.
