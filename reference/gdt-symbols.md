# Geometrical tolerancing — symbol groups (ISO 1101 / ASME Y14.5)

Check the current edition. Differences between ISO and ASME practice matter (e.g. fundamental tolerancing principle ISO 8015 vs. ASME Rule #1).

| Group | Characteristic | Needs datum? |
|---|---|---|
| Form | straightness, flatness, circularity, cylindricity | no |
| Profile | profile of a line, profile of a surface | optional (yes if locating) |
| Orientation | perpendicularity, parallelism, angularity | yes |
| Location | position; ISO also concentricity and symmetry | yes |
| Runout | circular runout, total runout | yes (axis datum) |

- ASME Y14.5 (from the 2009 edition) no longer includes concentricity and symmetry; ISO 1101 still does. Confirm which standard the customer drawing uses.
- A tolerance frame reads left to right: symbol | tolerance value (with diameter sign or modifier when needed) | datum references in order of precedence.
- Datums come from functional mounting surfaces, not from whatever is convenient to measure.
- General tolerances: ISO 2768-1 (linear/angular), ISO 2768-2 (geometrical: H, K, L classes); welded constructions: ISO 13920. A general-tolerance note must be on the drawing to apply.

## Sheet-metal reminders
- Large thin panels are not flat in free state; a flatness callout needs a stated measurement condition (free/restrained) or use profile of a surface.
- Hole patterns that cross a bend: state which flange carries the datum, and whether the pattern is controlled relative to the same flange.
- Do not tolerance what the process cannot hold; ask the shop for achievable bend and laser tolerances.
