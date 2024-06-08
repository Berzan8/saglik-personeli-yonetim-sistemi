import datetime #datetime modülünü içeri aktarıyoruz

class Hasta:
    def __init__(self, hasta_no, ad, soyad, dogum_tarihi, hastalik, tedavi):
        self.hasta_no=hasta_no
        self.ad=ad
        self.soyad=soyad
        self.dogum_tarihi=dogum_tarihi
        self.hastalik=hastalik
        self.tedavi=tedavi
    
    # Hasta numarasını döndüren get metodu   
    def get_hasta_no(self):
        return self.hasta_no
    # Hasta numarasını ayarlayan set metodu
    def set_hasta_no(self,hasta_no):
        
        self.hasta_no=hasta_no
        return self.hasta_no     
    
    # Hasta adını döndüren get metodu
    def get_ad(self):
        return self.ad
    # Hasta adını ayarlayan set metodu
    def set_ad(self,ad):
        
        self.ad=ad
        return self.ad
    
    #hasta soyad döndüren get metodu        
    def get_soyad(self):
        return self.soyad
    # Hasta soyadını ayarlayan set metodu
    def set_soyad(self,soyad):
        
        self.soyad=soyad
        return self.soyad
    
    #hasta doğum tarihini döndüren get metodu
    def get_dogum_tarihi(self):
        return self.dogum_tarihi
    # Hasta dogum tarihini ayarlayan set metodu
    def set_dogum_tarihi(self,dogum_tarihi):
        try:
            
            girilen_tarih = datetime.strptime(dogum_tarihi, "%Y-%m-%d")# Girilen tarihi doğru formatta kontrol ediyoruz
            print(f"Girilen tarih: {girilen_tarih}")
            
        except ValueError:
            print("Geçersiz tarih formatı. Lütfen 'YYYY-MM-DD' formatında bir tarih girin.")
    
    #hastanın hastalık bilgisini döndüren get metodu
    def get_hastalik(self):
        return self.hastalik
    # Hastanın hastalık bilgisini ayarlayan set metodu
    def set_hastalik(self,hastalik):
        
        self.hastalik=hastalik
        return self.hastalik
    
    #hasta tedavi bilgisini döndüren get metodu        
    def get_tedavi(self):
        return self.soyad
    # Hasta tedavi bilgisini ayarlayan set metodu
    def set_tedavi(self,tedavi):
       
       self.tedavi=tedavi
       return self.tedavi
    
     # Nesneyi yazdırmak için kullanılan __str__ metodu        
    def __str__(self):
        
        return print(f"hasta_no:{self.hasta_no}\nad:{self.ad}soyad:{self.soyad}\ndogum_tarihi:{self.dogum_tarihi}\nhastalik:{self.hastalik}\ntedavi:{self.tedavi}")
    
     # Tedavi süresini hesaplayan metodu tanımlıyoruz
    def tedavi_suresi_hesapla(baslangic,bitis):
        baslangic=input("tedavi baslangic tarihinizi 'YYYY-MM-DD' şeklinde giriniz ")
        try:
             girilen_tarih = datetime.strptime(baslangic, "%Y-%m-%d")# Girilen tarihi doğru formatta kontrol ediyoruz
             print(f"Girilen tarih: {girilen_tarih}")
        except ValueError:
            print("Geçersiz tarih formatı. Lütfen 'YYYY-MM-DD' formatında bir tarih girin.")   
        
        bitis=input("tedavi bitis tarihinizi 'YYYY-MM-DD' şeklinde giriniz")
        try:
             girilen_tarih = datetime.strptime(bitis, "%Y-%m-%d")# Girilen tarihi doğru formatta kontrol ediyoruz
             print(f"Girilen tarih: {girilen_tarih}")
        except ValueError:
            print("Geçersiz tarih formatı. Lütfen 'YYYY-MM-DD' formatında bir tarih girin.")
        
        tedavi_süresi=bitis-baslangic
        print(f"Bugün ile girilen tarih arasındaki gün farkı: {tedavi_süresi.days} gün")
        