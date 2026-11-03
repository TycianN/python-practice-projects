import random

kelimeler = [
    "bilgisayar", "klavye", "program", "yazilim", "degisken",
    "fonksiyon", "algoritma", "internet", "tarayici", "sunucu",
    "veritabani", "dosya", "klasor", "ekran", "fare",
    "elma", "armut", "kiraz", "portakal", "karpuz",
    "kedi", "kopek", "aslan", "kartal", "balina",
    "istanbul", "ankara", "izmir", "antalya", "fethiye",
    "kitap", "defter", "kalem", "pencere", "merdiven",
    "deniz", "orman", "dag", "nehir", "ruzgar",
]

secilen_kelime = random.choice(kelimeler)
tahminler = []
hak = 6

while hak > 0:
    # 1. Ekranda gösterilecek yazıyı hazırla (e _ _ a gibi)
    gosterim = ""
    for harf in secilen_kelime:
        if harf in tahminler:
            gosterim += harf + " "
        else:
            gosterim += "_ "

    print("\n" + gosterim)
    print(f"Kalan hak: {hak}")
    print("Denenen harfler:", ", ".join(tahminler))

    # 2. Kazandı mı? Hiç _ kalmadıysa kazandı
    if "_" not in gosterim:
        print("Tebrikler, kazandın!")
        break

    # 3. Tahmin al ve kontrol et
    tahmin = input("Bir harf gir: ").strip().lower()

    if len(tahmin) != 1 or not tahmin.isalpha():
        print("Tek bir harf girmelisin.")
        continue

    if tahmin in tahminler:
        print("Bu harfi zaten denedin.")
        continue

    # 4. Tahmini işle
    tahminler.append(tahmin)

    if tahmin in secilen_kelime:
        print("Doğru!")
    else:
        hak -= 1
        print("Yanlış!")

# 5. Döngü bitti, hak sıfırsa kaybetti
if hak == 0:
    print(f"\nKaybettin! Kelime: {secilen_kelime}")