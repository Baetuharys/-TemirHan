---
id: mai-blueprint-quotation-generator
title: Üretim Teklif Oluşturucu
type: blueprint
status: active
version: 0.2.0
summary: Convert a reviewed manufacturing scope and cost basis into a structured technical-commercial quotation without inventing commercial assumptions.
tags: [quotation, cost, commercial, manufacturing]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---
# Üretim Teklif Oluşturucu

## Amaç
Convert a reviewed manufacturing scope and cost basis into a structured technical-commercial quotation without inventing commercial assumptions.

## Skill uygulaması
Bkz. `skills/quotation-generator/SKILL.md`.

## Temel kurallar
- Eksik mühendislik veya ticari girdileri uydurma.
- Kaynak destekli veri, hesaplama, tahmin, mühendislik pratiği ve varsayımı birbirinden ayır.
- Doğrulama ve sonraki adımla bitir.
