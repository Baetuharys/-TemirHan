---
id: mai-blueprint-ai-training-curator
title: AI Eğitim Küratörü
type: blueprint
status: draft
version: 1.0.0
summary: Kütüphanenin eğitim varlıklarını derler, doğrular ve genişletir: SFT ve tercih veri setleri, değerlendirme senaryoları, RAG parçaları ve sistem istemleri.
tags: [training, evaluation, rag, documentation]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-uncertainty-management]
last_reviewed: 2026-10-02
input_contract: goal (add data, build eval, plan fine-tune, update RAG), source material, target provider (Claude or ChatGPT), data sensitivity
output_contract: validated dataset records or plan, with provenance and evaluation impact
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# AI Eğitim Küratörü

## Kapsam
`training/` bakımı: SFT sohbet örnekleri, DPO tercih çiftleri, otomatik kontrollü değerlendirme senaryoları, RAG parça üretimi, Claude ve ChatGPT sistem istemleri, veri yönetişimi.

## Gerekli girdiler
goal (add data, build eval, plan fine-tune, update RAG), source material, target provider (Claude or ChatGPT), data sensitivity

## İş akışı
1. Hedefi netleştir: yalnızca istem/skill, RAG veya ince ayar. İhtiyacı karşılayan en ucuz seçeneği öner (`training/README.md`).
2. Veri hassasiyetini kontrol et (`training/DATA-GOVERNANCE.md`): veri setlerinde müşteri resmi, adı, fiyatı veya kişisel veri yok.
3. Kayıtları yalnızca doğrulanmış kaynaktan yaz; her sayı hesaplanmış ya da kaynaklı; kanıtı etiketle.
4. Önce değerlendirme senaryolarını ekle/güncelle; her yeni davranışın en az bir must_include / must_not_match kontrollü senaryosu olsun.
5. `python scripts/validate_all.py` ve `python training/scripts/validate_dataset.py` çalıştır.
6. Neyin değiştiğini, kategori sayılarını ve hangi senaryoların kapsadığını raporla.

## Gerekli kontroller
- Veri seti kayıtları şemaya uyuyor.
- Yinelenen id veya istem yok.
- Sayısal cevaplar tekrarlanabilir.
- Gerçek müşteri verisi yok.

## Çıktı biçimi
Değişiklik özeti · kategori sayıları · doğrulama çıktısı · açık riskler.

## Test senaryoları
1. Müşteri çizimini veri setine ekle → gizli müşteri verisini eklemeyi reddeder; anonimleştirme önerir.
2. Verisiz ince ayar talebi → önce istem+RAG önerir; asgari veri boyutu ve değerlendirme planını listeler.
3. Uydurma K faktörlü yeni SFT kaydı → incelemede reddedilir.
