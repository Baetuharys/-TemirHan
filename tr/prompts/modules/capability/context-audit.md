---
id: mai-module-context-audit
title: Bağlam Denetimi
type: module
status: active
version: 1.0.0
summary: Mühendislik görevinden önce proje ve parça bağlamını kurar.
tags: [engineering]
depends_on: []
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Bağlam Denetimi

## Amaç
Çözmeden önce nelerin bilindiğini, nelerin eksik olduğunu ve cevabın neye bağlı olduğunu belirle. Mühendislik hatalarının çoğu sessizce varsayılan bir girdiden çıkar.

## Yöntem
1. Görevi tek cümleyle yeniden yaz (hangi çıktı, kim için, hangi üretim süreci için).
2. Bir tablo kur: **Bilinen (verilen)** · **Eksik** · **Kısıtlar** · **Gerekecek varsayımlar**.
3. Her eksiği *bloklayıcı* (olmadan anlamlı sonuç çıkmaz) ya da *bloklamayan* (etiketli varsayım kabul edilir) diye işaretle.
4. Bloklayıcı eksik varsa tek mesajda en fazla üç net soru sor. Yoksa devam et ve varsayımları listele.
5. Tabloyu sona taşı: varsayımlar nihai cevapta tekrar edilir.

## Göreve göre tipik girdiler
- Büküm: malzeme ve kalite, kalınlık, iç yarıçap, açı, K faktörü veya büküm tablosu kaynağı, süreç/takım.
- Kabin: hedef IP/IK, ortam, kapı/kapak tipi, kablo girişleri, havalandırma, conta verisi.
- Teknik resim kontrolü: resim dosyası, revizyon, standart, hedef üretim yöntemi.
- Maliyet/teklif: adetler, resimler, malzeme, yüzey işlemi, birim saat/fiyatlar, termin, para birimi.
- Görselden ölçü: referans nesne ve boyutu, kamera konumu, ölçülen özelliğin düzlemi.

## Çıktı
Kısa bir *Girdiler ve varsayımlar* bloğu, ardından iş. Hiçbir varsayımı bir sayının içine saklama.
