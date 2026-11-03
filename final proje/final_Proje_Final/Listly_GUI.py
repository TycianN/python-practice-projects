import copy
import json
import os
import sys
from datetime import datetime
from tkinter import filedialog, messagebox

import customtkinter as ctk
from PIL import Image

APP_ADI = "Listly"
VERSION = "v2.0.0"

if getattr(sys, "frozen", False):
    BASE_DIR = os.path.dirname(sys.executable)  # exe'nin bulunduğu klasör
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def kaynak_yolu(dosya):
    """Logo/ikon gibi pakete gömülü dosyaların yolu (exe'de _MEIPASS içinde)."""
    taban = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(taban, dosya)

JSON_DOSYA = os.path.join(BASE_DIR, "Alisveris_Sepeti.json")
AYAR_DOSYA = os.path.join(BASE_DIR, "Listly_Ayarlar.json")
TARIH_FORMAT = "%d.%m.%Y %H:%M"

CYAN = "#22d3ee"
YESIL = "#2fb344"
KIRMIZI = "#e5484d"
BEYAZ = "#ffffff"


# ---------- Yardımcı fonksiyonlar ----------
def simdi():
    return datetime.now().strftime(TARIH_FORMAT)


def yeni_id():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def yeni_liste_verisi():
    tarih = simdi()
    return {"id": yeni_id(), "olusturma": tarih, "guncelleme": tarih, "urunler": {}}


# ---------- Ayarlar (kullanıcı bilgisi + kayıt klasörü) ----------
def ayarlari_yukle():
    varsayilan = {
        "kullanici": {"ad": "", "soyad": "", "yas": "", "sehir": ""},
        "kayit_klasoru": "",
    }
    if not os.path.exists(AYAR_DOSYA):
        return varsayilan
    try:
        with open(AYAR_DOSYA, "r", encoding="utf-8") as f:
            veri = json.load(f)
        varsayilan["kullanici"].update(veri.get("kullanici", {}))
        varsayilan["kayit_klasoru"] = veri.get("kayit_klasoru", "")
    except (json.JSONDecodeError, OSError):
        pass
    return varsayilan


def ayarlari_kaydet(ayarlar):
    with open(AYAR_DOSYA, "w", encoding="utf-8") as f:
        json.dump(ayarlar, f, ensure_ascii=False, indent=2)


# ---------- Liste verileri ----------
def verileri_yukle():
    if not os.path.exists(JSON_DOSYA):
        return []
    try:
        with open(JSON_DOSYA, "r", encoding="utf-8") as f:
            veri = json.load(f)
    except json.JSONDecodeError:
        os.replace(JSON_DOSYA, JSON_DOSYA + ".bak")  # bozuk dosyayı yedekle
        return []

    if isinstance(veri, dict) and "listeler" in veri:
        return veri["listeler"]
    if isinstance(veri, dict) and veri:  # en eski format: { "ürün": miktar }
        tarih = simdi()
        return [{"id": yeni_id(), "olusturma": tarih, "guncelleme": tarih, "urunler": veri}]
    return []


def json_kaydet(listeler):
    with open(JSON_DOSYA, "w", encoding="utf-8") as f:
        json.dump({"listeler": listeler}, f, ensure_ascii=False, indent=2)


def txt_yaz(veri, klasor):
    os.makedirs(klasor, exist_ok=True)
    yol = os.path.join(klasor, f"Alisveris_Listesi_{veri['id']}.txt")
    gun = veri["olusturma"].split(" ")[0]
    with open(yol, "w", encoding="utf-8") as f:
        f.write(f"{gun} tarihli alışveriş listesi\n")
        f.write("=" * 32 + "\n\n")
        if veri["urunler"]:
            for urun, miktar in veri["urunler"].items():
                f.write(f"- {urun}: {miktar} adet\n")
        else:
            f.write("(Liste boş)\n")
        f.write(f"\nOluşturma: {veri['olusturma']}\n")
        f.write(f"Son düzenleme: {veri['guncelleme']}\n")
    return yol


