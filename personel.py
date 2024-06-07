class personel:
    def __init__(self,personel_no, ad, soyad, departman, maas):
        self.personel_no=personel_no
        self.ad=ad
        self.soyad=soyad
        self.departman=departman
        self.maas=maas
        
    def get_personel_no(self):
        return self.personel_no
    
    def set_personel_no(self,personel_no):
    
        self.personel_no = personel_no
        return self.personel_no
            
    
    def get_ad(self):
        return self.ad
    
    def set_ad(self,ad):
        
        self.ad=ad
        return self.ad
    
    def get_soyad(self):
        return self.soyad
    
    def set_soyad(self,soyad):
       
       self.soyad=soyad
       return self.soyad
                    
    def get_departman(self):
        return self.departman
    
    def set_departman(self,departman):
        
        self.departman=departman
        return self.departman
            
    def get_maas(self):
        return self.maas
    
    def set_maas(self,maas):
        
        self.maas=maas
        return self.maas
        
    def __str__(self,personel_no,ad,soyad,departman,maas):
        
        return print(f"personel_numarasi:{personel_no} \nadi:{ad} \nsoyadi:{soyad} \ndepartman:{departman} \n maasi:{maas}")
