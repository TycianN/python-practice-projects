import os
from colorama import Fore, Style, init

init(autoreset=True)

KM_MIL = 0.621371
MIL_KM = 1.609344
KG_LB = 2.20462
LB_KG = 0.453592


def ekran_temizle():
    os.system("cls" if os.name == "nt" else "clear")


def menu_goster():
    print(Fore.MAGENTA + "--------------------------------------")
    print(Fore.CYAN + Style.BRIGHT + "1-Km -> Mil")
    print(Fore.BLUE + Style.BRIGHT + "2-Mil -> Km")
    print(Fore.MAGENTA + "--------------------------------------")
    print(Fore.CYAN + Style.BRIGHT + "3-°C -> °F")
    print(Fore.BLUE + Style.BRIGHT + "4-°F -> °C")
    print(Fore.MAGENTA + "--------------------------------------")
    print(Fore.CYAN + Style.BRIGHT + "5-Kg -> Lb")
    print(Fore.BLUE + Style.BRIGHT + "6-Lb -> Kg")
    print(Fore.MAGENTA + "--------------------------------------")
    print(Fore.CYAN + Style.BRIGHT + "7-Çıkış")


def yenile():
    # önceki çıktıyı sil, menüyü tekrar çiz
    ekran_temizle()
    menu_goster()


def sayi_al(mesaj):
    # virgüllü girişi de kabul et (5,5 -> 5.5)
    return float(input(Fore.WHITE + Style.BRIGHT + mesaj).replace(",", "."))


yenile()

while True:
    try:
        ana_secim = int(input(Fore.WHITE + Style.BRIGHT + "Lütfen Bir Seçim Yapınız: "))
        yenile()

        if ana_secim == 1:
            print(Fore.CYAN + Style.BRIGHT + "Km -> Mil")
            deger = sayi_al("Lütfen Km Giriniz: ")
            sonuc = deger * KM_MIL
            print(Fore.GREEN + Style.BRIGHT + f"{deger} Km = {sonuc:.2f} Mil.")

        elif ana_secim == 2:
            print(Fore.CYAN + Style.BRIGHT + "Mil -> Km")
            deger = sayi_al("Lütfen Mil Giriniz: ")
            sonuc = deger * MIL_KM
            print(Fore.GREEN + Style.BRIGHT + f"{deger} Mil = {sonuc:.2f} Km.")

        elif ana_secim == 3:
            print(Fore.CYAN + Style.BRIGHT + "°C -> °F")
            deger = sayi_al("Lütfen °C Giriniz: ")
            sonuc = deger * 9 / 5 + 32
            print(Fore.GREEN + Style.BRIGHT + f"{deger} °C = {sonuc:.2f} °F.")

        elif ana_secim == 4:
            print(Fore.CYAN + Style.BRIGHT + "°F -> °C")
            deger = sayi_al("Lütfen °F Giriniz: ")
            sonuc = (deger - 32) * 5 / 9
            print(Fore.GREEN + Style.BRIGHT + f"{deger} °F = {sonuc:.2f} °C.")

        elif ana_secim == 5:
            print(Fore.CYAN + Style.BRIGHT + "Kg -> Lb")
            deger = sayi_al("Lütfen Kg Giriniz: ")
            sonuc = deger * KG_LB
            print(Fore.GREEN + Style.BRIGHT + f"{deger} Kg = {sonuc:.2f} Lb.")

        elif ana_secim == 6:
            print(Fore.CYAN + Style.BRIGHT + "Lb -> Kg")
            deger = sayi_al("Lütfen Lb Giriniz: ")
            sonuc = deger * LB_KG
            print(Fore.GREEN + Style.BRIGHT + f"{deger} Lb = {sonuc:.2f} Kg.")

        elif ana_secim == 7:
            print(Fore.RED + Style.BRIGHT + "Çıkış Sağlandı, Görüşmek Üzere...")
            break

        else:
            print(Fore.RED + Style.BRIGHT + "Lütfen Geçerli Bir Seçim Yap.")

    except ValueError:
        yenile()
        print(Fore.RED + Style.BRIGHT + "Lütfen Bir Sayı Giriniz!")