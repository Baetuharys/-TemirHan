---
id: mai-blueprint-material-property-research
title: Mühendislik Malzeme Özellikleri Araştırması
type: blueprint
status: active
version: 0.2.0
summary: Research and normalize material properties for engineering calculations while separating standard data, manufacturer data, and assumptions.
tags: [materials, research, density, mechanical-properties]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---
# Mühendislik Malzeme Özellikleri Araştırması

## Amaç
Research and normalize material properties for engineering calculations while separating standard data, manufacturer data, and assumptions.

## Skill uygulaması
Bkz. `skills/material-property-research/SKILL.md`.

## Temel kurallar
- Eksik mühendislik veya ticari girdileri uydurma.
- Kaynak destekli veri, hesaplama, tahmin, mühendislik pratiği ve varsayımı birbirinden ayır.
- Doğrulama ve sonraki adımla bitir.
