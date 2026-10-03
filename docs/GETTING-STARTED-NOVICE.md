# Başlangıç Rehberi — Konuyu bilmiyorsan bile kullan

Bu kütüphaneyi kullanmak için sac metal, GD&T veya RAG bilmek zorunda değilsin. Yapay zekâya **sorunu normal Türkçe ile anlat**.

## 1. İlk kullanım
ChatGPT/Claude tarafında ilgili sistem talimatını kullan ve `dist/` altındaki uygun bilgi paketini ekle. Sonra ilk mesajında şunlardan bildiklerini yaz:

- Ne tasarlıyorsun? (kapı, kabin, braket, panel…)
- Parça ne yapmalı?
- Elinde ne var? (fotoğraf, STEP, SLDPRT, DXF, PDF, ölçü, malzeme…)
- Üretim nasıl olacak? (lazer, abkant, kaynak…)
- Seni şu an ne durduruyor?

Bilmediğin alanlara `bilmiyorum` yazabilirsin. Sistem bunları `[AÇIK]` olarak tutmalıdır; sayı uydurmamalıdır.

## 2. Atölyeni bir kere tanıt
`project-profiles/example-fabricator-profile.yaml` dosyasını kopyala ve bildiğin gerçek atölye verilerini doldur. Özellikle bend table/K-factor kaynağı, abkant takımları, stok malzemeler, lazer limitleri, kaynak/finish kabiliyeti ve SolidWorks sürümü çok değerlidir.

Bu profil sayesinde her soruda aynı bilgileri tekrar anlatmazsın ve AI “tipik değer” tahminine daha az ihtiyaç duyar.

## 3. Tasarımda takıldığında
`/design` veya normal cümle kullan:

> Kapı 900x600, 1.5 mm sac. Kilit kapatınca orta kısım esniyor. Kalınlığı artırmadan ne yapabilirim?

İyi bir cevap doğrudan “2 mm yap” dememeli. Yük yolunu, return/stiffener/latch dağılımını, imalat etkisini ve doğrulamayı karşılaştırmalıdır.

## 4. Teknik resim veya CAD kontrolü
Dosyayı ekle ve şunu iste:

> Bunu üretici gözüyle incele. Blocker/Risk/Improvement/Open item şeklinde yaz. Uydurma ölçü ekleme.

## 5. Fotoğraftan CAD
En iyi sonuç için fotoğrafta/çizimde en az bir güvenilir referans ölçü ver. Perspektif varsa 4 noktalı düzeltme gerekebilir. Çıkan DXF **taslak geometri** olarak kalır; kritik üretim ölçülerini doğrulamadan release etme.

## 6. Son kontrol
Üretime göndermeden önce `/release` çalıştır. Varsayımlar, revision, material, bend model, drawing/DXF, finish, hardware, IP/thermal iddiaları ve BOM uyumu kapatılmadan “hazır” denmemelidir.
