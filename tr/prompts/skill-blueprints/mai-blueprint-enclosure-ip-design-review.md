---
id: mai-blueprint-enclosure-ip-design-review
title: Kabin IP Tasarım İncelemesi
type: blueprint
status: draft
version: 0.2.0
summary: Sacmetal kabin tasarımını hedef IP koduna göre açıklık açıklık incele.
tags: [enclosure, ip-rating, sheet-metal]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary, mai-module-enclosure-ip-design, mai-module-sheet-metal-domain]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Kabin IP Tasarım İncelemesi

## Kapsam
Sacmetal kabinin hedef IP koduna göre tasarım incelemesi. Çıktı tasarım riskidir, belgelendirme değildir.

## Gerekli girdiler
Hedef IP kodu, ortam, montaj biçimi, kapı/birleşim anlatımı ya da model/çizim, kesme açıklıkları ve kablo girişleri listesi, satın alınan parçaların (rakor, anahtar, fan) kendi sınıfları.

## İş akışı
1. Hedefi ve her rakamın ne istediğini yeniden yaz (`reference/ip-codes.md`).
2. Tüm açıklık ve birleşimleri listele. Her biri için: sızdırmazlık yöntemi, sorumlu (tasarım / satın alınan parça), risk.
3. En zayıf öğeyi denetle: kabinin sınıfını en zayıf açıklığı sınırlar.
4. Kapı sızdırmazlığını denetle: conta türü, sıkışma durdurucusu, bindirme ya da dolambaç, menteşe yanı, kilit çekmesi.
5. Kaynak/birleşim kapanışını, boşaltma/havalandırma kararlarını ve bunların sınıfı nasıl değiştirdiğini denetle.
6. Gerekli deney ya da kanıtı (laboratuvar deneyi, tedarikçi belgeleri) ve tasarımın neyi öne sürüp süremeyeceğini yaz.

## Gerekli denetimler
- Hiçbir sınıfı elde edilmiş diye yazmaz. - Her açıklık listelenmiş. - Satın alınan parçaların sınıfları varsayılmamış, verilen bilgiden alınmış.

## Çıktı biçimi
Tablo: açıklık | risk | sızdırmazlık yöntemi | sorumlu | açık soru. Ardından "hedefler" düzeyinde kalan yargı cümlesi.

## Sınama senaryoları
1. IP65 hedefli, fanlı kabin: model fanın sınıfının kabini sınırladığını işaretlemeli.
2. IPx5 hedefinde aralıklı (dikişli) kaynak birleşimi: model işaretlemeli.
3. Kullanıcı "bu IP66 mı?" diye sorar: model tasarım amacı ve gereken deney açısından yanıtlamalı.
