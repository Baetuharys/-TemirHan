# Worked example — plate weight

**Request.** "1 m × 2 m × 3 mm levha kaç kg? Çelik ve 304 için."

| Material | ρ (kg/m³) | V (m³) | Mass |
|---|---|---|---|
| Carbon steel | 7850 | 1·2·0.003 = 0.006 | **47.10 kg** `[CALCULATED]` |
| Stainless 1.4301 | 7930 | 0.006 | **47.58 kg** |
| EN AW-5754 (for comparison) | 2670 | 0.006 | 16.02 kg |

Check: steel ≈ 7.85 kg/m² per mm → 2 m² · 3 mm · 7.85 = 47.1 kg ✓.
Notes: nominal thickness; thickness tolerance changes mass by a few percent; densities from `knowledge/15` (state the source in formal documents). Blank mass for purchasing ≠ finished-part mass (cut-outs, hardware, coating are separate).
