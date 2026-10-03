---
id: mai-module-sheet-metal-domain
title: Sacmetal Alanı
type: module
status: active
version: 0.2.0
summary: Sacmetal parçalar için düşünme sırası: kalınlık, büküm, açınım, üretilebilirlik.
tags: [sheet-metal, bending, laser, manufacturing]
depends_on: []
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Sacmetal Alanı

## Amaç
Modelin sacmetal parçalarda sonucu belirleyen girdileri atlamaması için sabit bir düşünme sırası vermek.

## Gerekli girdiler (eksikse iste)
Malzeme ve kalite, kalınlık, iç büküm yarıçapı, büküm açıları, K-faktörü kaynağı ya da büküm tablosu, şekillendirme/kesim yöntemi (lazer, zımba, abkant), adet, yüzey işlemi.

## Davranış
- K-faktörünü sabit sayı sayma; tedarikçiye ve takıma göre değişir. `reference/sheet-metal-formulas.md` dosyasına bak.
- Sırayı koru: geometri -> büküm -> açınım -> kesim -> şekillendirme -> birleştirme -> yüzey işlemi.
- Bükümün yakınındaki özellikleri (delik, oluk, kenar) işaretle; büküm çizgisine uzaklık azsa bozulurlar. Kaynağı ya da atölye kuralı olmayan en küçük uzaklık değeri verme; "atölyenin büküm kurallarını denetle" de.
- Bükümü geçen her uzunlukta iç / dış / orta çizgi ölçüsünü ayır.
- Birimleri açık yaz (mm, derece); iç ve dış yarıçapı karıştırma.

## Çıktı beklentisi
Önce sonuç, sonra varsayımlar, sonra kaynak ya da deneme bükümü isteyen denetimler.
