---
id: mai-module-manufacturing-chain
title: Üretim Zinciri
type: module
status: active
version: 1.0.0
summary: Tasarım kararlarını sonraki üretim adımlarıyla ilişkilendirir.
tags: [engineering]
depends_on: []
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Üretim Zinciri

## Amaç
Her tasarım kararını etkilediği sonraki üretim adımına bağla.

## Zincir
Malzeme → Kesim (lazer/punch/plazma/su jeti) → Çapak alma → Şekillendirme (büküm, haddeleme, form takımları) → Birleştirme (kaynak, çakma bağlantı elemanı, perçin, vida) → Yüzey işlemi (toz boya, galvaniz, pasivasyon, eloksal) → Montaj → Muayene → Paketleme/Lojistik.

## Her tasarım kararında sor
| Adım | Soru |
|---|---|
| Malzeme | Kalite/kalınlık stokta ve istenen sertifikayla var mı? |
| Kesim | Asgari delik/oluk, köprü, kerf, yerleşim, kenar kalitesi, DXF katmanları? |
| Şekillendirme | Yarıçap–takım uyumu, kenar boyu, delik–büküm mesafesi, sıra, geri yaylanma? |
| Birleştirme | Erişim, çarpılma, kaynak tipi, bağlantı elemanı veri föyü sınırları? |
| Yüzey işlemi | Kaplama kalınlığının etkisi, maskeleme, askı izi, galvanik çift? |
| Montaj | Tolerans zinciri, cıvata erişimi, conta sıkışması? |
| Muayene | Kritik ölçü nasıl ölçülecek? Datum erişilebilir mi? |
| Maliyet | Hangi seçim yeni ayar, takım ya da ikinci operasyon ekliyor? |

## Kural
Sonraki adımdaki etkiyi söylemeyen tasarım incelemesi eksiktir. Tasarımı reddedebilecek *ilk* süreci söyle.
