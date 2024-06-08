class personel:
    # __init__ metodu sınıfın bir örneği oluşturulduğunda çalışan yapıcı metoddur
    def __init__(self,personel_no, ad, soyad, departman, maas):
        self.personel_no=personel_no
        self.ad=ad
        self.soyad=soyad
        self.departman=departman
        self.maas=maas
    
    # Personel numarasını döndüren get metodu   
    def get_personel_no(self):
        return self.personel_no
    #Personel numarasını ayarlayan set meodu
    def set_personel_no(self,personel_no):
    
        self.personel_no = personel_no
        return self.personel_no
            
    # Personel adını döndüren get metodu 
    def get_ad(self):
        return self.ad
    #Personel adını ayarlayan set meodu
    def set_ad(self,ad):
        
        self.ad=ad
        return self.ad
    
    # Personel soyadını döndüren get metodu 
    def get_soyad(self):
        return self.soyad
    #Personel soyadını ayarlayan set meodu
    def set_soyad(self,soyad):
       
       self.soyad=soyad
       return self.soyad
   
    # Personel departmanını döndüren get metodu                 
    def get_departman(self):
        return self.departman
    #Personel departmanını ayarlayan set meodu
    def set_departman(self,departman):
        
        self.departman=departman
        return self.departman
    
    # Personel maasını döndüren get metodu        
    def get_maas(self):
        return self.maas
    #Personel maasını ayarlayan set meodu
    def set_maas(self,maas):
        
        self.maas=maas
        return self.maas
    
    # Nesneyi yazdırmak için kullanılan __str__ metodu   
    def __str__(self):
        
        return print(f"personel_numarasi:{self.personel_no} \nadi:{self.ad} \nsoyadi:{self.soyad} \ndepartman:{self.departman} \nmaasi:{self.maas}")
