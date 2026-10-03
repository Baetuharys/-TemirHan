---
id: mai-blueprint-engineering-task-intake
title: Mühendislik Görev Alımı
type: blueprint
status: draft
version: 1.0.0
summary: Mühendislik talebini sınıflandırır, bloklayıcı eksikleri bulur ve doğru skill zincirine yönlendirir.
tags: [core, engineering]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary]
last_reviewed: 2026-10-02
input_contract: user request in any form (text, drawing, photo, files)
output_contract: task summary, known/missing inputs, skill chain, first questions
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Mühendislik Görev Alımı

## Kapsam
Her mühendislik talebinin ilk adımı: sınıflandır, eksikleri bul, doğru skill'e yönlendir. Görevi çözmez.

## Gerekli girdiler
Kullanıcının talebi (metin, resim, fotoğraf, dosya listesi).

## İş akışı
1. Görev ailesini belirle: büküm/açınım · kabin/IP · resim kontrolü · GD&T · ağırlık · maliyet/teklif · dökümantasyon · SolidWorks arayüz/makro · görselden ölçü · pazar araştırması · görsel üretim.
2. Bilinen verileri çıkar (malzeme, kalınlık, adet, süreç, standart, yazılım sürümü, termin).
3. Eksikleri listele; bloklayıcı/bloklamayan diye işaretle.
4. En fazla üç soru sor ya da etiketli varsayımla devam et.
5. Skill zincirini adlandır, ör. `ip-enclosure-design → enclosure-gasket-review → sheet-metal-manufacturability-check`.
6. Beklenen çıktıyı ve biçimini söyle.

## Gerekli kontroller
- Görev ailesi açıkça adlandırıldı.
- Bloklayıcı eksik varken işe başlanmadı.
- Gizli veri herkese açık yerlere kopyalanmadı.

## Çıktı biçimi
Görev özeti · Bilinen · Eksik (bloklayıcı/bloklamayan) · Önerilen skill zinciri · İlk soru(lar).

## Test senaryoları
1. "Kabin için IP65 lazım" → ortam, kapı tipi, kablo girişlerini sorar; kabin skill'lerine yönlendirir.
2. "Ölçüsü kaç?" yazılı fotoğraf → referans nesne ister; image-dimension-estimation'a yönlendirir.
3. Sürüm belirtilmeden "SolidWorks'te nasıl yaparım?" → sürümü ve arayüz dilini sorar.
