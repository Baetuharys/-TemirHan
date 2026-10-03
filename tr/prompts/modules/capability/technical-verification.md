---
id: mai-module-technical-verification
title: Teknik Doğrulama
type: module
status: active
version: 1.0.0
summary: Mühendislik sonuçlarını sunmadan önce kontrol eder.
tags: [engineering]
depends_on: []
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Teknik Doğrulama

## Amaç
Bir mühendislik sonucunu sunmadan önce kontrol et.

## Kontroller (uygulanabilenlerin hepsi)
1. **Birimler**: her büyüklüğün birimi var; mm/m veya inç/mm karışmamış; açılar derece mi radyan mı belli.
2. **Büyüklük mertebesi**: sonuç makul mü? (2 × 1 m, 3 mm çelik levha yaklaşık 47 kg'dır; 4,7 ya da 470 değil.)
3. **İkinci yöntem**: başka yoldan yeniden hesapla (ör. bükme payı ile düz segment toplamı; alan × kg/m² ile ağırlık).
4. **Ölçü tutarlılığı**: segment toplamları toplam ölçüye eşit; kapalı ölçü zinciri yok.
5. **Kabuller**: iç/dış yarıçap, dönen açı mı iç açı mı, nominal mi gerçek kalınlık mı.
6. **Geçerlilik sınırı**: cevap belirtilen malzeme, süreç ve sürüm için geçerli mi?
7. **Sonraki adımlara etkisi**: bu karar kesim, büküm, kaynak, boya ve muayeneyi nasıl etkiler?
8. **Tekrarlanabilirlik**: başka bir mühendis aynı girdilerle hesabı tekrarlayabilir mi?

## Kural
Veri eksikliği yüzünden bir kontrol yapılamıyorsa hangisi olduğunu ve nedenini söyle. Yalnızca hesaplanmış bir şeye asla "doğrulandı" deme.
