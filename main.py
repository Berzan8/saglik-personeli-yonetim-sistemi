from personel import personel
from Doktor import Doktor
from Hemsire import Hemsire
from Hasta import Hasta



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
    

if __name__ == "__main__":
    main()