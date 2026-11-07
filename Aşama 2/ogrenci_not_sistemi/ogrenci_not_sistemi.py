# ==================== KÜTÜPHANELER ====================
import os                                # ekranı temizlemek için
import time                              # bekleme efekti için
from itertools import zip_longest        # iki listeyi yan yana basmak için
from colorama import init, Fore, Style   # terminalde renk için

# colorama'yı başlatıyoruz. autoreset=True dersek her print'ten sonra
# renk kendiliğinden sıfırlanır, "Style.RESET_ALL" yazmak zorunda kalmayız.
init(autoreset=True)

# ==================== VERİLER ====================
kayit = {}      # tüm öğrenciler: {isim: not}
gecenler = {}   # 50 ve üstü alanlar
kalanlar = {}   # 50'nin altında kalanlar


# ==================== YARDIMCI FONKSİYONLAR ====================
def ekrani_temizle():
    # Windows'ta komut "cls", Mac/Linux'ta "clear". İkisini de kapsıyoruz.
    os.system("cls" if os.name == "nt" else "clear")


def bekle(saniye=1.5):
    # Mesajı kullanıcı okuyabilsin diye kısa bir mola veriyoruz.
    time.sleep(saniye)


def devam_etmek_icin_bekle():
    # Listeyi gösterdikten sonra ekran hemen silinmesin diye Enter bekliyoruz.
    input(Fore.CYAN + "\nAna menüye dönmek için Enter'a bas...")


class Ogrenci_not:

    # ---------- ANA MENÜ ----------
    def ana_menu():
        while True:
            ekrani_temizle()
            print(Fore.CYAN + Style.BRIGHT + "=" * 40)
            print(Fore.YELLOW + Style.BRIGHT + "     ÖĞRENCİ NOT KAYIT SİSTEMİ")
            print(Fore.CYAN + Style.BRIGHT + "=" * 40)
            print(Fore.GREEN + "  1- " + Fore.WHITE + "Öğrenci Ekle")
            print(Fore.BLUE + "  2- " + Fore.WHITE + "Tam Liste Oluştur")
            print(Fore.MAGENTA + "  3- " + Fore.WHITE + "Geçenler/Kalanlar Listesi")
            print(Fore.RED + "  4- " + Fore.WHITE + "Çıkış")
            print(Fore.CYAN + Style.BRIGHT + "=" * 40)

            # Harf girilirse program çökmesin diye try/except kullanıyoruz.
            try:
                secim = int(input(Fore.YELLOW + "Seçiminiz: "))
            except ValueError:
                print(Fore.RED + "Lütfen sadece sayı giriniz!")
                bekle()
                continue

            # Seçime göre ilgili fonksiyonu çağırıyoruz.
            if secim == 1:
                Ogrenci_not.bilgi_al()
            elif secim == 2:
                Ogrenci_not.listele()
            elif secim == 3:
                Ogrenci_not.gecti_mi_kaldi_mi()
            elif secim == 4:
                print(Fore.GREEN + "Çıkış yapılıyor, görüşürüz! 👋")
                bekle()
                ekrani_temizle()
                break
            else:
                print(Fore.RED + "Geçersiz seçim! 1 ile 4 arasında bir sayı gir.")
                bekle()

    # ---------- ÖĞRENCİ EKLEME ----------
    def bilgi_al():
        ekrani_temizle()
        print(Fore.CYAN + Style.BRIGHT + "--- ÖĞRENCİ EKLE ---\n")

        while True:
            ad_soyad = input(Fore.WHITE + "Öğrencinin Adını Ve Soyadını Yazınız: ").strip()

            # Boş isim kaydetmeyelim.
            if ad_soyad == "":
                print(Fore.RED + "İsim boş olamaz!")
                continue

            # Not sayı olmak zorunda, değilse tekrar soruyoruz.
            try:
                notu = float(input(f"{ad_soyad}'ın Notunu Giriniz: "))
            except ValueError:
                print(Fore.RED + "Lütfen sayı giriniz!")
                continue

            # Not 0-100 arasında olmalı.
            if notu < 0 or notu > 100:
                print(Fore.RED + "Not 0 ile 100 arasında olmalı!")
                continue

            # Her turda kaydediyoruz ki "e" dediğimizde de veri kaybolmasın.
            kayit[ad_soyad] = notu
            print(Fore.GREEN + f"✔ {ad_soyad} başarıyla kaydedildi!")
            bekle(1)

            devam_mi = input("Bilgi Girmeye Devam Etmek İstermisiniz?(e/h): ").lower()
            if devam_mi == "h":
                print(Fore.GREEN + "Bilgiler Kaydedildi, Ana Menüye Dönülüyor...")
                bekle()
                return   # fonksiyondan çık, ana menü döngüsüne geri dön
            print(Fore.YELLOW + "Devam Ediliyor...\n")

    # ---------- GEÇENLER / KALANLAR ----------
    def gecti_mi_kaldi_mi():
        ekrani_temizle()

        # Kayıt yoksa listelemenin anlamı yok.
        if not kayit:
            print(Fore.RED + "Henüz kayıtlı öğrenci yok!")
            bekle()
            return

        # Eski sonuçlar karışmasın diye önce sözlükleri sıfırlıyoruz.
        gecenler.clear()
        kalanlar.clear()

        # Herkesi nota göre doğru gruba atıyoruz.
        for ad_soyad, notu in kayit.items():
            if notu >= 50:
                gecenler[ad_soyad] = notu
            else:
                kalanlar[ad_soyad] = notu

        # Ekrana basılacak satırları hazırlıyoruz ({notu:g} -> 50.0 yerine 50 yazar).
        sol = [f"{ad} - {notu:g}" for ad, notu in gecenler.items()]
        sag = [f"{ad} - {notu:g}" for ad, notu in kalanlar.items()]

        # Sol sütunun genişliği en uzun satıra göre ayarlanır, sütunlar düzgün hizalanır.
        genislik = max([len(s) for s in sol] + [len("GEÇENLER")]) + 4

        # Başlıklar: geçenler yeşil, kalanlar kırmızı.
        print(Fore.GREEN + Style.BRIGHT + "GEÇENLER".ljust(genislik)
              + Fore.RED + Style.BRIGHT + "KALANLAR")
        print(Fore.CYAN + "-" * (genislik + 25))

        # zip_longest: listeler farklı uzunlukta olsa bile hiçbir öğrenci kaybolmaz.
        for g, k in zip_longest(sol, sag, fillvalue=""):
            print(Fore.GREEN + g.ljust(genislik) + Fore.RED + k)

        devam_etmek_icin_bekle()

    # ---------- TAM LİSTE ----------
    def listele():
        ekrani_temizle()

        if not kayit:
            print(Fore.RED + "Henüz kayıtlı öğrenci yok!")
            bekle()
            return

        print(Fore.CYAN + Style.BRIGHT + "--- TÜM ÖĞRENCİLER ---\n")
        for ad_soyad, notu in kayit.items():
            print(Fore.WHITE + f" {ad_soyad} - " + Fore.YELLOW + f"{notu:g}")

        devam_etmek_icin_bekle()


# ==================== PROGRAMI BAŞLAT ====================
Ogrenci_not.ana_menu()