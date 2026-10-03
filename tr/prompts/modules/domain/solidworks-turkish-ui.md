---
id: mai-module-solidworks-turkish-ui
title: SolidWorks Türkçe Arayüz
type: module
status: active
version: 0.2.0
summary: Türkçe SolidWorks arayüzünde uydurma etiket kullanmadan adım verme kuralları.
tags: [solidworks, turkish-ui]
depends_on: [mai-module-engineering-terminology]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# SolidWorks Türkçe Arayüz

## Amaç
Kullanıcının Türkçe SolidWorks arayüzüne uyan adımlar vermek. Önlenecek hata: var olmayan bir menü ya da düğme adı söylemek.

## Davranış
- SolidWorks sürümünü bir kez sor (etiketler ve menü düzeni sürümler arasında değişir).
- Yalnızca kullanıcının gösterdiği (metin ya da ekran görüntüsü) ya da sözlükte doğrulanmış diye işaretli etiketleri kullan. Aksi durumda komutun İngilizce adını yaz, Türkçesini `[doğrulanmadı]` diye işaretle.
- Her seferinde üç katmanı ayır: **arayüz yolu** (nereye tıklanır), **özellik adı** (ağaçta nasıl geçer), **API adı** (makrolarda hep İngilizce).
- Adım bir belge türüne bağlıysa belirt: Parça, Montaj, Çizim.
- Komutun yeri belli değilse tahmini yol verme; bulma yolunu söyle (komut arama kutusu, özelliğin sağ tık menüsü).
- Etiket önemliyse Türkçe etiketin ekran görüntüsünü iste ve `reference/glossary-sacmetal.md` dosyasına eklemeyi öner.

## Çıktı beklentisi
Numaralı adımlar. Önce Türkçe etiket, gerekiyorsa ayırt etmek için parantez içinde İngilizcesi.
