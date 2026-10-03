---
id: mai-blueprint-market-intelligence
title: Pazar İstihbaratı ve Potansiyel Müşteri Araştırması
type: blueprint
status: active
version: 1.1.0
summary: Kanıta dayalı pazar, rakip, proje ve potansiyel müşteri araştırması için blueprint.
tags: [market-intelligence, market-research, business-development]
depends_on: [mai-module-context-audit, mai-module-source-validation, mai-module-uncertainty-management, mai-module-no-fabrication]
last_reviewed: 2026-10-02
input_contract: coğrafya, sektör/yetenek, firma kriterleri, proje/zaman aralığı, istenen çıktı
output_contract: kanıtları, tarihleri, belirsizlikleri ve araştırma açıklarını içeren yapılandırılmış bulgular
portability: provider-agnostic
adapter_support: [chatgpt, claude]
---

# Pazar İstihbaratı ve Potansiyel Müşteri Araştırması

## Kapsam
Türkiye ve kullanıcının açıkça istediği yakın pazarlarda mekanik/sac metal iş geliştirmesi için kamuya açık pazar sinyallerini araştırır.

## İş akışı
1. Coğrafya, sektör, yetenek ve zaman aralığını tanımla.
2. Birden fazla kaynak sınıfından adayları keşfet.
3. Firma kimliğini ve ticari rolünü doğrula.
4. Proje, sözleşme, yatırım ve satın alma sinyallerini araştır.
5. Kamuya açık müşteri/partner ilişkilerini araştır.
6. Firma dosyaları oluştur.
7. Kanıta dayalı potansiyel müşteri uyumunu belirle.
8. Kaynakları, tarihleri, kanıt derecelerini ve bilinmeyenleri raporla.

## Zorunlu kontroller
- Desteksiz müşteri veya sözleşme iddiası yok.
- Coğrafya sessizce genişletilmez.
- Güncel iddialar güncel kaynak gerektirir.
- Önemli iddialar mümkün olduğunda ikinci kaynakla doğrulanır.
- Gerçekler, kaynakta bildirilen iddialar ve çıkarımlar görünür biçimde ayrılır.
