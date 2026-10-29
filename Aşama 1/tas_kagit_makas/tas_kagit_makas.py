import random
import time

secenekler = {1: "Taş", 2: "Kağıt", 3: "Makas"}
# anahtar, değeri yener
kazanma = {"Taş": "Makas", "Kağıt": "Taş", "Makas": "Kağıt"}

ai_skor = 0
kullanici_skor = 0

while True:
    ai_secim = random.choice(list(secenekler.values()))
    print("1-Taş / 2-Kağıt / 3-Makas")

    try:
        secim = int(input("Bir Seçim Yapınız: "))
    except ValueError:
        print("Lütfen sayı gir!")
        continue

    if secim not in secenekler:
        print("1, 2 veya 3 gir!")
        continue

    kullanici_secim = secenekler[secim]
    print(f"{kullanici_secim} Seçildi, AI Bekleniyor.")
    time.sleep(1.5)
    print(f"AI {ai_secim} Seçti.")
    time.sleep(1.5)

    if kullanici_secim == ai_secim:
        print("Berabere")
    elif kazanma[kullanici_secim] == ai_secim:
        print("Sen Kazandın!")
        kullanici_skor += 1
    else:
        print("AI Kazandı.")
        ai_skor += 1

    time.sleep(1)
    print("-------------")
    print(f"Skor Tablosu: Sen:{kullanici_skor} - AI: {ai_skor}")
    print("-------------")
    time.sleep(1.5)

    if kullanici_skor == 5 or ai_skor == 5:
        break

if kullanici_skor == 5:
    print("Oyunu sen kazandın!")
else:
    print("Oyunu AI kazandı!")