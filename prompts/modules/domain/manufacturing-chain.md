---
id: mai-module-manufacturing-chain
title: Manufacturing Chain
type: module
status: active
version: 1.0.0
summary: Connect design decisions to downstream manufacturing.
tags: [manufacturing,dfm]
depends_on: []
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Manufacturing Chain

## Purpose
Connect every design decision to the downstream process it affects.

## Chain
Material → Cutting (laser/punch/plasma/waterjet) → Deburring → Forming (bending, rolling, forming tools) → Joining (welding, self-clinching, rivets, screws) → Finishing (powder coat, galvanising, passivation, anodising) → Assembly → Inspection → Packing/Logistics.

## For any design decision ask
| Step | Question |
|---|---|
| Material | Is the grade/thickness stocked and certified as required? |
| Cutting | Min. hole/slot, web, kerf, nesting, edge quality, DXF layers? |
| Forming | Radius vs tooling, flange length, hole-to-bend, sequence, springback? |
| Joining | Access, distortion, seam type, hardware datasheet limits? |
| Finishing | Coating thickness effect, masking, hanging marks, galvanic pairs? |
| Assembly | Tolerance stack, fastener access, gasket compression? |
| Inspection | How is each critical dimension measured? Datum reachable? |
| Cost | Which choice adds a setup, a tool or a secondary operation? |

## Rule
A design review that does not name the downstream effect is incomplete. Name the *first* process that could reject the design.
