# Kişi Rehberi

Python öğrenirken pekiştirme amacıyla yaptığım, terminalde çalışan basit bir telefon rehberi.

## Ne yapıyor?
- **Kişi kaydeder:** İsim ve 11 haneli numara ister. İsim boşsa, sadece rakamdan oluşuyorsa ya da zaten kayıtlıysa uyarır. Numara geçersizse ya da başka birinde kayıtlıysa yine uyarır ve baştan sorar.
- **Arama yapar:** Rehberden isim seçerek ya da numara girerek arama yapar (arama tabii ki sahte, 2 saniye bekleyip "Cevap Vermedi" der).
- **Rehberi düzenler:** Kişinin ismini değiştirebilir, numarasını değiştirebilir ya da kişiyi silebilir.
- **Menüden kullanılır:** Her işlemden sonra ana menüye döner, 4 ile çıkılır.

## Kullanılan konular
- Sözlük (`dict`): isim anahtar, numara değer
- Sınıf ve metotlar (`class Telefon`)
- `while` döngüsü, `break`, `continue`
- `try/except` (menüde harf girilirse program çökmesin diye)
- `time.sleep`

## Nasıl çalıştırılır?
````
python kisi_rehberi.py
````

## Eksikleri
Rehber sadece program açıkken bellekte durur, kapatınca kayıtlar silinir. Dosyaya kaydetme (`json`) henüz öğrenmediğim konulardan, onu öğrenince ekleyeceğim.

## Notlarım
- En çok uğraştığım yer `rehber_duzenle` içindeki girintiler oldu. `break`'ten sonra yazılan kodun hiç çalışmadığını burada öğrendim.
- `raise` ile hata fırlatmayı denedim ama tekrar sorma mantığı için `print` + `continue` daha uygun çıktı.
