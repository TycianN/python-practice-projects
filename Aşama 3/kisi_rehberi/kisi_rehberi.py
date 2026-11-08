import time  # arama yaparken "çalıyor" havası vermek için 2 saniye bekletmek istiyorum, o yüzden time lazım

# rehberi tuttuğumuz sözlük
# anahtar = isim, değer = numara (yani "tayciann": "05551234567" gibi)
# en dışarıda tanımladım ki bütün metotlar ona ulaşabilsin
rehber = {}

# class
# telefonun yapabildiği her şeyi (kaydet, ara, düzenle) bu sınıfın içine koydum
class Telefon:
    # yeni bir kişiyi rehbere kaydeden metot
    def kisi_kaydet(self):
        # geçerli bir kayıt yapana kadar baştan sormaya devam etsin diye while True kullandım
        while True:
            isim = input("Kaydetmek istediğiniz kişinin ismini giriniz: ")
            # hiçbir şey yazmadan enter'a basılırsa isim boş gelir, bunu kabul etmiyoruz
            if not isim:
                print("İsim boş olamaz.")
                continue  # başa dön, tekrar isim sor
            # aynı isim zaten sözlükte varsa üstüne yazmasın diye kontrol ediyoruz
            if isim in rehber:
                print("Bu isimde birisi zaten kayıtlı.")
                continue
            # isim olarak sadece rakam yazılırsa (mesela 88) saçma olur, onu da engelledim
            if isim.isdigit():
                print("İsim sadece rakamlardan oluşamaz.")
                continue
            # isim tamamsa numarayı soruyoruz, isim kötüyse buraya hiç gelmeden başa dönüyor
            numara = input("Telefon numaranızı girin (Sadece rakam): ")
            # numara sadece rakamlardan oluşmalı VE tam 11 haneli olmalı (05xx formatı için)
            # ikisinden biri tutmuyorsa hata veriyoruz, o yüzden başına not koydum
            if not (numara.isdigit() and len(numara) == 11):
                print("Lütfen Geçerli Bir Numara Giriniz")
                continue
            # aynı numara başka birinde varsa kaydetmeyelim
            # rehber.values() sözlükteki bütün numaraları verir, anahtarlara değil değerlere bakıyoruz
            if numara in rehber.values():
                print("Bu numara başka bir kişide kayıtlı.")
                continue
            # buraya kadar geldiyse her şey düzgün demek, kaydı yapıyoruz
            rehber[isim] = numara
            print(f"Harika! {numara}, {isim} Adıyla Kaydedildi.")
            break  # kayıt bitti, döngüden çık ve menüye dön

    # rehberden ya da elle numara girerek arama yapan metot
    def arama_yap(self):
        print("1- Rehberden Arama Yap\n2- Numara Girerek Arama Yap")
        # int() içine aldım ama biri harf girerse ValueError verir
        # onu en alttaki menüde try/except ile yakalıyoruz, program çökmesin diye
        secim = int(input("Seçim Yapınız: "))
        if secim == 1:
            # önce rehberdeki herkesi ekrana yazdırıyoruz ki kullanıcı kimi arayacağını görsün
            # .items() hem ismi hem numarayı aynı anda verir
            for isim, numara in rehber.items():
                print(f"İsim: {isim}\nNumara: {numara}\n--")
            kisi_secim = input("Kimi Aramak İstersiniz(isim): ")
            # yazılan isim sözlükte varsa aramayı başlatıyoruz
            if kisi_secim in rehber:
                print(f"{kisi_secim} aranıyor... ({rehber[kisi_secim]})")
                time.sleep(2)  # 2 saniye bekle, gerçekten çalıyormuş gibi olsun
                print(f"{kisi_secim} Cevap Vermedi, Başka Zaman Aramayı Deneyiniz.")
            else:
                print("Rehberde böyle bir kişi yok.")
        elif secim == 2:
            # bu seçenekte rehbere bakmıyoruz, direkt numarayı kendimiz yazıyoruz
            numara = input("Aranacak Numara: ")
            # numaranın geçerli olup olmadığını burada da aynı şekilde kontrol ediyoruz
            if not (numara.isdigit() and len(numara) == 11):
                print("Lütfen Geçerli Bir Numara Giriniz")
                return  # geçersizse fonksiyondan çık, menüye dön
            print(f"{numara} aranıyor...")
            time.sleep(2)
            print("Cevap Vermedi, Başka Zaman Aramayı Deneyiniz.")

    # rehberdeki bir kişinin ismini, numarasını değiştiren ya da kişiyi silen metot
    def rehber_duzenle(self):
        # rehber boşsa düzenleyecek bir şey yok, boşuna soru sormayalım
        # boş sözlük "False" sayılır, o yüzden "not rehber" boş demek oluyor
        if not rehber:
            print("Rehber boş.")
            return
        # kullanıcı kimi düzenleyeceğini bilsin diye herkesi listeliyoruz
        for isim, numara in rehber.items():
            print(f"İsim: {isim}\nNumara: {numara}\n--")
        # geçerli bir işlem yapılana ya da q'ya basılana kadar sormaya devam
        while True:
            kisi_secim = input("Kimi Düzenlemek İstersiniz(isim) (çıkmak için q): ")
            # q yazarsa hiçbir şey yapmadan döngüden çıkıp menüye dönüyoruz
            if kisi_secim == "q":
                break
            # yazılan isim rehberde yoksa uyar ve baştan sor
            # bunu en başta eledim ki aşağıdaki kodlar hep "kişi var" varsayımıyla yazılabilsin
            if kisi_secim not in rehber:
                print("Rehberde böyle bir kişi yok.")
                continue
            print("1- İsmi Düzenle\n2- Numarayı Düzenle\n3- Kişiyi Sil")
            secim = input("Seçim Yapınız: ")
            if secim == "1":
                yeni_isim = input("Yeni İsim: ")
                # yeni isim boşsa ya da başkasında zaten varsa kabul etmiyoruz
                if not yeni_isim or yeni_isim in rehber:
                    print("Geçersiz ya da zaten kayıtlı bir isim.")
                    continue
                # sözlükte anahtar (isim) direkt değiştirilemez
                # o yüzden eski kaydı pop ile silip numarasını alıyoruz, yeni isimle tekrar ekliyoruz
                rehber[yeni_isim] = rehber.pop(kisi_secim)
                print("İsim güncellendi.")
                break
            elif secim == "2":
                yeni_numara = input("Yeni Numara: ")
                # yeni numara da kayıttaki kurallara uymalı: sadece rakam ve 11 hane
                if not (yeni_numara.isdigit() and len(yeni_numara) == 11):
                    print("Lütfen Geçerli Bir Numara Giriniz")
                    continue
                # anahtar (isim) aynı kalıyor, sadece değeri (numarayı) üstüne yazıyoruz
                rehber[kisi_secim] = yeni_numara
                print("Numara güncellendi.")
                break
            elif secim == "3":
                # del ile sözlükten kişiyi tamamen siliyoruz (isim + numara birlikte gider)
                del rehber[kisi_secim]
                print("Kişi silindi.")
                break
            else:
                # 1, 2 ya da 3 dışında bir şey yazıldıysa uyar, döngü başa döner
                print("Geçersiz seçim.")

