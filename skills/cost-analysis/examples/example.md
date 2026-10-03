# Worked example — cost of a small bent bracket

**Request.** "300 × 200 mm, 2 mm DKP, 4 delik Ø10, 2 büküm, toz boya, 50 adet. Maliyeti çıkar."

**Inputs.** `[FACT-SUPPLIED]` size, thickness, holes, bends, finish, batch 50. Grade assumed DC01 `[ASSUMPTION]`. Rates are **illustrative** (not market data): sheet 40/kg, yield 75 %, laser 30/min at 2000 mm/min, press brake 24/min, setup 30 min, powder coat 150/m², overhead 12 %.

**Result (illustrative).** Direct cost 118.17 → cost **132.36** per part. Price with 20 % markup on cost: **158.83** (margin on price 16.7 %). For a 20 % margin on price: 165.45.

| Item | Calculation | Value |
|---|---|---|
| Blank mass | 0.300·0.200·0.002·7850 | 0.942 kg |
| Material | 0.942/0.75·40 | 50.24 |
| Laser | (1125.7/2000 + 5·0.5/60)·30 | 18.13 |
| Bend setup | 30·24/50 | 14.40 |
| Bend handling | 2·0.3·24 | 14.40 |
| Powder coat | 0.12 m²·150 | 18.00 |
| Packaging | — | 3.00 |
| Overhead 12 % | | 14.18 |

**Sensitivity.** Batch 10 → 196.87, batch 200 → 120.26: setup amortisation is the top driver. Next: material price and yield.

**Open items.** Real machine rates, current sheet price, coating supplier minimum lot, inspection scope.
