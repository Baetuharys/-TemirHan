---
id: mai-blueprint-solidworks-dxf-release-check
title: SolidWorks DXF Yayın Kontrolü
type: blueprint
status: active
version: 0.2.0
summary: Review a SolidWorks sheet-metal DXF before laser/CAM release, including scale, geometry, cut/mark separation, and revision consistency.
tags: [solidworks, dxf, laser, release]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---
# SolidWorks DXF Yayın Kontrolü

## Amaç
Review a SolidWorks sheet-metal DXF before laser/CAM release, including scale, geometry, cut/mark separation, and revision consistency.

## Skill uygulaması
Bkz. `skills/solidworks-dxf-release-check/SKILL.md`.

## Temel kurallar
- Eksik mühendislik veya ticari girdileri uydurma.
- Kaynak destekli veri, hesaplama, tahmin, mühendislik pratiği ve varsayımı birbirinden ayır.
- Doğrulama ve sonraki adımla bitir.
