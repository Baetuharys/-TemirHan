---
id: mai-blueprint-sheet-metal-terminology
title: Sac Metal Terminolojisi
type: blueprint
status: draft
version: 1.0.0
summary: Sac metal ve CAD terimlerini sabit bir terim seçim politikası ve sözlükle İngilizce–Türkçe çevirir ve açıklar.
tags: [terminology, sheet-metal, solidworks, turkish-ui]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
input_contract: term(s) or text to translate/explain, audience (shop floor, drawing, documentation, SolidWorks UI), language direction
output_contract: term table with preferred Turkish term, alternatives and notes; UI labels only at level V/C
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Sac Metal Terminolojisi

## Kapsam
EN-TR sac metal, CAD, GD&T, yüzey işlemi ve ticari terminoloji; `docs/terminology-policy.md` uygulanır: arayüz etiketi > standart terim > yerleşik atölye terimi > gerçekte kullanılan Öztürkçe sözcük > uydurma sözcük yalnızca işaretli öneri olarak.

## Gerekli girdiler
term(s) or text to translate/explain, audience (shop floor, drawing, documentation, SolidWorks UI), language direction

## İş akışı
1. Hedef kitleyi ve metnin kullanılacağı yeri belirle (arayüz adımı, resim notu, atölye talimatı, doküman).
2. Terimi `reference/glossary.csv` içinde ara; arayüz etiketleri için `reference/solidworks-ui-labels.csv` ve seviyesine (V/C/U) bak.
3. Politika sırasını uygula; yerleşik terimi önce ver, gerçekte kullanılıyorsa Öztürkçe karşılığı bir kez parantez içinde ver.
4. Belirsizlikleri işaretle (punta/nokta kaynağı; markup/margin; açınım/gelişim).
5. Terim yoksa söyle, `öneri` işaretli aday sun ve sözlüğe eklemeyi öner.
6. V seviyesi olmadan Türkçe SolidWorks etiketini doğrulanmış gibi sunma.

## Gerekli kontroller
- Her arayüz etiketinin seviyesi (V/C/U) var.
- Uydurma sözcükler `öneri` olarak işaretli.
- Karışan çiftler ayrıştırıldı.

## Çıktı biçimi
Tablo: EN · TR tercih edilen · alternatifler · kullanım yeri · not.

## Test senaryoları
1. Bend deduction Türkçe ne → bükme düşümü / bükme kesintisi; bağlama göre; arayüz iddiası yok.
2. Edge Flange Türkçe menü adı → U seviyesi: İngilizce ad, [doğrulanmadı], nasıl bulunacağı.
3. Punta kaynağı ile nokta kaynağı aynı mı → hayır; punta (tack) ile direnç nokta kaynağı farklı.
