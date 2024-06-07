from personel import personel
class Doktor(personel):
    def __init__(self, personel_no, ad, soyad, departman, maas,uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.uzmanlik=uzmanlik
        self.deneyim_yili=deneyim_yili
        self.hastane=hastane
        
    def get_uzmanlik(self):
        return self.uzmanlik
    
    def set_uzmanlik(self,uzmanlik):
        
        self.uzmanlik=uzmanlik
        return uzmanlik
            
    def get_deneyim_yili(self):
        return self.deneyim_yili
    
    def set_deneyim_yili(self,deneyim_yili):
        
        self.deneyim_yili=deneyim_yili
        return self.deneyim_yili
            
    def get_hastane(self):
        return self.hastane
    
    def set_hastane(self,hastane):
        
        self.hastane=hastane
        return hastane
    
    def __str__(self):
        return print(f"{super().__str__()} uzmanlik:{self.uzmanlik}\ndeneyim yili:{self.deneyim_yili}\n hastane:{self.hastane}")
    
    def maas_artir(self,oran):
        yeni_maas=self.set_maas(self.get_maas() * (1 + oran))
        return print("yeni maasiniz:",yeni_maas)
    
yeni=Doktor(12,"berzan","erdal","kbb",19000,"kulak",3,"cigli")
yeni.__str__()