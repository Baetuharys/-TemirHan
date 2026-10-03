---
id: mai-blueprint-solidworks-sheet-metal-workflow
title: SolidWorks Sac Metal İş Akışı
type: blueprint
status: draft
version: 1.0.0
summary: SolidWorks'te sac modelleme, açınım ve yayınlama için, arayüz etiketi uydurmadan yönlendirme.
tags: [solidworks, engineering]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary, mai-module-solidworks-turkish-ui]
last_reviewed: 2026-10-02
input_contract: SolidWorks version and language, goal, material, thickness, bend method
output_contract: numbered steps with UI path, feature name, API name and a verification step
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# SolidWorks Sac Metal İş Akışı

## Kapsam
Kullanıcıyı SolidWorks'te bir sac parçanın modellenmesi, açınımı ve yayınlanması boyunca yönlendirir; İngilizce ya da Türkçe arayüzde, arayüz etiketi uydurmadan.

## Gerekli girdiler
SolidWorks sürümü ve arayüz dili, parça geometrisi veya hedef, malzeme, kalınlık, büküm yöntemi (K faktörü/büküm tablosu/gauge tablosu), sonraki çıktı (resim, DXF, montaj).

## İş akışı
1. Sürümü ve dili bir kez sor (`knowledge/04`).
2. Başlangıcı seç: Base Flange/Tab (yerel) veya Convert to Sheet Metal (içe aktarılmış katı).
3. `Sheet-Metal` parametrelerini ayarla: kalınlık, varsayılan yarıçap, büküm yöntemi, otomatik boşaltma.
4. Özellikleri üretime uygun sırayla ekle (flanşlar → köşeler → kıvrımlar → kesimler → form takımları → bağlantı elemanı delikleri) (`knowledge/03`).
5. Düzleştir; `knowledge/03` hata tablosuyla teşhis et.
6. Özel özellikleri gir; resmi (bükülü + açınım görünüşleri) oluştur ve DXF'i dışa aktar.
7. Her adımı İngilizce komut adıyla ver; Türkçe etiketi **yalnızca V/C seviyesindeyse** yaz, değilse `[doğrulanmadı]` ve komutu nasıl bulacağını ekle.

## Gerekli kontroller
- Yöntem (K faktörü/tablo) atölyeyle uyumlu.
- Büküm geçen kesimlerde gerekirse Normal Cut kullanıldı.
- DXF dışa aktarma seçenekleri büküm çizgilerini bilinçli olarak içeriyor/dışlıyor.
- Uydurma menü yolu yok.

## Çıktı biçimi
Üç katmanlı (arayüz yolu · özellik adı · gerekiyorsa API adı) numaralı adımlar ve sonda bir doğrulama adımı.

## Test senaryoları
1. "Edge Flange'in Türkçe adı ne?" → İngilizce ad + [doğrulanmadı] + nasıl aranacağı; ekran görüntüsü ister.
2. Düzleştirme başarısız → hata metnini ister; olası nedenleri sırayla listeler.
3. Sürüm verilmemiş → adımlardan önce sürüm ve dili sorar.
