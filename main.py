from personel import personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta

def main():
    try:
        # Personel nesneleri
        personel1 = Personel(1, "Ahmet", "Yılmaz", "Muhasebe", 5000)
        personel2 = Personel(2, "Mehmet", "Öztürk", "İnsan Kaynakları", 6000)
        print(personel1)
        print(personel2)

        # Doktor nesneleri
        doktor1 = Doktor(3, "Ali", "Kara", "Kardiyoloji", 8000, "Kardiyolog", 10, "Merkez Hastanesi")
        doktor2 = Doktor(4, "Ayşe", "Demir", "Nöroloji", 9000, "Nörolog", 7, "Şehir Hastanesi")
        doktor3 = Doktor(5, "Fatma", "Şahin", "Ortopedi", 8500, "Ortopedist", 5, "Devlet Hastanesi")
        print(doktor1)
        print(doktor2)
        print(doktor3)

        # Hemşire nesneleri
        hemsire1 = Hemsire(6, "Elif", "Kaya", "Acil", 4000, 40, "Yoğun Bakım Sertifikası", "Merkez Hastanesi")
        hemsire2 = Hemsire(7, "Serkan", "Yıldırım", "Ameliyathane", 4500, 45, "Ameliyathane Sertifikası", "Şehir Hastanesi")
        hemsire3 = Hemsire(8, "Sevil", "Çelik", "Pediatri", 4200, 40, "Pediatri Sertifikası", "Devlet Hastanesi")
        print(hemsire1)
        print(hemsire2)
        print(hemsire3)

        # Hasta nesneleri
        hasta1 = Hasta(1, "Zeynep", "Çakır", "1995-02-15", "Grip", ["İlaç Tedavisi"])
        hasta2 = Hasta(2, "Efe", "Aslan", "1988-07-23", "Kırık", ["Alçı", "Fizyoterapi"])
        hasta3 = Hasta(3, "Buse", "Ak", "2000-11-05", "Alerji", ["İlaç Tedavisi"])
        print(hasta1)
        print(hasta2)
        print(hasta3)
    
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    main()