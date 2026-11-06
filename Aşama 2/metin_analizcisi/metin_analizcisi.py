import string

print(" ")
print(" ")
print("==============================")
girilen_kelime = input("Kelime giriniz: ").lower()
print("==============================")
print(" ")
print(" ")

isaret_listesi = string.punctuation

sayac = {}

for isaret in isaret_listesi:
    girilen_kelime=girilen_kelime.replace(isaret," ").replace("'"," ")
kelimeler = girilen_kelime.split()

for kelime in kelimeler:
    if kelime in sayac:
        sayac[kelime] += 1
    else:
        sayac[kelime] = 1

toplam_kelime = len(kelimeler)

en_cok_kullanilan = sorted(sayac.items(), key=lambda x: x[1], reverse=True)[:10]

farkli_kelime = len(sayac)
print(" ")
print(" ")
print("==============================")
print("         Toplam Kelime")
print("==============================")
print(f"{toplam_kelime} Adet Kelime Bulunmakta.")
print(" ")
print(" ")

print("==============================")
print("         Farklı Kelime")
print("==============================")
print(f"{farkli_kelime} Adet Farklı Kelime Bulunmakta")
print(" ")
print(" ")

print("==============================")
print("  En Çok Kullanılan Kelimeler")
print("==============================")
for kelime, adet in en_cok_kullanilan:
    print("----------------------")
    print(f"{kelime}: {adet}")
print("==============================")
print(" ")
print(" ")



