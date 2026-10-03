---
id: mai-blueprint-cost-analysis
title: Maliyet Çözümlemesi
type: blueprint
status: draft
version: 0.2.0
summary: Sacmetal parça için etiketli girdilerle açık bir birim maliyet ve duyarlılık notu kur.
tags: [cost-analysis, manufacturing]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary, mai-module-cost-model, mai-module-sheet-metal-domain]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Maliyet Çözümlemesi

## Kapsam
Sacmetal parça ya da montajlar için birim ve parti maliyeti kestirimi. Çıktı kestirimdir, teklif değildir.

## Gerekli girdiler
Parça listesi ya da çizim, malzeme ve kg fiyatı (verilmiş), adet, işlem listesi (lazer, büküm, kaynak, yüzey), varsa atölye birim fiyatları, fiyat tarihi ve para birimi.

## İş akışı
1. Ham parça boyunu ve kütlesini hesapla (bkz. `reference/sheet-metal-formulas.md`); fire katsayısını uygula ve kaynağını yaz.
2. Maliyet modelindeki her kalemi doldur. Her sayıyı Verilen / Varsayılan / Hesaplanan diye etiketle.
3. Eksik birim fiyat: uydurma. Sor ya da gerekçe ve yerine konacak yolla Varsayılan diye işaretle.
4. Birim maliyeti kurulum/kalıptan ayır; dağıtımda varsayılan adedi göster.
5. Toplamı ve onu en çok oynatan iki girdinin duyarlılığını hesapla.
6. Sayı bir teklife girmeden önce doğrulanacakları listele.

## Gerekli denetimler
- Her fiyatın tarihi ve para birimi var. - Formüller görünür. - Varsayılan değerler sonda bir arada listelenmiş.

## Çıktı biçimi
Maliyet tablosu, toplam, duyarlılık, "doğrulanacaklar" listesi.

## Sınama senaryoları
1. Tüm birim fiyatlar verilmiş: tüm satırlar Verilen/Hesaplanan, Varsayılan yok.
2. Bükme birim fiyatı yok: model sormalı ya da Varsayılan diye işaretlemeli, bellekten doldurmamalı.
3. Adet 10'dan 1000'e değişir: model parça başına kurulum maliyetinin nasıl değiştiğini göstermeli.
