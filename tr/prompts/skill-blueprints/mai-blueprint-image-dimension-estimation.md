---
id: mai-blueprint-image-dimension-estimation
title: Görselden Boy/Ölçü Tahmini
type: blueprint
status: draft
version: 0.2.0
summary: Başvuru nesnesi kullanarak fotoğraftan parça boyutu kestir ve hata aralığını bildir.
tags: [visual-analysis, measurement]
depends_on: [mai-module-context-audit, mai-module-technical-verification, mai-module-no-fabrication, mai-module-action-summary, mai-module-uncertainty-management, mai-module-image-measurement]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Görselden Boy/Ölçü Tahmini

## Kapsam
Fotoğraf -> sınıflı, hata aralıklı boyut tahmini. Parça üretime gidecekse gerçek ölçümün yerini tutmaz.

## Gerekli girdiler
Fotoğraf, tahmin edilecek özellikler, fotoğrafta görünen boyutu bilinen bir başvuru (ya da bilinen standart parça), biliniyorsa kamera açısı.

## İş akışı
1. Fotoğrafı denetle: başvuru özellikle aynı düzlemde mi? Görünüm aşağı yukarı karşıdan mı? Kırpılmış yer var mı?
2. Başvuruyu ve boyutunu yaz. Boyut varsayıldıysa sonuçları, varsayımı adlandırarak Ölçekli tahmin diye sınıfla.
3. Ölçek = bilinen mm / bilinen piksel. Yalnızca o düzlemdeki özelliklere uygula.
4. Her özellik için değeri, sınıfı ve +/- hatayı ver (ana kaynağı adlandır: piksel okuma, eğiklik, mercek, başvuru boyutu).
5. Sayıları neyin daraltacağını yaz: karşıdan fotoğraf, çerçevede cetvel, kullanıcının ölçtüğü tek bir boyut.
6. Amaç üretimse kesimden önce gerçek ölçüm gerektiğini açıkça söyle.

## Gerekli denetimler
- Sınıfsız boyut yok. - Aralıksız tek sayı yok. - Başvuru adlandırılmış. - Eğiklik görünüyorsa perspektif uyarısı verilmiş.

## Çıktı biçimi
Tablo: özellik | değer | sınıf | başvuru | hata aralığı; ardından "bunu ne iyileştirir".

## Sınama senaryoları
1. Yanında cetvelle, karşıdan çekilmiş parça: küçük hatalı Ölçekli tahminler.
2. Eğik çekilmiş, başvurusuz parça: model sayı vermeyi reddetmeli, başvuru istemeli.
3. Özellikler başvurudan farklı derinlikte: model uyarmalı ve aralığı genişletmeli.
