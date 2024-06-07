from personel import personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta
import pandas as pd

def main():
    try:
        # Personel nesneleri
        personel1 = personel(1, "Ahmet", "Yılmaz", "Muhasebe", 5000)
        personel2 = personel(2, "Mehmet", "Öztürk", "İnsan Kaynakları", 6000)
        personel1.__str__()
        personel2.__str__()

        # Doktor nesneleri
        doktor1 = Doktor(3, "Ali", "Kara", "Kardiyoloji", 8000, "Kardiyolog", 10, "Merkez Hastanesi")
        doktor2 = Doktor(4, "Ayşe", "Demir", "Nöroloji", 9000, "Nörolog", 7, "Şehir Hastanesi")
        doktor3 = Doktor(5, "Fatma", "Şahin", "Ortopedi", 8500, "Ortopedist", 5, "Devlet Hastanesi")
        doktor1.__str__()
        doktor2.__str__()
        doktor3.__str__()

        # Hemşire nesneleri
        hemsire1 = Hemsire(6, "Elif", "Kaya", "Acil", 4000, 40, "Yoğun Bakım Sertifikası", "Merkez Hastanesi")
        hemsire2 = Hemsire(7, "Serkan", "Yıldırım", "Ameliyathane", 4500, 45, "Ameliyathane Sertifikası", "Şehir Hastanesi")
        hemsire3 = Hemsire(8, "Sevil", "Çelik", "Pediatri", 4200, 40, "Pediatri Sertifikası", "Devlet Hastanesi")
        hemsire1.__str__()
        hemsire2.__str__()
        hemsire3.__str__()

        # Hasta nesneleri
        hasta1 = Hasta(1, "Zeynep", "Çakır", "1995-02-15", "Grip", ["İlaç Tedavisi"])
        hasta2 = Hasta(2, "Efe", "Aslan", "1988-07-23", "Kırık", ["Alçı", "Fizyoterapi"])
        hasta3 = Hasta(3, "Buse", "Ak", "2000-11-05", "Alerji", ["İlaç Tedavisi"])
        hasta1.__str__()
        hasta2.__str__()
        hasta3.__str__()
    
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
    


# Personel, Doktor, Hemşire ve Hasta nesnelerini içeren listeler
personeller = [
    {"personel_no": 1, "ad": "Ahmet", "soyad": "Yılmaz", "departman": "Muhasebe", "maas": 5000},
    {"personel_no": 2, "ad": "Mehmet", "soyad": "Öztürk", "departman": "İnsan Kaynakları", "maas": 6000},
]

doktorlar = [
    {"personel_no": 3, "ad": "Ali", "soyad": "Kara", "departman": "Kardiyoloji", "maas": 8000, "uzmanlik": "Kardiyolog", "deneyim_yili": 10, "hastane": "Merkez Hastanesi"},
    {"personel_no": 4, "ad": "Ayşe", "soyad": "Demir", "departman": "Nöroloji", "maas": 9000, "uzmanlik": "Nörolog", "deneyim_yili": 7, "hastane": "Şehir Hastanesi"},
    {"personel_no": 5, "ad": "Fatma", "soyad": "Şahin", "departman": "Ortopedi", "maas": 8500, "uzmanlik": "Ortopedist", "deneyim_yili": 5, "hastane": "Devlet Hastanesi"},
]

hemsireler = [
    {"personel_no": 6, "ad": "Elif", "soyad": "Kaya", "departman": "Acil", "maas": 4000, "calisma_saati": 40, "sertifika": "Yoğun Bakım Sertifikası", "hastane": "Merkez Hastanesi"},
    {"personel_no": 7, "ad": "Serkan", "soyad": "Yıldırım", "departman": "Ameliyathane", "maas": 4500, "calisma_saati": 45, "sertifika": "Ameliyathane Sertifikası", "hastane": "Şehir Hastanesi"},
    {"personel_no": 8, "ad": "Sevil", "soyad": "Çelik", "departman": "Pediatri", "maas": 4200, "calisma_saati": 40, "sertifika": "Pediatri Sertifikası", "hastane": "Devlet Hastanesi"},
]

hastalar = [
    {"hasta_no": 1, "ad": "Zeynep", "soyad": "Çakır", "dogum_tarihi": "1995-02-15", "hastalik": "Grip", "tedavi": ["İlaç Tedavisi"]},
    {"hasta_no": 2, "ad": "Efe", "soyad": "Aslan", "dogum_tarihi": "1988-07-23", "hastalik": "Kırık", "tedavi": ["Alçı", "Fizyoterapi"]},
    {"hasta_no": 3, "ad": "Buse", "soyad": "Ak", "dogum_tarihi": "2000-11-05", "hastalik": "Alerji", "tedavi": ["İlaç Tedavisi"]},
]

# Verilerin DataFrame'e dönüştürülmesi
personel_df = pd.DataFrame(personeller)
doktor_df = pd.DataFrame(doktorlar)
hemsire_df = pd.DataFrame(hemsireler)
hasta_df = pd.DataFrame(hastalar)

# Boş değerler için 0 atama
personel_df.fillna(0, inplace=True)
doktor_df.fillna(0, inplace=True)
hemsire_df.fillna(0, inplace=True)
hasta_df.fillna(0, inplace=True)

# Doktorları uzmanlık alanlarına göre gruplandırarak toplam sayısını hesaplama
uzmanlik_gruplari = doktor_df.groupby("uzmanlik").size()
print("Uzmanlık Alanlarına Göre Doktor Sayıları:")
print(uzmanlik_gruplari)

# 5 yıldan fazla deneyime sahip doktorların toplam sayısını bulma
deneyimli_doktorlar = doktor_df[doktor_df["deneyim_yili"] > 5]
print(f"5 Yıldan Fazla Deneyime Sahip Doktor Sayısı: {len(deneyimli_doktorlar)}")

# Hasta adına göre DataFrame’i alfabetik olarak sıralama
sorted_hasta_df = hasta_df.sort_values(by="ad")
print("Alfabetik Sıraya Göre Hastalar:")
print(sorted_hasta_df)

# Maaşı 7000 TL üzerinde olan personelleri bulma
maasi_yuksek_personeller = personel_df[personel_df["maas"] > 7000]
print("Maaşı 7000 TL Üzerinde Olan Personeller:")
print(maasi_yuksek_personeller)

# Doğum tarihi 1990 ve sonrası olan hastaları gösterme
dogum_tarihi_filtre = hasta_df[hasta_df["dogum_tarihi"] >= "1990-01-01"]
print("Doğum Tarihi 1990 ve Sonrası Olan Hastalar:")
print(dogum_tarihi_filtre)

# Yeni bir DataFrame oluşturma
yeni_df = pd.concat([personel_df[["ad", "soyad", "departman", "maas"]], doktor_df[["uzmanlik", "deneyim_yili"]], hasta_df[["hastalik", "tedavi"]]], axis=1)
print("Yeni DataFrame:")
print(yeni_df)


if __name__ == "__main__":
    main()