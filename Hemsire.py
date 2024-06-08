from personel import *# personel modülündeki tüm sınıfları içeri aktarıyoruz

class Hemsire(personel):
    def __init__(self, personel_no, ad, soyad, departman, maas, calisma_saati, sertifika, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)# Üst sınıfın (personel) yapıcı metodunu çağırıyoruz
        self.calisma_saati=calisma_saati
        self.sertifika=sertifika
        self.hastane=hastane
    
     # Calisma saati bilgisini döndüren get metodu    
    def get_calisma_saati(self):
        return self.calisma_saati
     # Calisma saati bilgisini ayarlayan set metodu
    def set_calisma_saati(self,calisma_saati):
        
        self.calisma_saati=calisma_saati
        return self.calisma_saati
    
     # sertifika bilgisini döndüren get metodu        
    def get_sertifika(self):
        return self.sertifika
    # sertifika bilgisini ayarlayan set metodu
    def set_sertifika(self,sertifika):
       
       self.sertifika=sertifika
       return self.sertifika
   
     # hastane bilgisini döndüren get metodu        
    def get_hastane(self):
        return self.hastane
    # hastane bilgisini ayarlayan set metodu
    def set_hastane(self,hastane):
       
       self.hastane=hastane
       return self.hastane
    
    #Hemsire nesnesini yazdırmak için  __str__ metodunu kulanıyoruz
    def __str__(self):
        return str(super().__str__())+str(print(f"calisma saati:{self.calisma_saati}sertifika:{self.sertifika}hastane:{self.hastane} "))
    
     # Maas'ı arttıran metodu tanımlıyoruz
    def maas_artir(self,calisma_saati):
        if calisma_saati<4:
            print("maaş artirmak için günde en az 5 saat çalismaniz gerekir.")
            
        else :
            yenimaas=self.maas*(calisma_saati/10)+self.maas#çalışma saati oranına göre maası artırıyoruz
            print("yeni maas:",yenimaas)
            
