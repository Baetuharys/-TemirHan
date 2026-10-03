---
id: mai-skill-image-prompt-engineering
title: Image Prompt Engineering
status: active
version: 1.3.0
summary: Yapılandırılmış görsel üretim promptları oluşturur; amaç, konu, kompozisyon, kamera, ışık, malzeme, referanslar ve kısıtları ayrıştırır.
tags: [image, prompt, visual-generation, references, constraints]
depends_on: [mai-skill-engineering-task-intake]
name: image-prompt-engineering
description: Write precise image-generation prompts for engineering subjects: subject, view, materials, constraints, references and negative constraints. Use for görsel üretim promptu, prompt mühendisliği, referans rolleri.
---

# Image Prompt Engineering

## Amaç
Kullanıcının görsel üretim niyetini üretim aracından bağımsız, açık ve denetlenebilir bir prompt yapısına dönüştürmek.

## Prompt sırası
1. Intent / kullanım amacı
2. Subject / ana konu
3. Scene / bağlam
4. Geometry / biçim
5. Composition
6. Camera / viewpoint
7. Lighting
8. Materials / texture
9. Color
10. Text / labels
11. Reference images and their roles
12. Invariants / korunacaklar
13. Avoid / istenmeyenler
14. Output intent

## Kurallar
- Kullanıcı tarafından verilmemiş kritik geometrik ölçüleri uydurma.
- Referans görselin rolünü açıkça belirt: target, geometry, style, composition veya material reference.
- Düzenleme işlerinde değişmemesi gereken unsurları invariant olarak yaz.
- Kullanıcı ayrıntılı bir prompt verdiyse gereksiz yaratıcı ayrıntılar ekleme.
- Teknik görsellerde görsel doğruluk ile estetik iyileştirmeyi birbirinden ayır.
- Metin içeren görsellerde yazılacak metni aynen belirt; okunabilirlik garanti edilemiyorsa bunu belirt.
