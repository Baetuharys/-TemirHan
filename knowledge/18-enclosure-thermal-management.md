---
id: mai-knowledge-enclosure-thermal
title: Enclosure Thermal Management
category: enclosures
evidence: formula-and-practice
last_reviewed: 2026-10-02
verify_before_release: [heat-load list, ambient range, altitude, ingress target, component derating, fan/filter curve]
maturity: implemented
source_ids: [IEC-60529-2.2]
---

# Enclosure Thermal Management

Thermal design and IP design interact. A fan opening can solve temperature and simultaneously create an ingress path.

## 1. Required inputs
- internal dissipated heat by component and duty cycle;
- maximum/minimum ambient temperature;
- allowable internal temperature and component derating limits;
- enclosure dimensions/material/color/location (indoor/outdoor, sun exposure);
- target IP/IK and contamination environment;
- altitude and airflow restrictions;
- available ventilation, heat exchanger or cooling options.

## 2. First-pass forced-air calculation
For sensible heat only:
`Vdot = P / (rho × cp × ΔT)`.
`tools/calculators/thermal.py` returns m³/h after unit conversion. It is a sizing **screen**, not a fan selection: filters, grilles, pressure drop, recirculation, altitude and fan curve must then be checked.

## 3. Passive cooling
Do not infer passive capacity from surface area alone without a heat-transfer model and installation conditions. Natural convection, radiation, wall mounting, solar load and internal hotspots matter.

## 4. IP-aware patterns
- filtered fans require a filter/grille system compatible with the target enclosure concept;
- vents/breathers are components with their own ratings and installation constraints;
- place inlet/outlet to create a real flow path, not a short circuit;
- avoid drain paths that bypass the protected boundary;
- maintain service access for filter replacement;
- do not call an assembly IP-rated because individual components have IP markings—final assembly verification still applies.

## 5. Deliverable
Return heat-load table, thermal assumptions, first-pass calculation, proposed architecture, ingress impact, component-selection inputs and test/measurement plan.
