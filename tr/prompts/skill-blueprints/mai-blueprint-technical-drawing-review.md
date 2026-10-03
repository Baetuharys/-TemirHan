---
id: mai-blueprint-technical-drawing-review
title: Teknik Resim Gözden Geçirme
type: blueprint
status: draft
version: 0.2.0
summary: Bir çizimi görünümler, ölçüler, toleranslar, notlar, antet ve revizyon bilgisi açısından gözden geçir.
tags: [technical-drawing, documentation]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary, mai-module-engineering-terminology]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Teknik Resim Gözden Geçirme

## Kapsam
2B bir çizimin (PDF ya da görsel) eksiksizlik ve tutarlılık açısından gözden geçirilmesi. Parçayı yeniden tasarlamaz.

## Gerekli girdiler
Çizim, amaçlanan üretim yöntemi, varsa geçerli standart (bkz. `reference/standards-map.md`), biliniyorsa parçanın işlevi.

## İş akışı
1. Antet: parça numarası, ad, malzeme, kalınlık, revizyon, ölçek, kâğıt boyutu, izdüşüm yöntemi, genel tolerans notu (örn. ISO 2768 sınıfı), yüzey işlemi, birimler.
2. Görünümler: şekli tanımlamaya yetmeli; sacmetal parçada açınım görünümü olmalı; gerekli yerde kesit/ayrıntı görünümü.
3. Ölçüler: her özellik bir kez ve tam tanımlı; yinelenen ya da çelişen ölçü yok; fazla tanımlayan kapalı zincir yok; büküm ölçülerinin kuralı yazılmış.
4. Toleranslar: genel tolerans yazılmış; sıkı tolerans yalnızca işlevsel yerde; GD&T çerçeveleri tanımlı datumlara başvurmalı.
5. Notlar: büküm yarıçapı, K-faktörü/büküm tablosu başvurusu, çapak alma, yüzey işlemi, kaynak simgeleri, muayene gereksinimleri.
6. Sacmetale özgü: büküm çizgileri yön, açı ve yarıçapla işaretli; büküm sayısı açınım görünümüyle uyuşuyor.
7. Bulguları sınıfla: **Hata** (yanlış ya da eksik, üretimi durdurur), **Risk** (belirsiz), **Öneri**.

## Gerekli denetimler
- Bulgular çizimde tam yeri gösterir. - Standardı ve doğrulanacak sürümü anmadan madde alıntılanmaz. - Görselden okunan değerler öyle işaretlenir.

## Çıktı biçimi
Bulgu tablosu: # | yer | sınıf | bulgu | önerilen düzeltme.

## Sınama senaryoları
1. Genel tolerans notu olmayan çizim: nedeniyle Hata ya da Risk diye işaretlenmeli.
2. Bükümlü parçada açınım görünümü yok: işaretlenmeli.
3. Okunaksız tarama: model tahmin etmek yerine hangi değerleri okuyamadığını söylemeli.
