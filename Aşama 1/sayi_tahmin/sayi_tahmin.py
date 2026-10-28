import random

tutulan_sayi = random.randint(1, 100)
deneme = 0

while True:
    try:
        tahmin = int(input("Lütfen 1-100 arası bir sayı tahmin ediniz: "))
    except ValueError:
        print("Hata! Lütfen sayı giriniz.")
        continue

    if not 1 <= tahmin <= 100:
        print("Sayı 1 ile 100 arasında olmalı!")
        continue

    deneme += 1

    if tahmin == tutulan_sayi:
        print(f"Doğru tahmin! Sayı {tutulan_sayi} idi. {deneme} denemede buldun.")
        break
    elif tahmin > tutulan_sayi:
        print("Daha küçük bir sayı dene!")
    else:
        print("Daha büyük bir sayı dene!")