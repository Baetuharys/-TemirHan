---
id: mai-blueprint-laser-dxf-workflow
title: Lazer DXF İş Akışı
type: blueprint
status: draft
version: 1.0.0
summary: Kesim, işaretleme ve büküm katmanları ayrılmış temiz bir lazer kesim DXF'i hazırlar.
tags: [manufacturing, engineering]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary, mai-module-manufacturing-chain]
last_reviewed: 2026-10-02
input_contract: flat pattern, material, thickness, shop DXF rules, marking needs
output_contract: DXF checklist, layer table, open questions
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Lazer DXF İş Akışı

## Kapsam
Sac modelden lazer kesim (ve isteğe bağlı işaretleme/gravür) için DXF hazırlama; hataların atölyeye sızmasını önleme.

## Gerekli girdiler
Açınım veya eskiz, malzeme, kalınlık, makine/CAM gereksinimleri, işaretleme gereksinimleri (saplama, yazı, büküm çizgisi), adet.

## İş akışı
1. Atölyenin DXF gereksinimlerini teyit et (birim, sürüm, katman adları, çizgi tipleri, kontur kapatma toleransı).
2. Geometriyi katmanlara ayır: CUT (kes), MARK/ENGRAVE (işaretle), BEND (büküm; kesilmez), NOTES.
3. Konturları kontrol et: kapalı, çift çizgi yok, sıfır uzunluklu parça yok, CAM gerektiriyorsa spline dönüştürülmüş, asgari özellik boyutları (`knowledge/01`).
4. Yerleşimi kullanıcı yapıyorsa kerf ve parçalar arası köprüyü kontrol et.
5. İşaretleme özelliklerini (saplama konumu, parça no) ve kesimden süreç ayrımını kontrol et.
6. Dışa aktar; görüntüleyicide aç; toplam ölçüyü modelle karşılaştır.
7. Dosyayı parça no + revizyonla adlandır; resim revizyonuyla aynı tut.

## Gerekli kontroller
- Büküm çizgileri hiçbir zaman kesim katmanında değil.
- Birim mm, ölçek 1:1, orijin tanımlı.
- Gizli/çift öğe yok.
- İşaretleme kesimle karıştırılmamış.

## Çıktı biçimi
DXF kontrol listesi (madde · geçti/kaldı) · katman tablosu · atölyeye açık sorular.

## Test senaryoları
1. Saplama işaretleri kesim katmanıyla karışık → MARK katmanına ayrılır.
2. Dış konturda spline → atölye CAM'i polyline istiyorsa işaretlenir.
3. DXF ölçüsü modelin sınırlayıcı kutusundan farklı → Hata olarak işaretlenir.