# sınıftan bir nesne oluşturuyoruz, bütün metotlara bu "telefon" üzerinden ulaşacağız
telefon = Telefon()
# ana menü: kullanıcı 4'e basana kadar sürekli ekrana gelsin diye while True içinde
while True:
    print("\n1- Kişi Kaydet\n2- Arama Yap\n3- Rehberi Düzenle\n4- Çıkış")
    secim = input("Seçiminiz: ")
    # try içine aldım çünkü arama_yap'taki int(input()) harf girilirse ValueError fırlatıyor
    # böyle olunca program çökmesin, aşağıdaki except mesaj verip menüye geri dönsün
    try:
        if secim == "1":
            telefon.kisi_kaydet()
        elif secim == "2":
            telefon.arama_yap()
        elif secim == "3":
            telefon.rehber_duzenle()
        elif secim == "4":
            # çıkış mesajı, sonra break ile ana döngüyü bitiriyoruz ve program kapanıyor
            print("Çıkış Yapıldı, Görüşürüz...(NOT: rehber kaydedilmemektedir projenin konularında json yoktur.)")
            break
        else:
            # 1-4 dışında bir şey yazıldıysa uyar, menü tekrar görünür
            print("Geçerli bir seçim yapınız.")
    except ValueError:
        # arama menüsünde sayı yerine harf yazılırsa buraya düşer
        print("Lütfen Geçerli bir sayı giriniz.")