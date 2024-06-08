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
        
        # Tüm nesneleri bir listeye ekleyelim
        tum_nesneler = [personel1, personel2, doktor1, doktor2, doktor3, hemsire1, hemsire2, hemsire3, hasta1, hasta2, hasta3]
        
        # Pandas DataFrame oluşturma
        data = {
            "personel_no": [p.get_personel_no() if isinstance(p, personel) else 0 for p in tum_nesneler],
            "ad": [p.get_ad() for p in tum_nesneler],
            "soyad": [p.get_soyad() for p in tum_nesneler],
            "departman": [p.get_departman() if isinstance(p, personel) else "Hasta" for p in tum_nesneler],
            "maas": [p.get_maas() if isinstance(p, personel) else 0 for p in tum_nesneler],
            "uzmanlik": [p.get_uzmanlik() if isinstance(p, Doktor) else 0 for p in tum_nesneler],
            "deneyim_yili": [p.get_deneyim_yili() if isinstance(p, Doktor) else 0 for p in tum_nesneler],
            "hastane": [p.get_hastane() if isinstance(p, (Doktor, Hemsire)) else 0 for p in tum_nesneler],
            "calisma_saati": [p.get_calisma_saati() if isinstance(p, Hemsire) else 0 for p in tum_nesneler],
            "sertifika": [p.get_sertifika() if isinstance(p, Hemsire) else 0 for p in tum_nesneler],
            "hasta_no": [p.get_hasta_no() if isinstance(p, Hasta) else 0 for p in tum_nesneler],
            "dogum_tarihi": [p.get_dogum_tarihi() if isinstance(p, Hasta) else 0 for p in tum_nesneler],
            "hastalik": [p.get_hastalik() if isinstance(p, Hasta) else 0 for p in tum_nesneler],
            "tedavi": [p.get_tedavi() if isinstance(p, Hasta) else 0 for p in tum_nesneler],
        }
     
        df = pd.DataFrame(data)

        # Boş olan değişken değerleri için 0 atama
        df.fillna(0, inplace=True)

        # Doktorları uzmanlık alanlarına göre gruplandırarak toplam sayısını hesaplama ve yazdırma
        doktor_uzmanlik_gruplama = df[df["uzmanlik"] != 0].groupby("uzmanlik").size()
        print("\nDoktorların Uzmanlık Alanlarına Göre Dağılımı:")
        print(doktor_uzmanlik_gruplama)

        # 5 yıldan fazla deneyime sahip doktorların toplam sayısını bulma
        deneyimli_doktor_sayisi = df[(df["deneyim_yili"] > 5)].shape[0]
        print(f"\n5 Yıldan Fazla Deneyime Sahip Doktor Sayısı: {deneyimli_doktor_sayisi}")

        # Hasta adına göre DataFrame’i alfabetik olarak sıralama ve yazdırma
        df_hasta_adi_ile = df[df["departman"] == "Hasta"].sort_values("ad")
        print("\nHasta Adına Göre Sıralanmış DataFrame:")
        print(df_hasta_adi_ile)

        # Maaşı 7000 TL üzerinde olan personelleri bulma ve yazdırma
        yuksek_maasli_personeller = df[df["maas"] > 7000]
        print("\nMaaşı 7000 TL Üzerinde Olan Personeller:")
        print(yuksek_maasli_personeller)

        # Doğum tarihi 1990 ve sonrası olan hastaları gösterme
        df["dogum_tarihi"] = pd.to_datetime(df["dogum_tarihi"], errors='coerce')
        yeni_dogmus_hastalar = df[(df["dogum_tarihi"] >= "1990-01-01")]
        print("\nDoğum Tarihi 1990 ve Sonrası Olan Hastalar:")
        print(yeni_dogmus_hastalar)

        # Yeni bir DataFrame elde etme ve yazdırma
        yeni_df = df[["ad", "soyad", "departman", "maas", "uzmanlik", "deneyim_yili", "hastalik", "tedavi"]]
        print("\nYeni DataFrame:")
        print(yeni_df)
    
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
    

if __name__ == "__main__":
    main()