---
id: mai-blueprint-solidworks-macro-generator
title: SolidWorks Makro Üretici
type: blueprint
status: draft
version: 0.2.0
summary: SolidWorks API makrolarını açık varsayımlar, hata yönetimi ve sınama planıyla yaz ve açıkla.
tags: [solidworks, macro, automation]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary, mai-module-solidworks-turkish-ui, mai-module-sheet-metal-domain]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# SolidWorks Makro Üretici

## Kapsam
Parça, montaj ve çizim otomasyonu için SolidWorks API kullanan VBA (istenirse .NET) makroları.

## Gerekli girdiler
SolidWorks sürümü, makronun çalışacağı belge türü, tam amaç, uyması gereken adlandırma kuralları (konfigürasyon adları, özel özellik adları), DEĞİŞMEMESİ gerekenler, örnek dosya ya da bir tanımı.

## İş akışı
1. Amacı yeniden yaz: girdi -> eylem -> çıktı -> dokunulmayanlar.
2. Kodun dayandığı varsayımları listele (örn. bir konfigürasyon adı var, bir özellik tanımlı). Her birini açık iletiyle çalışma anı denetimine çevir.
3. Makroyu yaz: `Option Explicit`, türlü değişkenler, `Nothing` dönebilen her API çağrısından sonra boşluk denetimi, kullanıcının durumunu (etkin konfigürasyon, yeniden oluşturma ayarı) geri getiren hata işleyici.
4. İş konfigürasyon ya da görünürlük değiştiriyorsa özgün durumu önce sakla ve çıkışta, hatada da, geri koy.
5. API üyesi uydurma. Kullanıcının sürümünde bir yöntemin var olduğundan emin değilsen söyle ve o sürümün SolidWorks API Yardımı'na yönlendir.
6. Sınama planı ver: önce bir kopyada, tek parçayla, sonra tüm montajla; her adımdan sonra nelere bakılacağı.
7. Nasıl çalıştırılacağını yalnızca doğrulanmış Türkçe etiketlerle anlat (makro araç çubuğu / Araçlar menüsü).

## Gerekli denetimler
- Özgün durum geri getirilmiş. - Kullanıcının vermediği sabit ad yok. - Hata iletileri neyin düzeltileceğini söylüyor. - Sürüme bağlı çağrılar işaretlenmiş.

## Çıktı biçimi
Amaç ve varsayımlar, kod bloğu, sınama planı, bilinen sınırlar.

## Sınama senaryoları
1. Montajdaki her sacmetal parçanın açınım konfigürasyonunu açıp sınırlandırıcı kutunun boy/en değerini okuyan ve her parçayı özgün konfigürasyonuna döndüren makro.
2. Montajdaki içe aktarılmış katı gövdeleri sacmetal parçaya dönüştüren makro: bir parçada dönüştürme başarısız olursa ne olacağını tanımlamalı (atla ve bildir; sessizce durma).
3. API'nin sunmayabileceği bir özellik isteyen istek: model emin olmadığını söylemeli ve denetleme yolunu vermeli.
