import secrets
import string


def evet_mi(soru):
    return input(f"{soru} (e/h): ").strip().lower() == "e"


def sifre_uret(uzunluk, harf=True, rakam=True, sembol=True):
    gruplar = []
    if harf:
        gruplar.append(string.ascii_letters)
    if rakam:
        gruplar.append(string.digits)
    if sembol:
        gruplar.append(string.punctuation)

    if not gruplar:
        raise ValueError("En az bir karakter türü seçmelisin.")
    if uzunluk < len(gruplar):
        raise ValueError(f"Şifre en az {len(gruplar)} karakter olmalı.")

    # Seçilen her türden en az bir karakter garanti
    sifre = [secrets.choice(grup) for grup in gruplar]

    # Kalanı tüm karakterlerden doldur
    tum_karakterler = "".join(gruplar)
    sifre += [secrets.choice(tum_karakterler) for _ in range(uzunluk - len(gruplar))]

    # Garanti edilen karakterler hep başta kalmasın diye karıştır
    secrets.SystemRandom().shuffle(sifre)
    return "".join(sifre)


def main():
    try:
        uzunluk = int(input("Şifre uzunluğu: "))
    except ValueError:
        print("Lütfen geçerli bir sayı gir.")
        return

    harf = evet_mi("Harf olsun mu")
    rakam = evet_mi("Rakam olsun mu")
    sembol = evet_mi("Sembol olsun mu")

    try:
        print(f"Şifren: {sifre_uret(uzunluk, harf, rakam, sembol)}")
    except ValueError as hata:
        print(hata)


if __name__ == "__main__":
    main()


    
