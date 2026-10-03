# Smoke tests — Weight Analysis

Run each prompt in a fresh chat with the skill loaded. A test passes only if the expected behaviour is present **and** no failure mode occurs.

## Test 1
**Scenario / expected behaviour:** 1 m × 2 m × 3 mm steel plate → 47.1 kg `[CALCULATED]`.

**Fail if:** Assuming stainless density equals steel.

## Test 2
**Scenario / expected behaviour:** Same in 1.4301 → ≈ 47.6 kg with ρ ≈ 7930 kg/m³; states density source.

**Fail if:** Mixing mm and m.

## Test 3
**Scenario / expected behaviour:** "Part is 5 kg" vs CAD 4.2 kg → asks configuration, density, hardware, coating.

**Fail if:** Reporting blank mass as finished mass.

## Always
- Every number carries a unit and, where relevant, an evidence label.
- Missing inputs are listed, not invented.