# ---------- Kullanıcı tanıma penceresi ----------
class ProfilPenceresi(ctk.CTkToplevel):
    def __init__(self, ana, kullanici):
        super().__init__(ana)
        self.ana = ana
        self.title("Seni Tanıyalım")
        self.geometry("340x470")
        self.resizable(False, False)
        self.transient(ana)

        ctk.CTkLabel(
            self, text="Seni tanıyalım 👋", text_color=CYAN,
            font=ctk.CTkFont(size=20, weight="bold"),
        ).pack(pady=(20, 10))

        self.ad = self._alan("Ad *", kullanici.get("ad", ""))
        self.soyad = self._alan("Soyad *", kullanici.get("soyad", ""))
        self.yas = self._alan("Yaş", kullanici.get("yas", ""))
        self.sehir = self._alan("Şehir", kullanici.get("sehir", ""))

        self.hata = ctk.CTkLabel(self, text="", text_color=KIRMIZI)
        self.hata.pack(pady=(4, 0))
        ctk.CTkButton(self, text="Kaydet", command=self.kaydet).pack(pady=12)

        self.after(150, self._odak)

    def _alan(self, etiket, deger):
        ctk.CTkLabel(self, text=etiket, anchor="w").pack(fill="x", padx=30)
        e = ctk.CTkEntry(self)
        e.pack(fill="x", padx=30, pady=(0, 8))
        e.insert(0, deger)
        return e

    def _odak(self):
        self.lift()
        self.grab_set()
        self.ad.focus()

    def kaydet(self):
        ad = self.ad.get().strip()
        soyad = self.soyad.get().strip()
        yas = self.yas.get().strip()
        sehir = self.sehir.get().strip()

        if not ad or not soyad:
            self.hata.configure(text="Ad ve soyad boş olamaz.")
            return
        if yas and (not yas.isdigit() or not 0 < int(yas) < 120):
            self.hata.configure(text="Geçerli bir yaş gir.")
            return

        self.ana.profil_kaydet({"ad": ad, "soyad": soyad, "yas": yas, "sehir": sehir})
        self.destroy()


