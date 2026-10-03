---
id: mai-blueprint-weight-analysis
title: Ağırlık Analizi
type: blueprint
status: draft
version: 1.0.0
summary: Plaka, bitmiş parça ve CAD kütlesini yoğunluk kaynağı belirterek hesaplar ve çapraz kontrol eder.
tags: [analysis, engineering]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary]
last_reviewed: 2026-10-02
input_contract: material, thickness, geometry, cut-outs, hardware, coating
output_contract: table of formulas, inputs, results and labels
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Ağırlık Analizi

## Kapsam
Sac/levha parça ve montajların kütlesini hesaplar ve makullüğünü kontrol eder: satın alma için plaka kütlesi, sevkiyat için bitmiş parça kütlesi, CAD kütle özellikleriyle karşılaştırma.

## Gerekli girdiler
Malzeme ve kalite (yoğunluk kaynağı), kalınlık, geometri (alan veya ölçüler), kesikler, bağlantı elemanları, kaplama, adet.

## İş akışı
1. Ne istendiğini belirle: plaka kütlesi, bitmiş parça kütlesi, montaj kütlesi, sevkiyat kütlesi.
2. Yoğunluğu kaynağıyla seç (`knowledge/15`); paslanmazı çelikle aynı varsayma.
3. `m = V·ρ` (V m³, ρ kg/m³) veya `m = A·T·ρ` hesapla; yerine konan sayıları göster.
4. Kesikleri düş; bağlantı elemanı, kaynak, kaplamayı ayrı ekle ve tahmin diye etiketle.
5. CAD kütle özellikleriyle karşılaştır; farkı açıkla (yoğunluk, konfigürasyon, kaplama).
6. Büyüklük mertebesi kontrolü yap (mm başına kg/m²: çelik ≈ 7,85).
7. Sonucu birimiyle ve belirsizlik notuyla ver.

## Gerekli kontroller
- Birimler tutarlı (mm / m).
- Yoğunluk kalitesi gerçek kaliteyle uyumlu.
- Plaka kütlesi ile bitmiş parça kütlesi karıştırılmamış.

## Çıktı biçimi
Tablo: kalem · formül · girdiler · sonuç · etiket. Ardından notlar ve açık maddeler.

## Test senaryoları
1. 1 m × 2 m × 3 mm çelik levha → 47,1 kg `[HESAPLANAN]`.
2. Aynısı 1.4301'de → ρ ≈ 7930 kg/m³ ile ≈ 47,6 kg; yoğunluk kaynağını belirtir.
3. "Parça 5 kg" ama CAD 4,2 kg → konfigürasyon, yoğunluk, bağlantı elemanı, kaplamayı sorar.
