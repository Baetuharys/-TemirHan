# Worked example — U-channel flat length

**Part.** 1.5 mm sheet, inside radius 1.5 mm, outside legs 20 / 60 / 20 mm, two 90° bends. K = 0.38 from the shop's bend table `[SOURCE-BACKED]`.

**Calculation.** `BA = (π/2)·(1.5 + 0.38·1.5) = 3.252 mm` · `OSSB = (1.5+1.5)·tan45° = 3.000 mm` · `BD = 2·3.000 − 3.252 = 2.748 mm`.
`Flat length = 100 − 2·2.748 = 94.503 mm` `[CALCULATED]`.
Second method: flat segments `(20−3) + (60−6) + (20−3) = 88` ; plus `2·3.2515 = 6.503` → **94.503 mm** ✓ (same result by the second method).

**Checks.** Compare with the SolidWorks flat pattern (same K or same bend table?) · relief at the ends · holes ≥ 2.5·T + R = 5.25 mm from the bend lines · bend lines on their own DXF layer · test bend before series.

**Output note for the drawing.** "Flat pattern generated with K = 0.38, shop bend table rev. B."
