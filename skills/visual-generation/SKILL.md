---
id: mai-skill-visual-generation
title: Visual Generation Orchestrator
status: active
version: 1.3.0
summary: Görsel üretim, düzenleme ve mühendislik görselleştirmesi için doğru alt skill'i seçer.
tags: [image, generation, orchestration, routing]
depends_on: [mai-skill-image-prompt-engineering, mai-skill-image-editing, mai-skill-engineering-visualization]
name: visual-generation
description: Orchestrate visual generation tasks: choose between prompt engineering, editing, reference analysis and engineering visualization, and verify the result against invariants. Use for görsel üretim, kapak/illüstrasyon, teknik görsel iş akışı.
---

# Visual Generation Orchestrator

## Routing
- Yeni görsel → image-prompt-engineering
- Mevcut görsel düzenleme → image-editing
- Çoklu referans → reference-image-analysis + image-prompt-engineering
- CAD/teknik çizim/sketch → engineering-visualization
- İterasyon → önceki prompt + değişiklik listesi + invariant kontrolü

## Genel çıktı
Amaç, referans rolleri, üretim promptu, korunacaklar, kaçınılacaklar ve doğrulama maddeleri.
