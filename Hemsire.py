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
        
        self.calisma_saati=calisma_saati
        return self.calisma_saati
            
    def get_sertifika(self):
        return self.sertifika
    
    def set_sertifika(self,sertifika):
       
       self.sertifika=sertifika
       return self.sertifika
            
    def get_hastane(self):
        return self.hastane
    
    def set_hastane(self,hastane):
       
       self.hastane=hastane
       return self.hastane
    
    def __str__(self):
        return str(super().__str__())+str(print(f"calisma saati:{self.calisma_saati}sertifika:{self.sertifika}hastane:{self.hastane} "))
    
    def maas_artir(self,calisma_saati):
        if calisma_saati<4:
            print("maaş artirmak için günde en az 5 saat çalismaniz gerekir.")
            
        else :
            yenimaas=self.maas*(calisma_saati/10)+self.maas
            print("yeni maas:",yenimaas)
            
