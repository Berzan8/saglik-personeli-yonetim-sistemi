from Doktor import *
from Hemsire import *
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
        try:
            if isinstance(hasta_no,int) and hasta_no.strip():
                self.hasta_no = hasta_no
            else:
                raise ValueError("Lütfen rakamlardan olusan çalişma  saatinizi giriniz!!...")
        except ValueError as e:
            print(f"Hata: {e}")     
    
    def get_ad(self):
        return self.ad
    
    def set_ad(self,ad):
        try:
            if isinstance(ad,int) and ad.strip():
                self.ad = ad
            else:
                raise ValueError("Lütfen adinizi giriniz!!...")
        except ValueError as e:
            print(f"Hata: {e}")
            
    def get_soyad(self):
        return self.soyad
    
    def set_soyad(self,soyad):
        try:
            if isinstance(soyad,int) and soyad.strip():
                self.soyad = soyad
            else:
                raise ValueError("Lütfen soyadinizi giriniz!!...")
        except ValueError as e:
            print(f"Hata: {e}")
    
    def get_dogum_tarihi(self):
        return self.dogum_tarihi
    
    def set_dogum_tarihi(self,dogum_tarihi):
        dogum_tarihi = input("Tarihi 'YYYY-MM-DD' formatında girin: ")

        try:
            girilen_tarih = datetime.strptime(dogum_tarihi, "%Y-%m-%d")
            print(f"Girilen tarih: {girilen_tarih}")
        except ValueError:
            print("Geçersiz tarih formatı. Lütfen 'YYYY-MM-DD' formatında bir tarih girin.")
    
    def get_hastalik(self):
        return self.hastalik
    
    def set_hastalik(self,hastalik):
        try:
            if isinstance(hastalik,int) and hastalik.strip():
                self.hastalik = hastalik
            else:
                raise ValueError("Lütfen hastaliginizi giriniz!!...")
        except ValueError as e:
            print(f"Hata: {e}")
            
    def get_tedavi(self):
        return self.soyad
    
    def set_tedavi(self,tedavi):
        try:
            if isinstance(tedavi,int) and tedavi.strip():
                self.tedavi = tedavi
            else:
                raise ValueError("Lütfen tedavinizi giriniz!!...")
        except ValueError as e:
            print(f"Hata: {e}")
            
    def __str__(self,hasta_no,ad,soyad,dogum_tarihi,hastalik,tedavi):
        
        return print(f"hasta_no:{hasta_no}\n ad:{ad}soyad:{soyad}\n dogum_tarihi:{dogum_tarihi}\n hastalik:{hastalik}\tedavi:{tedavi}")
    
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