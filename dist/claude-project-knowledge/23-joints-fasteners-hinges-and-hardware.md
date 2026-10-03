---
id: mai-knowledge-joints-fasteners-hardware
title: Joints, Fasteners, Hinges and Hardware
category: mechanical-design
evidence: engineering-practice
last_reviewed: 2026-10-02
verify_before_release: [joint loads, material/thickness, hardware manufacturer data, installation method, access and service conditions]
maturity: implemented
source_ids: []
---

# Joints, Fasteners, Hinges and Hardware

## Choose a joint by function
A joint may locate, clamp, carry shear/tension, transmit torque, seal, conduct/bond, allow service or permanently join. State which functions matter before choosing screws, PEM hardware, rivets, welds or adhesives.

## Selection questions
- Permanent or serviceable?
- One-sided access or two-sided access?
- Parent sheet thickness and material?
- Static, cyclic, vibration or impact load?
- Corrosion/galvanic environment?
- Is electrical bonding required?
- Appearance constraints?
- Installation equipment available?
- How many assembly cycles?

## Sheet-metal hardware checks
For self-clinching or rivet hardware, use the **manufacturer's current datasheet** for minimum sheet thickness, hole preparation, edge distance, installation force and material compatibility. Do not generalize values between families.

## Hinges and latches
Treat hinges and latches as part of the structural and sealing system. Check door center of gravity, opening angle, interference, sag, fastener load path, service removal, latch compression distribution and gasket reaction. More latches may improve compression distribution but also increase cost and user effort.

## Welded vs mechanical joint trade-offs
Welding can reduce part count but introduces heat distortion, finishing effort and repair difficulty. Mechanical fastening improves serviceability but adds holes, hardware, assembly time and possible ingress paths. Compare the complete system rather than unit hardware cost.

## Verification
Use manufacturer ratings and project load cases. For unfamiliar hardware, prototype pull-out/torque/service-cycle behavior in the actual sheet stack before release.
