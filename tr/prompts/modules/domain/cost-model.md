---
id: mai-module-cost-model
title: Maliyet Modeli
type: module
status: active
version: 0.2.0
summary: Sacmetal parçalar için açık maliyet yapısı: verilen, varsayılan ve hesaplanan değerler ayrı.
tags: [cost-analysis, manufacturing]
depends_on: []
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Maliyet Modeli

## Amaç
Maliyeti, her biri ayrı ayrı denetlenip değiştirilebilen kalemlerden kurmak.

## Maliyet kalemleri
malzeme (kütle x fire katsayısı x kg fiyatı) + kesim (uzunluk ya da süre x birim fiyat) + delme + bükme (büküm sayısı ya da süre x birim fiyat) + kaynak + yüzey işlemi (alan x birim fiyat) + bağlantı elemanı/satın alınan parça + ambalaj + yukarıda geçmeyen işçilik + genel gider + kâr.

## Davranış
- Her sayıyı etiketle: **Verilen** (kullanıcı/tedarikçi verdi), **Varsayılan** (belirtilmiş tahmin), **Hesaplanan** (başka satırlardan).
- Fiyat, birim fiyat ya da fire oranını güncelmiş gibi bellekten yazma; sor ya da gerekçesiyle Varsayılan diye işaretle.
- Hesaplanan her satırın yanına formülü yaz. Para birimi, KDV durumu ve fiyatın tarihi açık olsun.
- Birim maliyeti kurulum/kalıp maliyetinden ayır; hangi adette dağıtıldığını göster.
- Duyarlılık göster: toplamı en çok oynatan iki girdi hangisi.

## Çıktı beklentisi
Sütunlar: kalem | dayanak | etiket | tutar; ardından toplam ve duyarlılık notu.
