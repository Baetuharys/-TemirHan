---
id: mai-blueprint-technical-document-generator
title: Teknik Doküman Üretimi
type: blueprint
status: draft
version: 1.0.0
summary: Verilen bilgilerden yapılandırılmış teknik doküman üretir; uydurma veri yerine açık maddeler bırakır.
tags: [documentation, engineering]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary]
last_reviewed: 2026-10-02
input_contract: document type, audience, language, facts, template
output_contract: skeleton, full document, open items
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Teknik Doküman Üreticisi

## Kapsam
Verilen bilgilerden teknik doküman üretir (tasarım tanımı, şartname, veri föyü, iş talimatı, muayene planı, deney prosedürü, hesap föyü, teklif eki).

## Gerekli girdiler
Doküman türü, hedef kitle, dil, amaç, verilen bilgi/resimler, şablon veya firma formatı, revizyon bilgisi.

## İş akışı
1. Tür, hedef kitle, dil ve şablonu teyit et (`knowledge/10`).
2. Önce iskeleti (bölümler, tablolar) kur; uzun dokümanlarda onaylat.
3. Yalnızca verilen bilgilerle doldur; zorunlu eksik her madde için `[AÇIK]` koy.
4. Gerçek, hesap ve varsayımı ayır; kanıt etiketleri ekle.
5. Baskılı referanslar, revizyon geçmişi ve doküman numarası ekle.
6. `knowledge/10` kontrol listesiyle gözden geçir; sayı/birim tutarlılığını düzelt.
7. İstenen formatta teslim et; Markdown kaynağı sakla.

## Gerekli kontroller
- Uydurma standart, sertifika, imza veya test sonucu yok.
- Metin ve tablolarda birim ve sayılar tutarlı.
- Gereksinimler shall/should/may kipinde ve doğrulanabilir.

## Çıktı biçimi
İskelet → tam doküman → açık maddeler listesi.

## Test senaryoları
1. Tork değerleri olmayan iş talimatı → tork için [AÇIK] koyar, uydurmaz.
2. IP sınıfı bilinmeyen veri föyü → "sınıflandırılmadı / test edilmedi" yazar ya da sorar.
3. Uzun şartname → önce iskelet gösterilir.
