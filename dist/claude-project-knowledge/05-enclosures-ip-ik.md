---
id: mai-knowledge-enclosures-ip
title: Sheet Metal Enclosures, IP and IK Ratings
category: enclosures
evidence: standard-derived
last_reviewed: 2026-10-02
verify_before_release: [current edition of IEC 60529, IEC 62262, IEC 62208 / IEC 61439 where relevant, gasket datasheet, test lab report]
maturity: implemented
source_ids: [IEC-60529-2.2, IEC-62262-1.1]
---

# Sheet Metal Enclosures, IP and IK Ratings (Sac Kabin, IP ve IK Sınıfları)

## 1. The golden rule
An **IP rating is earned by test, not by drawing.** A design can *target* a rating and a review can find leakage paths, but "this is IP65" is a statement that needs a test report (own lab, accredited lab, or the component supplier's type-test for a catalogue enclosure). The AI must never say "guaranteed IP65" from geometry.

## 2. IP code (IEC 60529 / EN 60529 / TS EN 60529)
Format: `IP` + first digit (solids) + second digit (water) + optional letters. `X` means "not rated for that part", e.g. `IPX4`.

**First digit — solid objects and dust**
| Digit | Protection |
|---|---|
| 0 | none |
| 1 | objects ≥ 50 mm |
| 2 | objects ≥ 12.5 mm (finger) |
| 3 | objects ≥ 2.5 mm |
| 4 | objects ≥ 1 mm |
| 5 | dust-protected (limited ingress, no harmful deposit) |
| 6 | dust-tight (no ingress, vacuum test) |

**Second digit — water**
| Digit | Protection |
|---|---|
| 0 | none |
| 1 | vertically dripping |
| 2 | dripping, enclosure tilted up to 15° |
| 3 | spraying up to 60° from vertical |
| 4 | splashing from any direction |
| 5 | water jets, 6.3 mm nozzle |
| 6 | powerful jets, 12.5 mm nozzle |
| 7 | temporary immersion (typically up to 1 m, 30 min) |
| 8 | continuous immersion, conditions agreed with manufacturer |
| 9 | high-pressure, high-temperature jets (IEC 60529 amendment; `IPX9K` in ISO 20653 for road vehicles) |

Important consequences
- IP65 does not imply IP64, IP66 or IP67 tests were passed. IP66 and IP67 do **not** include each other; a product that needs both is marked `IP66/IP67`.
- IP says nothing about corrosion, UV, impact, pressure, condensation, or explosion protection.
- The additional letters (A, B, C, D; H, M, S, W) are rarely used; do not add them without a source.

## 3. IK code (IEC 62262 / EN 50102 legacy)
Mechanical impact protection.
| IK | Impact energy |
|---|---|
| IK00 | not rated |
| IK01 | 0.14 J |
| IK02 | 0.2 J |
| IK03 | 0.35 J |
| IK04 | 0.5 J |
| IK05 | 0.7 J |
| IK06 | 1 J |
| IK07 | 2 J |
| IK08 | 5 J |
| IK09 | 10 J |
| IK10 | 20 J |
Sheet-metal enclosures often reach IK08–IK10 by wall thickness and construction, but windows, displays and plastic parts decide the real rating.

## 4. NEMA / UL types
NEMA 250 and UL 50/50E enclosure types (e.g. Type 4, 4X, 12) are **not one-to-one equivalent** to IP codes. They also include corrosion, icing, oil and other tests. Give a mapping only as "approximately comparable, not equivalent".

## 5. Leakage paths in a sheet-metal enclosure (checklist)
1. Door/cover seam — gasket continuity, corners, overlap.
2. Gasket joint (a gasket cut from strip is spliced; a moulded or foam-in-place gasket has no joint).
3. Welded seams — must be **continuous**; stitch or spot welds are not a seal.
4. Mounting holes — through-holes into the interior (rear panel holes) need sealing washers or blind (PEM/stud) fasteners.
5. Cable entries — glands, grommets, gland plates; **unused entries must be plugged**.
6. Windows and displays — gasket or adhesive seal; thermal expansion.
7. Vents/breathers — rating of the vent element; open louvers destroy IP5x/6x/ IPx4+.
8. Hinges, locks, handles — shaft seals; lock cut-outs.
9. Fastener screws on the gasket line — local stiffness and spacing.
10. Drains and condensation holes — deliberately open; they define the rating or must be a rated drain/breather.
11. Paint/powder on the gasket face — thickness, drips, runs, coating over welds.
12. Earth (ground) bonding points — masked paint surfaces create gaps if not sealed.

## 6. Design principles that matter in sheet metal
- **Door overlap / labyrinth**: a double-flanged (return) door edge helps against jets and rain; flat butt joints rely entirely on the gasket.
- **Roof slope / drip edge** for outdoor use; no flat top that collects water (IPx4 and above).
- **Gasket compression**: define the compression window from the gasket datasheet (often in the order of 20–40% for foam/elastomer, **verify**), then design the stop (hard stop, embossed stop, door-closing hardware) so that compression is *controlled*, not left to bolt torque.
- **Stiffness at the sealing line**: flanges should not bow between fasteners. Typical fastener pitch for a gasketed cover is shorter than for an unsealed cover (design check, not a rule).
- **Gasket groove vs flat gasket**: a groove controls compression and position; a flat gasket glued to the lid is cheaper but more sensitive to flatness.
- **Corners**: the most common leak; closed-corner welds must be ground flat or the gasket must run around a radius.
- **Cable glands**: use IP-rated glands matching the cable diameter range; the gland's own IP must be ≥ the enclosure's target; unused holes plugged.
- **Material compatibility**: gasket material vs UV, ozone, oil, temperature (EPDM, silicone, PU foam, neoprene differ). State environment.
- **Ventilation and thermal**: fan/filter and breathers are separate design topics; a closed IP65 enclosure traps heat; calculate the dissipated power and allowed internal temperature, consider heat exchanger/air-conditioner, or a rated breather element for pressure equalization.
- **Condensation**: breather membranes, anti-condensation heaters, drain; this is not part of the IP rating.

## 7. Related standards (where to look)
| Topic | Standard family |
|---|---|
| IP code | IEC 60529 (EN 60529) |
| IK code | IEC 62262 |
| Empty enclosures for low-voltage switchgear | IEC 62208 |
| Low-voltage switchgear and controlgear assemblies | IEC 61439 (EN 61439) |
| Machinery electrical equipment | IEC 60204-1 |
| North American enclosure types | NEMA 250, UL 50, UL 50E |
| Stainless/marine/chemical corrosion | project specification; ISO 12944 for coatings on steel structures |
Always cite edition and national adoption (TS EN ...) and confirm before quoting in a formal document.

## 8. Test and evidence
Distinguish: **design intent** (calculation, geometry review) → **prototype test** (own test with documented setup) → **accredited test report** (lab) → **declaration** in the product documentation. Warranty and certification language depends on which level exists.

## 9. Review output template
1. Target IP/IK and exposure (indoor/outdoor, wash-down, dust type, temperature, UV, chemicals).
2. List of leakage paths with a risk (low/medium/high) and a design response.
3. Open items (data needed: gasket datasheet, gland datasheet, cable list, heat load).
4. Test plan.
5. Statement of limits: "Target, not certified".
