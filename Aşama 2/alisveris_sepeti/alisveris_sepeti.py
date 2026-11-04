stok = {
    'Elma': 5.5,
    'Armut': 6,
    'Muz': 12,
    'Portakal': 8,
    'Mandalina': 7.5,
    'Çilek': 25,
    'Üzüm': 18,
    'Karpuz': 4,
    'Kavun': 6.5,
    'Şeftali': 14,
    'Kiraz': 40,
    'Domates': 9,
    'Salatalık': 7,
    'Biber': 15,
    'Patlıcan': 11,
    'Patates': 6,
    'Soğan': 5,
    'Sarımsak': 45,
    'Havuç': 6.5,
    'Marul': 10,
    'Süt': 30,
    'Yoğurt': 35,
    'Ayran': 12,
    'Peynir': 120,
    'Tereyağı': 95,
    'Yumurta': 4.5,
    'Ekmek': 10,
    'Pirinç': 55,
    'Makarna': 22,
    'Bulgur': 28,
    'Mercimek': 40,
    'Nohut': 38,
    'Şeker': 35,
    'Tuz': 10,
    'Un': 30,
    'Zeytinyağı': 280,
    'Ayçiçek Yağı': 90,
    'Çay': 85,
    'Kahve': 150,
    'Su': 5
}

sepet={

}

class Sepet:
    def __init__(self):
        self.sepet = {}

    def urun_ekle(self):
        urun_ad = input("Ürün Adı Giriniz: ").strip().capitalize()

        if urun_ad not in stok:
            print("Bu ürün listede yok.")
            return

        try:
            miktar = int(input("Almak İstediğiniz Miktarı Giriniz: "))
        except ValueError:
            print("Lütfen sayı giriniz.")
            return

        if miktar <= 0:
            print("Miktar 0'dan büyük olmalı.")
            return

        # Aynı ürün tekrar eklenirse üstüne ekle
        self.sepet[urun_ad] = self.sepet.get(urun_ad, 0) + miktar
        print(f"{miktar} Adet {urun_ad} eklendi.")

    def urun_cikar(self):
        urun_ad = input("Çıkarmak istediğiniz ürünü yazınız: ").strip().capitalize()

        if urun_ad not in self.sepet:
            print("Bu ürün sepette yok.")
            return

        adet = self.sepet[urun_ad]
        miktar = adet  # varsayılan: hepsini çıkar

        if adet > 1:
            print(f"Sepette {adet} Adet {urun_ad} var.")
            try:
                miktar = int(input("Çıkarmak İstediğiniz Miktarı Giriniz: "))
            except ValueError:
                print("Lütfen sayı giriniz.")
                return

        if miktar >= adet:
            del self.sepet[urun_ad]
        else:
            self.sepet[urun_ad] = adet - miktar

    def listele(self):
        if not self.sepet:
            print("Sepet boş.")
            return
        for urun, adet in self.sepet.items():
            satir = stok[urun] * adet
            print(f"{adet} Adet {urun} x {stok[urun]:.2f} TL = {satir:.2f} TL")
        print(f"Genel Toplam: {self.toplam():.2f} TL")

    def toplam(self):
        return sum(stok[urun] * adet for urun, adet in self.sepet.items())

sepetim=Sepet()

while True:
    print("--SEPETE HOŞGELDİNİZ--")
    print("1-Ürün Ekle\n2-Ürün Çıkar\n3-Listele\n4-Çıkış")
    try:
        secim=int(input("Seçim Yapınız: "))
    except ValueError:
        print("Lütfen Sayı Giriniz.")
        continue
    if secim==1:
        print("--Ürün Ekleme--")
        sepetim.urun_ekle()
    elif secim==2:
        print("--Ürün Çıkarma--")
        sepetim.urun_cikar()
    elif secim==3:
        print("--Sepet Listeleme--")
        sepetim.listele()
    elif secim==4:
        print("Görüşmek Üzere...")
        break
    else:
        print("Lütfen Geçerli Bir Seçim Yapınız.")
        







