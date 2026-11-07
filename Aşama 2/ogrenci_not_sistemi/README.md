# Öğrenci Not Sistemi / Student Grade System

🇹🇷 [Türkçe](#-türkçe) | 🇬🇧 [English](#-english)

---

## 🇹🇷 Türkçe

### Ne yapıyor?
Terminalde çalışan, menülü ve renkli bir öğrenci not kayıt programı. Öğrencilerin adı ve notu kaydedilir, tam liste görüntülenir ve 50 ve üzeri alanlar "Geçenler", altında kalanlar "Kalanlar" olarak yan yana iki sütunda listelenir.

### Özellikler
- Ana menü (öğrenci ekle, tam liste, geçenler/kalanlar, çıkış)
- Aynı oturumda birden fazla öğrenci ekleme (e/h ile devam)
- Hatalı girişlere karşı koruma (sayı olmayan not, 0-100 dışı not, boş isim)
- Geçenler yeşil, kalanlar kırmızı, yan yana hizalı çıktı
- Renkli terminal arayüzü, ekran temizleme ve kısa bekleme efektleri

### Kullanılan konular
sözlük (dict), sınıf (class), `while` döngüsü, `try/except`, f-string, list comprehension, `zip_longest`, `colorama`, `os`, `time`

### Kurulum ve çalıştırma
```bash
pip install colorama
python ogrenci_not_sistemi.py
```

### Notlarım
- Sözlükte anahtar tektir, aynı isim tekrar girilirse eski not güncellenir
- Kayıt satırının döngüde nereye yazıldığı çok önemli; yanlış girinti veriyi kaybettiriyor
- `zip_longest` ile farklı uzunluktaki listeler yan yana yazdırılabilir

---

## 🇬🇧 English

### What does it do?
A colorful, menu-driven student grade tracker that runs in the terminal. It stores student names and grades, shows the full list, and splits students into "Passed" (50 and above) and "Failed" (below 50), displayed side by side in two columns.

### Features
- Main menu (add student, full list, passed/failed list, exit)
- Add multiple students in one session (continue with y/n)
- Input validation (non-numeric grade, grade outside 0-100, empty name)
- Passed in green, failed in red, aligned side by side
- Colored terminal UI with screen clearing and short delay effects

### Concepts used
dictionary, class, `while` loop, `try/except`, f-strings, list comprehension, `zip_longest`, `colorama`, `os`, `time`

### Installation and usage
```bash
pip install colorama
python ogrenci_not_sistemi.py
```

### My notes
- Dictionary keys are unique, so entering the same name again updates the old grade
- Where the save line sits inside the loop matters; wrong indentation loses data
- `zip_longest` lets you print lists of different lengths side by side