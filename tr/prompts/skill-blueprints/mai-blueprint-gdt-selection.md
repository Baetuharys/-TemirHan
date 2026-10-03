---
id: mai-blueprint-gdt-selection
title: GD&T Seçimi
type: blueprint
status: draft
version: 1.0.0
summary: Fonksiyona dayalı, ölçülebilir ve aşırı olmayan geometrik tolerans ve datum seçimi.
tags: [technical-drawing, engineering]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary]
last_reviewed: 2026-10-02
input_contract: function, mating parts, process capability, standard
output_contract: table of frames with datums, modifiers and inspection notes
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# GD&T Seçimi

## Kapsam
Fonksiyonu ifade eden ve ölçülebilir geometrik tolerans ile datum seçimi; aşırı toleranslandırmadan kaçınma. Standart metninin yerine geçmez.

## Gerekli girdiler
Parça fonksiyonu, eşleşen parçalar, montaj yöntemi, ölçüm yöntemi, süreç kabiliyeti, geçerli standart (ISO 1101 veya ASME Y14.5), varsa mevcut resim.

## İş akışı
1. Her kritik özelliğin fonksiyonunu belirle (sızdırmazlık, geçme, bağlama, hizalama).
2. **Datum düzenini** parçanın nasıl bağlandığına ve ölçüldüğüne göre seç (kararlı yüzeyler, delik grupları); ince, rijit olmayan parçalar için tutma koşulunu belirt.
3. Her gereksinimi `knowledge/07` ile bir karakteristiğe eşle (düzlemsellik, paralellik, diklik, konum, profil…).
4. İşe yarayan en gevşek toleransı seç; süreç kabiliyetiyle karşılaştır (lazer ±0,1–0,2 mm, büküm açısı ±0,5°–1°).
5. Değiştirici (MMC/LMC/serbest durum) gerekçeli mi karar ver.
6. ISO 2768 genel tolerans sonuçlarını kontrol et.
7. Ölçüm yönteminin var olduğunu kontrol et.
8. Çerçeveleri datum referanslarıyla metin olarak ver.

## Gerekli kontroller
- Atıf yapılan her datum tanımlı.
- Datum sırası gerekçeli.
- Notsuz, sürecin tutamayacağı kadar sıkı tolerans yok.
- Standart (ISO/ASME) adlandırıldı; baskı doğrulanacak.

## Çıktı biçimi
Tablo: özellik · fonksiyon · karakteristik · tolerans · datumlar · değiştirici · ölçüm notu.

## Test senaryoları
1. 4 delikli montaj plakası → A|B|C datumlarına ⌀ bölgeli konum; MMC yalnızca boşluklu geçmede.
2. "1 m × 1,5 mm saçta düzlemsellik 0,05" talebi → gerçekçi/rijit değil diye işaretlenir; fonksiyon ve tutma koşulu sorulur.
3. Tanımsız "D" datumuna atıf yapan çerçeve → Hata olarak işaretlenir.
