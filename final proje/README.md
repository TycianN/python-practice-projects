# Listly

Listly, alışveriş listeleri oluşturup yönetmek için hazırlanmış bir masaüstü uygulamasıdır. Ürün ekleyebilir, miktarlarını değiştirebilir, listeleri kaydedebilir ve geçmiş listeleri görüntüleyebilirsin.

## Özellikler

- Alışveriş listesine ürün ekleme, miktarını artırma/azaltma ve ürünü silme
- Listeleri tarih bilgileriyle kaydetme ve geçmiş listeleri açma
- Listeleri JSON olarak uygulama klasöründe saklama
- Listeleri ayrıca `.txt` dosyası olarak seçtiğin klasöre kaydetme
- İsteğe bağlı profil bilgileri: ad, soyad, yaş ve şehir
- Koyu temalı grafik arayüz

## Çalıştırma

Projeyi Python ile çalıştırmak için `Listly_GUI.py` dosyasını aç. Uygulama `customtkinter` ve `Pillow` paketlerini kullanır; bunlar kurulu değilse önce yükle:

```bash
python -m pip install customtkinter pillow
```

Ardından proje klasöründe:

```bash
python Listly_GUI.py
```

Windows için derlenmiş uygulama `dist/Listly.exe` içinde bulunur.

## Verilerin saklanması

Uygulama kullanıcı verilerini çalıştırıldığı yerdeki dosyalara kaydeder:

- `Listly_Ayarlar.json`: profil bilgileri ve seçilen kayıt klasörü
- `Alisveris_Sepeti.json`: kaydedilen alışveriş listeleri
- Seçilen klasörde `Alisveris_Listesi_*.txt` dosyaları: metin dışa aktarımları

## Gizlilik notu

Profil bilgileri ve alışveriş listeleri bilgisayarında yerel dosyalara kaydedilir. Bu dosyaları GitHub'a yükleme veya başkalarıyla paylaşma; içlerinde kişisel bilgiler ya da özel olabilecek alışveriş bilgileri bulunabilir. Bu dosyaları paylaşmadan önce içeriklerini kontrol et ve gerekirse kişisel verileri sil. Uygulama klasörünü veya seçtiğin kayıt klasörünü yedeklerken de aynı gizlilik önlemlerini uygula.
