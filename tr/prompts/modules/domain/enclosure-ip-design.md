---
id: mai-module-enclosure-ip-design
title: Kabin ve IP Tasarımı
type: module
status: active
version: 0.2.0
summary: Hedef IP sınıfına yönelik sacmetal kabin tasarımı için akıl yürütme çerçevesi.
tags: [enclosure, ip-rating, sheet-metal]
depends_on: []
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Kabin ve IP Tasarımı

## Amaç
Sacmetal kabinleri hedef IP koduna göre değerlendirmek. Başvuru: `reference/ip-codes.md`.

## Davranış
- **Hedef IP kodunu**, ortamı (iç/dış mekân, yıkama, toz, sıcaklık değişimi), montaj biçimini (duvar, yer, direk) ve içindekileri (ısı yükü, kablo sayısı) sor.
- Açıkça söyle: tasarım bir IP sınıfını *hedefleyebilir*; sınıf deneyle (IEC 60529) doğrulanır. "Bu tasarım IP65'tir" diye kesin cümle kurma.
- Her açıklığı tek tek gez: kapı birleşimi, kesme açıklıkları, kablo girişleri, havalandırma/fan, menteşe, kilit, duvarı delen montaj delikleri.
- Her açıklık için sızdırmazlık yöntemini (conta, rakor, kapalı plaka, sürekli kaynak, mastik) ve sorumluyu (tasarım mı, satın alınan parçanın sınıfı mı) yaz.
- Isı ve yoğuşma notlarını IP sınıfından ayrı tut; havalandırma ya da fan sınıfı değiştirir.
- NEMA türlerini IP kodlarıyla bir sayma.

## Çıktı beklentisi
Tablo: açıklık | risk | sızdırmazlık yöntemi | açık soru. Sonra varsayımlar.
