---
id: mai-skill-image-editing
title: Image Editing
status: active
version: 1.3.0
summary: Mevcut görseli düzenlerken korunacak ve değiştirilecek unsurları açıkça tanımlar.
tags: [image, editing, reference, invariants, compositing]
depends_on: [mai-skill-image-prompt-engineering, mai-skill-reference-image-analysis]
name: image-editing
description: Edit an existing image by stating what must be preserved and what may change (geometry, part count, hole positions, proportions, text/logo). Use for görsel düzenleme, mevcut resmi değiştirme, invariant kontrolü.
---

# Image Editing

## İş akışı
Target image → intended changes → invariants → references → edit prompt → visual verification.

## Invariant kontrolü
Özellikle mühendislik görsellerinde korunması gerekenler:
- ana geometri
- parça sayısı
- delik ve bağlantı konumları
- oranlar
- görünüş açısı
- logo/metin
- kablo/bağlantı noktaları

## Değiştirilebilir alanlar
- arka plan
- ışık
- malzeme görünümü
- yüzey dokusu
- renk
- kamera görünümü (kullanıcı izin verirse)
- çevresel bağlam

Geometrik değişiklik istenmiyorsa modelin yeni detay eklemesine izin veren belirsiz ifadeler kullanılmaz.
