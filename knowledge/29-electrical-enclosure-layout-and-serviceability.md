---
id: mai-knowledge-enclosure-layout-serviceability
title: Electrical Enclosure Mechanical Layout and Serviceability
category: enclosures
evidence: engineering-practice
last_reviewed: 2026-10-02
verify_before_release: [electrical design authority requirements, equipment manufacturer clearances, wiring/bending space, thermal data, applicable safety standards]
maturity: implemented
source_ids: []
---

# Electrical Enclosure Mechanical Layout and Serviceability

This file covers **mechanical packaging**, not electrical code compliance.

## Mechanical layout priorities
- Mounting and removal path for every replaceable device.
- Tool access to screws/terminals/filters/fans.
- Cable routing without crushing or impossible bend paths.
- Door swing and equipment interference.
- Heat sources and airflow path.
- Separation of wet/dirty cable-entry zones from sensitive components where relevant.
- Space for labels, grounding/bonding hardware and maintenance.
- Lifting/transport loads and center of gravity.

## Do not invent electrical clearances
Creepage, clearance, protective bonding, conductor sizing and other electrical safety requirements depend on governing standards, voltage/system conditions and component data. Treat them as supplied/verified requirements from the electrical design authority, not generic AI rules.

## Serviceability review
Simulate: install, wire, inspect, replace filter/fan, remove mounting plate, open door fully, torque fasteners, clean/drain, and reassemble. A design that works only before wiring is not serviceable.
