from personel import personel # personel sınıfını içeri aktarıyoruz

class Doktor(personel):
    def __init__(self, personel_no, ad, soyad, departman, maas,uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas) # Üst sınıfın (personel) yapıcı metodunu çağırıyoruz
        self.uzmanlik=uzmanlik
        self.deneyim_yili=deneyim_yili
        self.hastane=hastane
    
    # Uzmanlık alanını döndüren get metodu    
    def get_uzmanlik(self):
        return self.uzmanlik
    # Uzmanlık alanını ayarlayan set metodu
    def set_uzmanlik(self,uzmanlik):
        
        self.uzmanlik=uzmanlik
        return uzmanlik
    
    #deneyim yılını döndüren get metodu        
    def get_deneyim_yili(self):
        return self.deneyim_yili
    # deneyim yılını ayarlayan set metodu
    def set_deneyim_yili(self,deneyim_yili):
        
        self.deneyim_yili=deneyim_yili
        return self.deneyim_yili
    
    #hastane adını döndüren get metodu        
    def get_hastane(self):
        return self.hastane
    #hastane adını ayarlayan set metodu
    def set_hastane(self,hastane):
        
        self.hastane=hastane
        return hastane
    
     #Doktor nesnesini yazdıran __str__ metodu
    def __str__(self):
        return str( super().__str__())+str(print(f" uzmanlik:{self.uzmanlik}\ndeneyim yili:{self.deneyim_yili}\n hastane:{self.hastane}"))
    
    # Maas'ı arttıran metodu tanımlıyoruz
    def maas_artir(self,oran):
        yeni_maas=self.set_maas(self.get_maas() * (1 + oran))
        return print("yeni maasiniz:",yeni_maas)# Orana göre maaşı artırıyoruz
    