# SolidWorks sheet-metal feature map (English names; verify Turkish labels in the user's interface)

| Need | Feature family (English) | Note |
|---|---|---|
| First body from a sketch | Base Flange/Tab | defines thickness and sheet-metal parameters |
| Add a wall on an edge | Edge Flange | flange position, length, relief options |
| Sloped/mitred flange along edges | Miter Flange | needs a sketch profile |
| Folded edge | Hem | types: closed, open, tear-drop, rolled |
| Offset step | Jog | |
| Bend along a sketch line | Sketched Bend | |
| Transition between profiles | Lofted-Bend | |
| Corners | Break-Corner / Corner-Trim, Closed Corner | |
| Emboss / louver | Forming Tool | library of forming tools |
| Solid to sheet metal | Convert to Sheet Metal / Insert Bends | works on suitable thin-walled solids |
| Flat pattern | Flatten / Flat-Pattern feature | the formed and flat states are shown through the feature or a flat-pattern configuration |
| Cut through bends | Normal Cut, or a normal cut in the sheet-metal context | |

## Names that often appear in the tree (default English interface)
Sheet-Metal1, Base-Flange1, Edge-Flange1, Flat-Pattern1, Process-Bends1 (naming varies by version).
Example from a user's Turkish template (SUPPLIED): a flat-pattern configuration named `VarsayılanSM-DÜZ-ÇOĞALTMA`, used both for a bounding box and for the drawing's flat view.

## Troubleshooting checklist
1. Is thickness the same on every flange? (a body from another thickness will not unfold)
2. Is the bend radius larger than the available flange or segment?
3. Do two flanges overlap or touch at a corner without a corner treatment?
4. Is the part really a sheet-metal body or a plain solid?
5. Is the rebuild error in the flat-pattern feature or in an earlier feature?
