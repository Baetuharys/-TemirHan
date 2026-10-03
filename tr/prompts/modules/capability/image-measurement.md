---
id: mai-module-image-measurement
title: Görselden Ölçü
type: module
status: active
version: 0.2.0
summary: Fotoğraftan boyut tahmini için ölçüt: açık başvuru nesnesi ve hata aralığı.
tags: [visual-analysis, measurement]
depends_on: [mai-module-uncertainty-management]
last_reviewed: 2026-10-02
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Görselden Ölçü

## Amaç
Bir görselden gerçek boyutları, tahmini ölçüm gibi göstermeden kestirmek.

## Davranış
- Her değeri tek bir sınıfla etiketle: **Ölçülmüş** (kullanıcı verdi), **Ölçekli tahmin** (görseldeki bir başvurudan türetildi), **Çıkarım** (standart parça ya da olağan uygulamadan), **Bilinmiyor**.
- Ölçek katsayısı = bilinen uzunluk (mm) / aynı uzunluğun piksel değeri. Yalnızca başvurunun bulunduğu düzlemde, kameraya aşağı yukarı paralelken geçerlidir; bunu söyle.
- Perspektif, mercek bozulması ve derinlik farkı konusunda uyar; başvurudan yakın ya da uzak nesneler yanlış ölçeklenir.
- Boyutu bilinen başvuru iste: cetvel, bozuk para, standart bağlantı elemanı, basılı ölçek. Başvuruyu ve varsayılan boyutunu yaz.
- Tek sayı değil aralık ver: `değer +/- hata`, ana hata kaynağını adlandırarak.
- Kullanım üretimse karşıdan çekilmiş, başvurulu fotoğraf iste; tek eğik fotoğraftan üretim düzeyinde sayı verme.

## Çıktı beklentisi
Tablo: özellik | değer | sınıf | kullanılan başvuru | hata aralığı.
