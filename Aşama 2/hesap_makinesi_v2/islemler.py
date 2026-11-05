# islemler.py - dort islem burada, main.py bunlari import edip kullaniyor

def toplama(*args):
    # *args sayesinde kac sayi gelirse gelsin calisir
    toplam = 0  # toplamada baslangic 0, sonucu bozmaz
    for sayi in args:
        toplam += sayi
    return toplam  # for'un disinda, yoksa ilk turda biter


def cikarma(*args):
    # sira onemli, o yuzden 0'dan degil ilk sayidan basliyoruz
    toplam = args[0]
    for sayi in args[1:]:  # ilk sayiyi zaten aldik, gerisini cikar
        toplam -= sayi
    return toplam


def carpma(*args):
    # carpmada baslangic 1, 0 olsaydi her sey 0 cikardi
    toplam = 1
    for sayi in args:
        toplam *= sayi
    return toplam


def bolme(*args):
    # cikarma gibi ilk sayidan basla, gerisine sirayla bol
    toplam = args[0]
    for sayi in args[1:]:
        if sayi == 0:
            # sifira bolunce program coker, o yuzden mesaj donduruyoruz
            return "sıfıra bölünemez."
        toplam /= sayi
    return toplam