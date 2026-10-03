---
id: mai-blueprint-sheet-metal-manufacturability-check
title: Sac Metal Üretilebilirlik Kontrolü
type: blueprint
status: draft
version: 1.0.0
summary: Sac parçanın üretim için tasarım incelemesi; süreç adımına göre Hata/Risk/Öneri bulguları.
tags: [sheet-metal, engineering]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary, mai-module-sheet-metal-domain, mai-module-manufacturing-chain]
last_reviewed: 2026-10-02
input_contract: model/drawing, material, thickness, quantity, process
output_contract: findings table with location, class, fix and cost effect
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Sac Üretilebilirlik Kontrolü

## Kapsam
Bir sac parça veya montajın üretime/teklife çıkmadan önceki üretim-için-tasarım incelemesi. Atölyenin reddedeceği, yeniden fiyatlayacağı veya zorlanacağı özellikleri bulur.

## Gerekli girdiler
Model/resim, malzeme ve kalınlık, adet, süreç (lazer/punch/büküm/kaynak/boya), tolerans sınıfı, varsa atölye kabiliyet verisi.

## İş akışı
1. Kesim: asgari delik/oluk, köprü, köşe yarıçapı, kenar mesafeleri, yerleşime uygunluk.
2. Şekillendirme: yarıçap–takım, kenar boyu, delik–büküm mesafesi, boşaltma, büküm sırası ve çarpışmalar, geri yaylanma, tane yönü.
3. Birleştirme: kaynak erişimi ve çarpılma, bağlantı elemanı veri föyü sınırları, galvaniz/paslanmaz hususları.
4. Yüzey işlemi: kaplama kalınlığı–geçme, maskeleme, askı izi, tahliye delikleri.
5. Montaj/muayene: tolerans zinciri, datum erişilebilirliği.
6. Maliyet etkenleri: ek ayar, özel takım, ikinci operasyon.
7. Her bulguyu **Hata / Risk / Öneri** diye sınıflandır, yerini belirt, çözüm ver.

## Gerekli kontroller
- Pratik kurallar *tipik* diye etiketlenir; atölye değeri önceliklidir.
- Yeri olmayan bulgu yok.
- Parçayı reddedebilecek ilk süreç adlandırılır.

## Çıktı biçimi
Bulgu tablosu: # · yer · sınıf · bulgu · önerilen çözüm · maliyet/süre etkisi.

## Test senaryoları
1. 3 mm kalınlıkta, 8 mm kenarlı parça → Hata: kenar takım asgarisinden kısa (tipik).
2. Bükümden 2 mm uzakta oluk → mesafe kuralıyla Risk.
3. Malzemesiz talep → yargılamadan önce malzeme ve kalınlığı sorar.
