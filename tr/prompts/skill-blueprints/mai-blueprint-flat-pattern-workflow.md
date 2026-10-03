---
id: mai-blueprint-flat-pattern-workflow
title: Açınım İş Akışı
type: blueprint
status: draft
version: 1.0.0
summary: Bükülü sac modelden doğrulanmış açınım ve DXF'e giden akış: K faktörü/büküm tablosu uyumu, boşaltma, büküm çizgileri.
tags: [sheet-metal, engineering]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary, mai-module-sheet-metal-domain, mai-module-manufacturing-chain]
last_reviewed: 2026-10-02
input_contract: model/drawing, material, thickness, radii, bend method, process
output_contract: findings table, expected flat dimensions, open items
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Açınım İş Akışı

## Kapsam
Bükülü sac modelden güvenilir bir açınıma ve DXF'e giden yol. Düzleştirme kontrolleri, K faktörü/büküm tablosu uyumu, boşaltma, büküm çizgileri, sınırlayıcı kutu.

## Gerekli girdiler
Model veya resim, malzeme ve kalınlık, iç yarıçaplar, büküm yöntemi (K faktörü / büküm tablosu / pay), kesim süreci, levha formatı.

## İş akışı
1. Malzeme, kalınlık, yarıçap ve **atölyenin** kullandığı büküm yöntemini teyit et; yalnızca CAD'e güvenme.
2. Düzleştir ve hataları kontrol et (çakışma, başarısız büküm, eksik boşaltma, kapalı köşe).
3. Özellik–büküm mesafelerini kontrol et (`knowledge/01`, `knowledge/02`).
4. Bir iki büküm için beklenen düz boyu elle hesapla (`knowledge/02`).
5. Sınırlayıcı kutuyu levha formatı ve yerleşimle karşılaştır.
6. Büküm çizgilerini ayrı katmanda hazırla; işaretleme geometrisine karar ver.
7. Yöntemi ve revizyonu resim notuna yaz; DXF'i dışa aktar; aç ve incele.
8. Seri üretimden önce deneme bükümü öner.

## Gerekli kontroller
- K faktörü veya büküm tablosu kaynağı kayıtlı.
- Birim mm, ölçek 1:1.
- Büküm çizgileri kesim çizgisi değil.
- Bükümün yanındaki delik/oluk bozulması dikkate alındı.

## Çıktı biçimi
Bulgu tablosu (madde · durum · not) · beklenen açınım ölçüleri · açık maddeler.

## Test senaryoları
1. K faktörü verilmemiş → kaynağını sorar; etiketli tahmin aralığı sunar.
2. 2 mm sacta bükümden 3 mm uzakta delik → mesafe kuralıyla risk olarak işaretlenir.
3. Büküm çizgileri kesim katmanında olan DXF → Hata olarak işaretlenir.
