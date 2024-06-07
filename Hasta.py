import datetime

class Hasta:
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi):
        self.hasta_no=hasta_no
        self.ad=ad
        self.soyad=soyad
        self.dogum_tarihi=dogum_tarihi
        self.hastalik=hastalik
        self.tedavi=tedavi
        
    def get_hasta_no(self):
        return self.hasta_no
    def set_hasta_no(self,hasta_no):
        
        self.hasta_no=hasta_no
        return self.hasta_no     
    
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
    
    def get_dogum_tarihi(self):
        return self.dogum_tarihi
    
    def set_dogum_tarihi(self,dogum_tarihi):
        try:
            
            girilen_tarih = datetime.strptime(dogum_tarihi, "%Y-%m-%d")
            print(f"Girilen tarih: {girilen_tarih}")
            
        except ValueError:
            print("Geçersiz tarih formatı. Lütfen 'YYYY-MM-DD' formatında bir tarih girin.")
    
    def get_hastalik(self):
        return self.hastalik
    
    def set_hastalik(self,hastalik):
        
        self.hastalik=hastalik
        return self.hastalik
            
    def get_tedavi(self):
        return self.soyad
    
    def set_tedavi(self,tedavi):
       
       self.tedavi=tedavi
       return self.tedavi
            
    def __str__(self):
        
        return print(f"hasta_no:{self.hasta_no}\nad:{self.ad}soyad:{self.soyad}\ndogum_tarihi:{self.dogum_tarihi}\nhastalik:{self.hastalik}\ntedavi:{self.tedavi}")
    
    def tedavi_suresi_hesapla(baslangic,bitis):
        baslangic=input("tedavi baslangic tarihinizi 'YYYY-MM-DD' şeklinde giriniz ")
        try:
             girilen_tarih = datetime.strptime(baslangic, "%Y-%m-%d")
             print(f"Girilen tarih: {girilen_tarih}")
        except ValueError:
            print("Geçersiz tarih formatı. Lütfen 'YYYY-MM-DD' formatında bir tarih girin.")   
        
        bitis=input("tedavi bitis tarihinizi 'YYYY-MM-DD' şeklinde giriniz")
        try:
             girilen_tarih = datetime.strptime(bitis, "%Y-%m-%d")
             print(f"Girilen tarih: {girilen_tarih}")
        except ValueError:
            print("Geçersiz tarih formatı. Lütfen 'YYYY-MM-DD' formatında bir tarih girin.")
        
        tedavi_süresi=bitis-baslangic
        print(f"Bugün ile girilen tarih arasındaki gün farkı: {tedavi_süresi.days} gün")
        