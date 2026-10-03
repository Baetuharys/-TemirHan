---
id: mai-blueprint-sheet-metal-bend-analysis
title: Sacmetal Büküm Çözümlemesi
type: blueprint
status: draft
version: 0.2.0
summary: Bükme payı, bükme düşümü ve düz uzunluğu hesapla; yapılamayacak bükümleri işaretle.
tags: [sheet-metal, bending]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary, mai-module-sheet-metal-domain]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Sacmetal Büküm Çözümlemesi

## Kapsam
Her seferinde bir parça ya da bir büküm: düz uzunluk, bükme payı/düşümü, yapılabilirlik uyarıları.

## Gerekli girdiler
Malzeme/kalite, T, R (iç), büküm açısı, K-faktörü kaynağı, ölçü kuralı (iç / dış / orta), varsa takım ya da atölye büküm tablosu.

## İş akışı
1. Bükümü geçen her uzunluğun ölçü kuralını doğrula.
2. K'yı verilen tablodan al; yoksa varsayılan K'yı ve kaynağını yaz, sonucu **Varsayılan** diye işaretle.
3. Hesapla: `BA = teta(rad) x (R + K*T)`, `OSSB = (R+T) x tan(teta/2)`, `BD = 2*OSSB - BA`.
4. Düz uzunluğu topla; her kesimi göster.
5. İşaretle: atölyenin desteklediğinden küçük R, büküm çizgisine yakın delik/oluk, kalıbın izin verdiğinden kısa kenar, büküm sırası çarpışmaları.
6. Sonucu birimiyle ver ve onu en çok değiştirecek tek girdiyi söyle.

## Gerekli denetimler
- İç ve dış yarıçap karışmamış. - Açı doğru birimde. - K-faktörü kaynağı yazılmış. - Kaynaksız en küçük uzaklık sayısı verilmemiş.

## Çıktı biçimi
Tablo: kesim | tür | uzunluk | BA/BD | not. Ardından uyarılar ve açık sorular.

## Sınama senaryoları
1. 2 mm çelik, R 2, 90 derece, K verilen tablodan: her terimi gösteren beklenen sonuç.
2. Aynı parça, K verilmemiş: model varsayımı belirtmeli, sessizce bir değer seçmemeli.
3. Büküm çizgisine 3 mm uzak delik: model bozulma riskini işaretlemeli, sınır uydurmak yerine atölye kuralını sormalı.