# ---------- Ana uygulama ----------
class ListlyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.title(f"{APP_ADI} {VERSION}")
        self.geometry("980x620")
        self.minsize(860, 520)

        # Açılışta veriler otomatik yüklenir
        self.ayarlar = ayarlari_yukle()
        self.listeler = verileri_yukle()
        self.aktif = yeni_liste_verisi()
        self.degisti = False

        self._arayuz_kur()
        self.yenile()

        self.protocol("WM_DELETE_WINDOW", self.kapat)
        self.after(200, self._ikon_koy)  # CTk'de ikon biraz gecikmeli verilmeli

        # İlk açılışta kullanıcıyı tanı
        if not self.ayarlar["kullanici"]["ad"]:
            self.after(300, self.profil_ac)

    def _ikon_koy(self):
        try:
            self.iconbitmap(kaynak_yolu("Listly.ico"))
        except Exception:
            pass  # ikon bulunamazsa uygulama yine çalışır

    # ----- Arayüz -----
    def _arayuz_kur(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sol panel
        yan = ctk.CTkFrame(self, width=260, corner_radius=0)
        yan.grid(row=0, column=0, sticky="nsew")
        yan.grid_propagate(False)
        yan.grid_rowconfigure(5, weight=1)

        try:
            logo = ctk.CTkImage(Image.open(kaynak_yolu("Listly_logo.png")), size=(48, 48))
        except OSError:
            logo = None
        ctk.CTkLabel(
            yan, text=f"  {APP_ADI}", image=logo, compound="left", text_color=CYAN,
            font=ctk.CTkFont(size=28, weight="bold"),
        ).grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")
        ctk.CTkLabel(yan, text=VERSION, text_color="gray").grid(
            row=1, column=0, padx=20, sticky="w")

        self.kullanici_lbl = ctk.CTkLabel(yan, text="", justify="left", anchor="w")
        self.kullanici_lbl.grid(row=2, column=0, padx=20, pady=(10, 6), sticky="w")

        ctk.CTkButton(yan, text="➕ Yeni Liste", command=self.yeni_liste).grid(
            row=3, column=0, padx=20, pady=(4, 4), sticky="ew")

        ctk.CTkLabel(
            yan, text="📂 Geçmiş Listeler", text_color=CYAN,
            font=ctk.CTkFont(size=14, weight="bold"),
        ).grid(row=4, column=0, padx=20, pady=(14, 4), sticky="w")

        self.gecmis_cerceve = ctk.CTkScrollableFrame(yan, fg_color="transparent")
        self.gecmis_cerceve.grid(row=5, column=0, padx=8, pady=0, sticky="nsew")
        yan.grid_columnconfigure(0, weight=1)

        self.klasor_lbl = ctk.CTkLabel(
            yan, text="", text_color="gray", wraplength=220, justify="left", anchor="w")
        self.klasor_lbl.grid(row=6, column=0, padx=20, pady=(8, 0), sticky="w")

        alt = ctk.CTkFrame(yan, fg_color="transparent")
        alt.grid(row=7, column=0, padx=20, pady=12, sticky="ew")
        alt.grid_columnconfigure((0, 1), weight=1)
        ctk.CTkButton(alt, text="📁 Klasör", width=100, fg_color="#334155",
                      command=self.klasor_degistir).grid(row=0, column=0, padx=(0, 4), sticky="ew")
        ctk.CTkButton(alt, text="👤 Profil", width=100, fg_color="#334155",
                      command=self.profil_ac).grid(row=0, column=1, padx=(4, 0), sticky="ew")

        # Sağ panel
        ana = ctk.CTkFrame(self, fg_color="transparent")
        ana.grid(row=0, column=1, sticky="nsew", padx=20, pady=16)
        ana.grid_columnconfigure(0, weight=1)
        ana.grid_rowconfigure(3, weight=1)

        self.baslik_lbl = ctk.CTkLabel(
            ana, text="", text_color=CYAN, font=ctk.CTkFont(size=22, weight="bold"))
        self.baslik_lbl.grid(row=0, column=0, sticky="w")

        self.tarih_lbl = ctk.CTkLabel(ana, text="", text_color="gray")
        self.tarih_lbl.grid(row=1, column=0, sticky="w")

        self.durum_lbl = ctk.CTkLabel(ana, text="")
        self.durum_lbl.grid(row=2, column=0, sticky="w", pady=(0, 6))

        self.urun_cerceve = ctk.CTkScrollableFrame(ana, label_text="🛒 SEPETİNİZ",
                                                   label_text_color=CYAN)
        self.urun_cerceve.grid(row=3, column=0, sticky="nsew")

        # Ürün ekleme satırı
        ekle = ctk.CTkFrame(ana, fg_color="transparent")
        ekle.grid(row=4, column=0, sticky="ew", pady=(10, 0))
        ekle.grid_columnconfigure(0, weight=1)

        self.ad_entry = ctk.CTkEntry(ekle, placeholder_text="Ürün adı")
        self.ad_entry.grid(row=0, column=0, sticky="ew", padx=(0, 8))
        self.miktar_entry = ctk.CTkEntry(ekle, placeholder_text="Adet", width=80)
        self.miktar_entry.grid(row=0, column=1, padx=(0, 8))
        ctk.CTkButton(ekle, text="Ekle", width=90, fg_color=YESIL, hover_color="#248a38",
                      command=self.urun_ekle).grid(row=0, column=2)

        self.ad_entry.bind("<Return>", lambda e: self.miktar_entry.focus())
        self.miktar_entry.bind("<Return>", lambda e: self.urun_ekle())

        # Alt satır: mesaj + kaydet
        alt = ctk.CTkFrame(ana, fg_color="transparent")
        alt.grid(row=5, column=0, sticky="ew", pady=(10, 0))
        alt.grid_columnconfigure(0, weight=1)

        self.mesaj_lbl = ctk.CTkLabel(alt, text="", anchor="w")
        self.mesaj_lbl.grid(row=0, column=0, sticky="w")
        ctk.CTkButton(alt, text="💾 Sepeti Kaydet", command=self.kaydet).grid(row=0, column=1)

    # ----- Ekranı yenileme -----
    def yenile(self):
        self.yenile_kullanici()
        self.yenile_gecmis()
        self.yenile_panel()

    def yenile_kullanici(self):
        k = self.ayarlar["kullanici"]
        if k["ad"]:
            satir = f"Merhaba, {k['ad']} {k['soyad']} 👋"
            ek = " · ".join(x for x in [f"{k['yas']} yaş" if k["yas"] else "", k["sehir"]] if x)
            if ek:
                satir += f"\n{ek}"
        else:
            satir = "Merhaba! 👋"
        self.kullanici_lbl.configure(text=satir)

        klasor = self.ayarlar["kayit_klasoru"]
        self.klasor_lbl.configure(
            text=f"txt klasörü:\n{klasor}" if klasor else "txt klasörü: seçilmedi")

    def yenile_gecmis(self):
        for w in self.gecmis_cerceve.winfo_children():
            w.destroy()

        if not self.listeler:
            ctk.CTkLabel(self.gecmis_cerceve, text="Henüz kayıtlı liste yok.",
                         text_color=KIRMIZI).pack(anchor="w", padx=8, pady=4)
            return

        for l in sorted(self.listeler, key=lambda x: x["id"], reverse=True):
            aktif_mi = l["id"] == self.aktif["id"]
            ctk.CTkButton(
                self.gecmis_cerceve,
                text=f"{l['olusturma']}\n{len(l['urunler'])} ürün",
                anchor="w",
                fg_color="#1d4ed8" if aktif_mi else "#1e293b",
                hover_color="#334155",
                command=lambda i=l["id"]: self.liste_ac(i),
            ).pack(fill="x", padx=4, pady=3)

    def yenile_panel(self):
        v = self.aktif
        gun = v["olusturma"].split(" ")[0]
        self.baslik_lbl.configure(text=f"{gun} tarihli alışveriş listesi")
        self.tarih_lbl.configure(
            text=f"Oluşturma: {v['olusturma']}   •   Son düzenleme: {v['guncelleme']}")

        if not self.kayitli_mi():
            self.durum_lbl.configure(text="● Henüz kaydedilmedi", text_color=KIRMIZI)
        elif self.degisti:
            self.durum_lbl.configure(text="● Kaydedilmemiş değişiklikler var", text_color=KIRMIZI)
        else:
            self.durum_lbl.configure(text="● Kaydedildi", text_color=YESIL)

        for w in self.urun_cerceve.winfo_children():
            w.destroy()

        if not v["urunler"]:
            ctk.CTkLabel(self.urun_cerceve, text="Sepetin bomboş, henüz bir şey eklemedin.",
                         text_color=KIRMIZI).pack(pady=20)
            return

        for ad, miktar in v["urunler"].items():
            satir = ctk.CTkFrame(self.urun_cerceve)
            satir.pack(fill="x", pady=3, padx=2)

            ctk.CTkLabel(satir, text=f"• {ad}", text_color=BEYAZ, anchor="w").pack(
                side="left", padx=10, pady=6, expand=True, fill="x")
            ctk.CTkButton(satir, text="✕", width=32, fg_color=KIRMIZI, hover_color="#b4373b",
                          command=lambda a=ad: self.urun_sil(a)).pack(side="right", padx=(4, 8))
            ctk.CTkButton(satir, text="+", width=32, fg_color=YESIL, hover_color="#248a38",
                          command=lambda a=ad: self.miktar_degistir(a, 1)).pack(side="right", padx=2)
            ctk.CTkLabel(satir, text=f"{miktar} adet", width=70).pack(side="right", padx=4)
            ctk.CTkButton(satir, text="−", width=32, fg_color="#334155",
                          command=lambda a=ad: self.miktar_degistir(a, -1)).pack(side="right", padx=2)

    def mesaj(self, metin, renk=BEYAZ):
        self.mesaj_lbl.configure(text=metin, text_color=renk)

    # ----- Liste işlemleri -----
    def kayitli_mi(self):
        return any(l["id"] == self.aktif["id"] for l in self.listeler)

    def degisiklik_sor(self):
        """Kaydedilmemiş değişiklik varsa sorar. Devam edilebilirse True döner."""
        if not self.degisti:
            return True
        cevap = messagebox.askyesnocancel(
            "Kaydedilmemiş değişiklikler",
            "Bu listede kaydedilmemiş değişiklikler var. Kaydedilsin mi?")
        if cevap is None:  # vazgeç
            return False
        if cevap:  # evet
            return self.kaydet()
        return True  # hayır, kaydetmeden devam

    def yeni_liste(self):
        if not self.degisiklik_sor():
            return
        self.aktif = yeni_liste_verisi()
        self.degisti = False
        self.mesaj("")
        self.yenile()

    def liste_ac(self, liste_id):
        if liste_id == self.aktif["id"]:
            return
        if not self.degisiklik_sor():
            return
        for l in self.listeler:
            if l["id"] == liste_id:
                self.aktif = copy.deepcopy(l)  # düzenleme kayıtlı veriden bağımsız
                break
        self.degisti = False
        self.mesaj("")
        self.yenile()

    def urun_ekle(self):
        ad = self.ad_entry.get().strip()
        miktar_metin = self.miktar_entry.get().strip() or "1"

        if not ad:
            self.mesaj("Ürün adı boş olamaz.", KIRMIZI)
            return
        if not miktar_metin.isdigit() or int(miktar_metin) <= 0:
            self.mesaj("Lütfen geçerli bir sayı giriniz (0'dan büyük).", KIRMIZI)
            return

        miktar = int(miktar_metin)
        urunler = self.aktif["urunler"]
        # Büyük/küçük harf farkını eşitle (Süt / süt)
        mevcut = next((k for k in urunler if k.casefold() == ad.casefold()), ad)
        urunler[mevcut] = urunler.get(mevcut, 0) + miktar

        self.degisti = True
        self.ad_entry.delete(0, "end")
        self.miktar_entry.delete(0, "end")
        self.ad_entry.focus()
        self.mesaj(f"{mevcut} başarıyla eklendi!", YESIL)
        self.yenile_panel()

    def miktar_degistir(self, ad, fark):
        urunler = self.aktif["urunler"]
        if ad not in urunler:
            return
        yeni = urunler[ad] + fark
        if yeni <= 0:
            del urunler[ad]
            self.mesaj(f"{ad} sepetten tamamen kaldırıldı.", KIRMIZI)
        else:
            urunler[ad] = yeni
            self.mesaj(f"{ad} miktarı: {yeni}", YESIL if fark > 0 else KIRMIZI)
        self.degisti = True
        self.yenile_panel()

    def urun_sil(self, ad):
        if ad in self.aktif["urunler"]:
            del self.aktif["urunler"][ad]
            self.degisti = True
            self.mesaj(f"{ad} sepetten tamamen kaldırıldı.", KIRMIZI)
            self.yenile_panel()

    # ----- Kayıt -----
    def klasor_sec(self):
        baslangic = self.ayarlar["kayit_klasoru"] or os.path.expanduser("~")
        klasor = filedialog.askdirectory(
            title="Not defteri (.txt) dosyaları nereye kaydedilsin?",
            initialdir=baslangic, parent=self)
        if klasor:
            self.ayarlar["kayit_klasoru"] = klasor
            ayarlari_kaydet(self.ayarlar)
            self.yenile_kullanici()
        return klasor

    def klasor_hazir_mi(self):
        """Kayıtlı klasör geçerliyse döndürür, değilse kullanıcıyı uyarıp seçtirir."""
        klasor = self.ayarlar["kayit_klasoru"]
        if klasor and os.path.isdir(klasor):
            return klasor
        messagebox.showinfo(
            "Kayıt klasörü seçilmedi",
            "Not defteri (.txt) dosyalarının nereye kaydedileceğini seçmen gerekiyor.",
            parent=self)
        return self.klasor_sec()

    def klasor_degistir(self):
        eski = self.ayarlar["kayit_klasoru"]
        yeni = self.klasor_sec()
        if not yeni or yeni == eski or not self.listeler:
            return
        if messagebox.askyesno(
                "Mevcut listeler",
                "Kayıtlı tüm listelerin txt dosyaları yeni klasöre de yazılsın mı?",
                parent=self):
            try:
                for l in self.listeler:
                    txt_yaz(l, yeni)
                self.mesaj("Tüm listeler yeni klasöre yazıldı.", YESIL)
            except OSError as e:
                messagebox.showerror("Hata", f"Dosyalar yazılamadı:\n{e}", parent=self)

    def kaydet(self):
        """Listeyi kaydeder. Başarılıysa True döner."""
        if not self.aktif["urunler"] and not self.kayitli_mi():
            self.mesaj("Boş liste kaydedilmez, önce ürün ekle.", KIRMIZI)
            return False

        self.aktif["guncelleme"] = simdi()
        kopya = copy.deepcopy(self.aktif)
        for i, l in enumerate(self.listeler):
            if l["id"] == kopya["id"]:
                self.listeler[i] = kopya
                break
        else:
            self.listeler.append(kopya)

        try:
            json_kaydet(self.listeler)
        except OSError as e:
            messagebox.showerror("Hata", f"Liste kaydedilemedi:\n{e}", parent=self)
            return False

        self.degisti = False
        sonuc, renk = "Liste kaydedildi! (JSON + not defteri)", YESIL

        klasor = self.klasor_hazir_mi()
        if not klasor:
            messagebox.showwarning(
                "Klasör seçilmedi",
                "Klasör seçmediğin için liste sadece uygulamaya kaydedildi, "
                ".txt dosyası oluşturulmadı. Bir sonraki kayıtta tekrar sorulacak.",
                parent=self)
            sonuc, renk = "Liste kaydedildi, ama txt oluşturulmadı (klasör seçilmedi).", KIRMIZI
        else:
            try:
                txt_yaz(kopya, klasor)
            except OSError as e:
                messagebox.showerror("Hata", f"txt yazılamadı:\n{e}", parent=self)
                sonuc, renk = "Liste kaydedildi, ama txt yazılamadı.", KIRMIZI

        self.mesaj(sonuc, renk)
        self.yenile()
        return True

    # ----- Profil -----
    def profil_ac(self):
        ProfilPenceresi(self, self.ayarlar["kullanici"])

    def profil_kaydet(self, kullanici):
        self.ayarlar["kullanici"] = kullanici
        ayarlari_kaydet(self.ayarlar)
        self.yenile_kullanici()

    # ----- Kapanış -----
    def kapat(self):
        if self.degisiklik_sor():
            self.destroy()


if __name__ == "__main__":
    ListlyApp().mainloop()
