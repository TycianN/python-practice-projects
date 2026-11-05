# Modüler Hesap Makinesi v2

## Ne yapıyor?
Terminalde çalışan, renkli ve animasyonlu bir hesap makinesi. Toplama, çıkarma, çarpma ve bölme fonksiyonları ayrı bir dosyada (`islemler.py`, kendi modülüm), ana dosya (`main.py`) onları çağırıyor. `*args` sayesinde istediğim kadar sayıyla işlem yapabiliyorum.

## Nasıl kullanılır?
1. `pip install colorama` ile colorama'yı kur.
2. `islemler.py` ve `main.py` aynı klasörde olsun.
3. `python main.py` ile çalıştır.
4. Menüden işlem simgesini (`+`, `-`, `*`, `/`) yaz, sonra sayıları aralarında boşluk bırakarak gir. Mesela `2 5 10`.
5. Çıkmak için `0` yaz.

## Kullanılan konular
fonksiyonlar, `*args`, sözlükle işlem seçimi, modül oluşturma, `try/except`, `while` döngüsü, `colorama` ile renkli çıktı

## Notlarım
- Çıkarma ve bölmede ilk sayıdan başlıyor: `10 3 2` girersem `10 - 3 - 2` yapıyor.
- Sıfıra bölmede program çökmüyor, uyarı yazısı dönüyor.
- Yanlış simge, harf ya da boş giriş yapınca da çökmüyor, uyarı verip menüye dönüyor.
- Ekran temizleme işletim sistemine göre kendisi seçiliyor (Windows: `cls`, Mac/Linux: `clear`).
- Bölme sonucu ondalıklı çıkıyor (`10.0` gibi), çünkü sayıları `float` yapıyorum.
- Yapılacak: sıfıra bölmeyi yazı döndürmek yerine hata fırlatıp (`raise`) ana dosyada yakalamak.
