# kendi yazdigim modul (islemler.py)
import islemler
import os
import time
from colorama import Fore, Style, init

init()  # windows'ta renkler bozuk cikmasin diye

# simge -> fonksiyon eslesmesi
islem = {
    "+": islemler.toplama,
    "-": islemler.cikarma,
    "*": islemler.carpma,
    "/": islemler.bolme
}


def yaz(metin, renk=Fore.WHITE, hiz=0.03):
    # yaziyi harf harf yazdirir, ayni kodu surekli tekrar etmemek icin yaptim
    print(renk, end="")
    for harf in metin:
        print(harf, end="", flush=True)
        time.sleep(hiz)
    print(Style.RESET_ALL)


def bekle():
    # enter'a basana kadar bekle ki uyarilari okuyabileyim
    input(Fore.CYAN + "Devam için ENTER tuşuna bas..." + Style.RESET_ALL)


while True:
    # ekrani temizle (windows degilse clear)
    os.system("cls" if os.name == "nt" else "clear")

    # menu
    yaz("'+'-(Toplama)\n'-'-(Çıkarma)\n'*'-(Çarpma)\n'/'-(Bölme)\n'0'-(Çıkış)", Fore.CYAN, 0.02)

    secim = input(Fore.MAGENTA + "Yapmak istediğiniz işlem nedir: " + Style.RESET_ALL)

    # 0 girerse cikis
    if secim == "0":
        yaz("Görüşmek Üzere...", Fore.GREEN, 0.15)
        break
    # sozlukte olmayan bir sey girdiyse basa don
    elif secim not in islem:
        yaz("Geçerli Bir Seçim Yapınız.", Fore.RED, 0.05)
        bekle()
        continue

    girdi = input(Fore.MAGENTA + "Sayıları aralarında boşluk bırakarak girin: " + Style.RESET_ALL)

    # yaziyi sayiya cevir, harf girerse hata verir
    sayilar = []
    try:
        for parca in girdi.split():
            sayilar.append(float(parca))
    except ValueError:
        yaz("Lütfen Sayı Giriniz.", Fore.RED, 0.05)
        bekle()
        continue

    # hic sayi girmediyse (sadece enter) cokmesin
    if not sayilar:
        yaz("Lütfen Sayı Giriniz.", Fore.RED, 0.05)
        bekle()
        continue

    # sozlukten fonksiyonu al, sayilari * ile ac
    sonuc = islem[secim](*sayilar)
    print(Fore.GREEN + "Sonuç:", sonuc, Style.RESET_ALL)
    bekle()