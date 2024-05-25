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
        try:
            if isinstance(personel_no, int) and personel_no.strip():
                self.personel_no = personel_no
            else:
                raise ValueError("Lütfen rakamlardan olusan personel numaranizi giriniz!!...")
        except ValueError as e:
            print(f"Hata: {e}")
    
    def get_ad(self):
        return self.ad
    
    def set_ad(self,ad):
        try:
            if isinstance(ad, str) and ad.strip():
                self.ad=ad
            else:
                raise ValueError("adin içinde rakam bulunmaz!!...")
        except ValueError as e:
            print(f"Hata: {e}")
    
    def get_soyad(self):
        return self.soyad
    
    def set_soyad(self,soyad):
        try:
            if isinstance(soyad,str) and soyad.strip():
                self.soyad = soyad
            else:
                raise ValueError("soyadın içinde rakam bulunmaz!!...")
        except ValueError as e:
            print(f"Hata: {e}")
            
    def get_departman(self):
        return self.departman
    
    def set_departman(self,departman):
        try:
            if isinstance(departman, str) and departman.strip():
                self.departman = departman
            else:
                raise ValueError("departman adini eksik ya da hatali girdiniz!!...")
        except ValueError as e:
            print(f"Hata: {e}")
            
    def get_maas(self):
        return self.maas
    
    def set_maas(self,maas):
        try:
            if isinstance(maas, int) and maas.strip():
                self.maas = maas
            else:
                raise ValueError("Lütfen rakamlardan olusan maasinizi giriniz!!...")
        except ValueError as e:
            print(f"Hata: {e}")
        
    def __str__(self,personel_no,ad,soyad,departman,maas):
        
        return print(f"personel_numarasi:{personel_no} \nadi:{ad} \nsoyadi:{soyad} \ndepartman:{departman} \n maasi:{maas} \n")
