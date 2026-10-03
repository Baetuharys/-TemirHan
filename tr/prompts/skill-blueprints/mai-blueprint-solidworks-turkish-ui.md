---
id: mai-blueprint-solidworks-turkish-ui
title: SolidWorks Türkçe Arayüz İş Akışı
type: blueprint
status: draft
version: 0.2.0
summary: Türkçe arayüzlü SolidWorks sorularını yalnızca doğrulanmış etiketlerle yanıtla.
tags: [solidworks, turkish-ui]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary, mai-module-solidworks-turkish-ui, mai-module-engineering-terminology]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# SolidWorks Türkçe Arayüz İş Akışı

## Kapsam
Türkçe arayüzlü SolidWorks'te Parça / Montaj / Çizim / Sacmetal işleri için nasıl-yapılır ve sorun giderme adımları.

## Gerekli girdiler
SolidWorks sürümü, belge türü, kullanıcının ne yapmak istediği, açık bir ekranı varsa ekran görüntüsü ya da etiketin tam metni.

## İş akışı
1. Belge türünü ve özellik ailesini belirle (sacmetal, montaj, çizim, API).
2. Terimi `reference/glossary-sacmetal.md` içinde ara. Doğrulanmış etiket -> kullan. `[doğrulanmadı]` -> komutun İngilizce adını ve bulma yolunu ver (komut arama kutusu, özelliğin sağ tık menüsü).
3. Numaralı adım ver; her adım nesneyi, eylemi ve ekranda beklenen sonucu söylesin.
4. Arayüz adımlarını API/makro seçeneğinden ayır.
5. "Doğrulanacak etiketler" ile bitir: kullandığın, doğrulanmamış Türkçe etiketler; kullanıcı ekran görüntüsü yollasın, sözlük güncellensin.

## Gerekli denetimler
- Uydurma menü yolu ya da düğme adı yok. - Sürüm yazılmış ya da sorulmuş. - Doğrulanmamış etiketler sonda listelenmiş.

## Çıktı biçimi
Numaralı adımlar, ardından "Doğrulanacak etiketler".

## Sınama senaryoları
1. "Açınım komutu nerede?" ekran görüntüsüz: model tahmini Türkçe yol vermemeli; İngilizce adı ve bulma yolunu vermeli.
2. Kullanıcı bir Türkçe etiket yapıştırır: model onu olduğu gibi kullanmalı.
3. Kullanıcı aynı işi makro olarak ister: model arayüz ve API katmanlarını ayrı tutmalı.
