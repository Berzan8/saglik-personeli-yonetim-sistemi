from personel import *

class Hemsire(personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.calisma_saati=calisma_saati
        self.sertifika=sertifika
        self.hastane=hastane
        
    def get_calisma_saati(self):
        return self.calisma_saati
    
    def set_calisma_saati(self,calisma_saati):
        try:
            if isinstance(calisma_saati,int) and calisma_saati.strip():
                self.calisma_saati = calisma_saati
            else:
                raise ValueError("Lütfen rakamlardan olusan çalişma  saatinizi giriniz!!...")
        except ValueError as e:
            print(f"Hata: {e}")
            
    def get_sertifika(self):
        return self.sertifika
    
    def set_sertifika(self,sertifika):
        try:
            if isinstance(sertifika,str) and sertifika.strip():
                self.sertifika = sertifika
            else:
                raise ValueError("Lütfen harflerden olusan sertifikanizi giriniz!!...")
        except ValueError as e:
            print(f"Hata: {e}")
            
    def get_hastane(self):
        return self.hastane
    
    def set_hastane(self,hastane):
        try:
            if isinstance(hastane,str) and hastane.strip():
                self.hastane = hastane
            else:
                raise ValueError("Lütfen harflerden olusan hastane adini giriniz!!...")
        except ValueError as e:
            print(f"Hata: {e}")
    
    def __str__(self, personel_no, ad, soyad, departman, maas,calisma_saati,sertifika,hastane):
        return print(f"{super().__str__(personel_no, ad, soyad, departman, maas)}calisma saati:{calisma_saati}sertifika:{sertifika}hastane:{hastane} ")
    
    def maas_artir(self,calisma_saati):
        if calisma_saati<4:
            print("maaş artirmak için günde en az 5 saat çalismaniz gerekir.")
            
        else :
            yenimaas=self.maas*(calisma_saati/10)+self.maas
            print("yeni maas:",yenimaas)