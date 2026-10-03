# Enclosure Design Pattern Library

These are **patterns to reason with**, not certified dimensions. Each pattern lists what problem it solves, what can fail, what information must be supplied, and how to verify it.

| Pattern | Use | Key checks |
|---|---|---|
| Folded return / door hem | stiffness, safer edge, gasket support | bend radius, clearance, drainage, coating |
| Continuous gasket land | ingress-control concept | continuous compression, corners, hardware spacing |
| Labyrinth overlap | reduce direct ingress path | drainage, capillary paths, service access |
| Removable gland plate | cable-entry serviceability | seal boundary, bonding, fastener access |
| Mounting plate | isolate internal equipment from shell | stiffness, earth/bonding requirement, access |
| Stiffener / return flange | panel rigidity | load path, weld distortion, fastener interference |
| Multi-point latch | distribute door compression | door flatness, gasket compression, latch access |
| Filtered ventilation | thermal management | IP trade-off, filter maintenance, pressure drop |
| Plinth / base | floor interface and cable space | lifting, anchoring, corrosion, drainage |

Use `skills/design-troubleshooter`, `skills/enclosure-gasket-review`, `skills/enclosure-thermal-review`, and `skills/ip-enclosure-design` to choose between patterns. Never infer an IP rating from the pattern alone.
