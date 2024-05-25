from personel import *
class Doktor(personel):
    def __init__(self, personel_no, ad, soyad, departman, maas,uzmanlik, deneyim_yili, hastane):
        super().__init__(personel_no, ad, soyad, departman, maas)
        self.uzmanlik=uzmanlik
        self.deneyim_yili=deneyim_yili
        self.hastane=hastane
        
    def get_uzmanlik(self):
        return self.uzmanlik
    
    def set_uzmanlik(self,uzmanlik):
        try:
            if isinstance(uzmanlik,str) and uzmanlik.strip():
                self.uzmanlik = uzmanlik
            else:
                raise ValueError("girilen uzmanlik bulunmadi!!...")
        except ValueError as e:
            print(f"Hata: {e}")
            
    def get_deneyim_yili(self):
        return self.deneyim_yili
    
    def set_deneyim_yili(self,deneyim_yili):
        try:
            if isinstance(deneyim_yili,int) and deneyim_yili.strip():
                self.uzmanlik = deneyim_yili
            else:
                raise ValueError("girilen deneyim yili geçersiz!!...")
        except ValueError as e:
            print(f"Hata: {e}")
            
    def get_hastane(self):
        return self.hastane
    
    def set_hastane(self,hastane):
        try:
            if isinstance(hastane,int) and hastane.strip():
                self.hastane = hastane
            else:
                raise ValueError("girilen deneyim yili geçersiz!!...")
        except ValueError as e:
            print(f"Hata: {e}")
    
    def __str__(self, personel_no, ad, soyad, departman, maas,uzmanlik,deneyim_yili,hastane):
        return print(f"{super().__str__(personel_no, ad, soyad, departman, maas)} uzmanlik:{uzmanlik}\ndeneyim yili:{deneyim_yili}\n hastane:{hastane}")
    
    def maas_artir(self,deneyim_yili):
        if deneyim_yili<0:
            print("maaş artirmak için en az bir yil çalismaniz gerekir.")
            
        else :
            yenimaas=self.maas*(deneyim_yili/10)+self.maas
            print("yeni maas:",yenimaas)
doktorlar=Doktor(12,"kar","tanesi","tor",23000,"red",3,"veli")
doktorlar.maas_artir(3)