---
id: mai-blueprint-cad-engineering-practice
title: CAD Mühendislik Pratiği
type: blueprint
status: draft
version: 1.0.0
summary: CAD dosya formatları, adlandırma, revizyon yönetimi, konfigürasyonlar, montaj düzeni, yayın paketleri ve kütle özellikleri konusunda yönlendirme.
tags: [cad, solidworks, engineering, documentation]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
input_contract: CAD system and version, file types involved, goal (exchange, release, cleanup, naming), team/PDM situation
output_contract: recommendation with reasons, checklist, risks, next actions
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# CAD Mühendislik Pratiği

## Kapsam
Sac ve genel mekanik parçalar için CAD veri yönetimi ve modelleme pratiği: formatlar, veri aktarımı, adlandırma, referanslar, revizyon kontrolü, yayın paketleri, içe aktarılmış geometri.

## Gerekli girdiler
CAD system and version, file types involved, goal (exchange, release, cleanup, naming), team/PDM situation

## İş akışı
1. Amacı belirle: tedarikçiyle veri aktarımı, üretime yayın, montaj temizliği, adlandırma/revizyon düzeni, içe aktarılmış geometri.
2. CAD sistemini/sürümünü, alıcı tarafı ve PDM olup olmadığını sor.
3. Formatı `knowledge/09`a göre seç (3B için STEP, düz profil için DXF, resim için PDF); tek formata güvenme.
4. Model, resim, DXF ve ürün ağacında adlandırma, referans, birim ve revizyon tutarlılığını kontrol et.
5. Yayın paketi kontrol listesi ve kalan riskleri ver (sürüm, birim, konfigürasyon).
6. Gerçek dosyalar açılmadan doğrulanamayanları belirt.

## Gerekli kontroller
- Aktarılan her dosyada birim (mm) teyit edildi.
- Model, resim, DXF ve ürün ağacında revizyon aynı.
- Yerel sürücü referansı yok; göreli yol veya Pack and Go.
- Başka sistemlerle paylaşılan adlarda Türkçe karakter ve boşluk yok.

## Çıktı biçimi
Öneri · kontrol tablosu (madde · durum · not) · riskler · sonraki adımlar.

## Test senaryoları
1. Tedarikçi CAD dosyası istiyor → aynı revizyonda STEP + DXF + PDF önerir, hangi CAD/sürüm kullandıklarını sorar.
2. STEP içe aktarılıp açınım alınacak → kalınlık, birim kontrolü, yerel sac olarak yeniden kurma; açınım sonucuna körü körüne güvenmez.
3. 'parça son hali (2) ÇALIŞMA.sldprt' dosya adı → numaralandırma düzeni önerir, özel karakter uyarısı yapar.
