# IP Codes (IEC 60529) — quick reference

Format: `IP` + first digit (solids) + second digit (water). `X` = not rated for that part.
Check the current edition of IEC 60529 before quoting in a formal document.

## First digit — solid objects / dust
| Digit | Protection |
|---|---|
| 0 | none |
| 1 | objects ≥ 50 mm (large surface of the body, e.g. back of hand) |
| 2 | objects ≥ 12.5 mm (finger) |
| 3 | objects ≥ 2.5 mm (tools, thick wires) |
| 4 | objects ≥ 1 mm (wires, small screws) |
| 5 | dust-protected (limited ingress, no harmful deposit) |
| 6 | dust-tight |

## Second digit — water
| Digit | Protection |
|---|---|
| 0 | none |
| 1 | vertically falling drops |
| 2 | drops with enclosure tilted up to 15° |
| 3 | spraying, up to 60° from vertical |
| 4 | splashing from any direction |
| 5 | water jets (6.3 mm nozzle) |
| 6 | powerful water jets (12.5 mm nozzle) |
| 7 | temporary immersion (up to 1 m, 30 min) |
| 8 | continuous immersion, conditions agreed with the manufacturer |
| 9 | high-pressure, high-temperature jets (`IPX9K` comes from ISO 20653 / DIN 40050-9, not IEC 60529) |

## Sheet-metal design consequences (design intent only — the rating itself comes from testing)
- IP rating is **earned by test**, not by drawing. A design can only *target* a rating.
- IP5x/6x: closed seams, gasketed door, no open through-holes; filter/vent changes the rating.
- IPx4 and above: drip edges / roof slope, door overlap or labyrinth, gasket compression
  defined (groove or flat gasket + stop), cable entries via glands or sealed plates.
- Every cut-out (display, switch, gland, fan) is a seal location; list each one.
- Welded seams that must seal need to be continuous; spot or stitch welds are not a seal by themselves.
- Condensation and drainage are separate from IP; mention them but do not mix them in the rating.
- NEMA / UL enclosure types are **not** one-to-one equivalent to IP codes.
