---
id: mai-knowledge-cost-analysis
title: Sheet-Metal Cost Analysis (Maliyet Analizi)
category: cost
evidence: calculation
last_reviewed: 2026-10-02
verify_before_release: [material prices, machine hour rates, shop overhead, subcontractor quotes]
maturity: implemented
source_ids: []
---

# Sheet-Metal Cost Analysis (Maliyet Analizi)

## 1. Cost model
```text
Part cost = Material + Cutting + Forming (bending) + Joining + Finishing + Hardware
          + Setup/Tooling (amortised) + Inspection + Packaging + Logistics
          + Overhead (genel gider) + Risk allowance
Price     = Cost + Margin
```
All rates in this file are **illustrative, not market data**. Replace them with the shop's numbers.

## 2. Components and drivers
| Component | Formula / driver |
|---|---|
| Material | `mass / nesting yield × price per kg`; mass = `L·W·T·ρ` of the **blank**, not the finished part |
| Nesting yield | usable-sheet utilisation; small parts in big sheets 70–85 %, depends on nesting and remnants |
| Laser cutting | `(cut length / cutting speed + pierces × pierce time) × machine rate`; speed falls with thickness |
| Punching | hits × time per hit × machine rate (+ tool cost if new tools) |
| Bending | `setup / batch + bends × handling time × press brake rate`; setup depends on tooling changes |
| Welding | length or number of tacks × time × rate; grinding after welding |
| Hardware (PEM, nuts, glands, gaskets) | purchase price × quantity + insertion time |
| Finishing | powder coat: area × price per m² (+ masking); galvanizing/anodizing: per kg or per m²; minimum lot charges |
| Inspection | frequency, first-article, certificate requirements |
| Packaging/logistics | per part or per pallet |
| Overhead | percent of direct cost or hourly burden |
| Risk | allowance for new process, tight tolerance, scrap risk |

## 3. Worked example (illustrative rates)
Part: flat blank 300 × 200 mm, 2 mm DC01, 4 holes ⌀10, 2 bends, powder coat, batch 50.
| Item | Calculation | Value |
|---|---|---|
| Mass of blank | 0.300 × 0.200 × 0.002 × 7850 | 0.942 kg |
| Material | 0.942 / 0.75 yield × 40 per kg | 50.24 |
| Cut length | 2×(300+200) + 4×π×10 | 1125.7 mm |
| Laser | (1125.7/2000 + 5 pierces × 0.5 s) × 30 per min | 18.13 |
| Bend setup | 30 min × 24 per min / 50 | 14.40 |
| Bend handling | 2 bends × 0.3 min × 24 | 14.40 |
| Powder coat | 0.12 m² (both faces) × 150 per m² | 18.00 |
| Packaging | — | 3.00 |
| **Direct cost** | | **118.17** |
| Overhead 12 % | | 14.18 |
| **Cost** | | **132.36** |
| Price with 20 % **markup on cost** | cost × 1.20 | 158.83 (margin on price 16.7 %) |
| Price for 20 % **margin on price** | cost / 0.80 (rounded cost 132.36) | 165.45 |

Batch sensitivity of the same part (same rates): batch 10 → cost 196.87; batch 50 → 132.36; batch 200 → 120.26. Setup amortisation is the largest lever on small batches.

## 4. Quick cost-reduction levers (design for manufacturing)
Fewer bends and fewer different bend radii/tools · allow a standard thickness and grade · avoid features that need new tools · nest-friendly shapes (common-line cutting) · loosen tolerances that do not matter · avoid secondary operations (tapping, deburr by hand) · combine parts when function allows · minimise painted area/ masking · standard fasteners.

## 5. Margin vs markup
`markup = (price − cost)/cost`, `margin = (price − cost)/price`. Always label which one the user means.

## 6. Sensitivity and uncertainty
Report ranges: material ± price change, yield ± 5 points, machine time ± 10–20 %. Show the **top 3 drivers**. If a rate is guessed, mark it `[ASSUMPTION]` and list it among the open items.

## 7. Output template
1. Inputs and assumptions table. 2. Cost breakdown table. 3. Unit price and lot price at quantity breaks. 4. Sensitivity (top drivers). 5. Open items (needed rates/prices). 6. Statement: illustrative if rates are not supplied.
