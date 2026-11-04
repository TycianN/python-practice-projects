import json
from colorama import Fore,Back,Style
import os
import time

uygulama_adi="Listly"
version="v1.0.0"

#Classlar
class AnaListe:
    def __init__(self,ad,miktar):
        self.urun_adi=ad
        self.urun_miktari=miktar
    def urun_ekle():
        pass
    def urun_cikar():
        pass

sepet = {}  # { "ürün_adı": miktar }

class Alisveris_listesi(AnaListe): 
    def urun_ekle(self):
        soru_ad = input(Fore.WHITE+Style.RESET_ALL+"Eklemek İstediğiniz Ürünün Adı Nedir: ")
        soru_miktar = int(Fore.WHITE+Style.RESET_ALL+input(f"{soru_ad} Ürününden Kaç Tane Eklemek İstersiniz: "))
        
        # Ürün zaten sepette varsa miktarını üstüne ekle, yoksa yeni ekle
        if soru_ad in sepet:
            sepet[soru_ad] += soru_miktar
        else:
            sepet[soru_ad] = soru_miktar
        print(Fore.GREEN+Style.BRIGHT+f"Ürün Başarıyla eklendi!")

    def urun_cikar(self):
        cikar_ad_soru = input(Fore.WHITE+Style.RESET_ALL+"Hangi Ürünü Çıkarmak İstersiniz: ")
        
        # Önce ürün sepette var mı diye kontrol ediyoruz
        if cikar_ad_soru in sepet:
            cikar_miktar_soru = int(Fore.WHITE+Style.RESET_ALL+input(f"{cikar_ad_soru} Ürününden Kaç Tane Çıkarmak İstersiniz: "))
            
            # Çıkarmak istenen miktar, sepetteki miktara eşit veya fazlaysa ürünü tamamen sil
            if cikar_miktar_soru >= sepet[cikar_ad_soru]:
                del sepet[cikar_ad_soru]
                print(Fore.RED+Style.BRIGHT+f"{cikar_ad_soru} sepetten tamamen kaldırıldı.")
            else:
                # Sadece miktarını azalt
                sepet[cikar_ad_soru] -= cikar_miktar_soru
                print(Fore.RED+Style.BRIGHT+f"{cikar_ad_soru} miktarından {cikar_miktar_soru} adet çıkarıldı. Kalan: {sepet[cikar_ad_soru]}")
        else:
            print(Fore.RED+Style.BRIGHT+"Bu ürün zaten sepette yok.")

    def sepeti_kaydet(self):
        json.dump(sepet,open("Alisveris_Sepeti.json","w",encoding="utf-8"))


    def sepeti_goruntule(self):
        if not sepet:
            print(Fore.RED + "Sepetin bomboş, henüz bir şey eklemedin." + Style.RESET_ALL)
        else:
            print(Fore.CYAN+Style.BRIGHT+"\n--- 🛒 SEPETİNİZ ---")
            for urun, miktar in sepet.items():
                print(Fore.WHITE+Style.RESET_ALL+f"• {urun} " + f"- {miktar} adet")
            print(Fore.CYAN+Style.BRIGHT+"--------------------")

while True:
    print(Fore.CYAN+Style.BRIGHT+"-------------------------")
    print(Fore.CYAN+Style.BRIGHT+f"-------- {uygulama_adi} ---------")
    print(Fore.CYAN+Style.BRIGHT+"-------------------------")

    print(Fore.WHITE+Style.BRIGHT+"1 -> Ürün Ekle\n2 -> Ürün Çıkar\n3 -> Sepeti Kaydet\n4 -> Sepeti Görüntüle")
    try:
        secim=int(input(Fore.WHITE+Style.RESET_ALL+"\nNe Yapmak İstersiniz: "))
    except ValueError:
        print(Fore.RED+Style.BRIGHT+"Lütfen Sayı Giriniz.")
    if secim=="1":
        print(Fore.CYAN+Style.BRIGHT+"\n--- ➕ ÜRÜN EKLEME ---")


# satır renkleri kontrol edilecek. headerlar cyan, yazılar white, uyarılar yada negatif şeyler kırmızı, olumlu şeyler green.
