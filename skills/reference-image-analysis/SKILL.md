---
id: mai-skill-reference-image-analysis
title: Reference Image Analysis
status: active
version: 1.3.0
summary: Bir veya daha fazla referans görseli amaçlarına göre sınıflandırır ve hangi bilginin hangisinden alınacağını tanımlar.
tags: [image, reference, analysis, geometry, style]
name: reference-image-analysis
description: Analyse reference images for geometry, scale and invariants before visual generation or measurement. Use for referans görsel analizi, ölçek/oran çıkarma.
---

# Reference Image Analysis

## Referans rolleri
- Target: üzerinde düzenleme yapılacak görsel
- Geometry: biçim/oran referansı
- Style: görsel dil, malzeme veya render karakteri
- Composition: yerleşim ve kadraj
- Material: yüzey/doku
- Text/Logo: korunacak marka veya yazı

## Kural
Bir referansın rolü belirtilmeden ondan bütün özellikleri kopyalamış gibi sonuç çıkarılmaz.

## Çıktı
Her referans için: rol, kullanılacak özellikler, korunacak özellikler, belirsizlikler.

## Knowledge to load
Paths are relative to the repository root.
- `knowledge/08-image-dimension-estimation.md`
