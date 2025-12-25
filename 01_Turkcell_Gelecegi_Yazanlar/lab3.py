"""
================================================================================
DERS: AKIŞ KONTROLÜ VE FONKSİYONEL PROGRAMLAMA
================================================================================

BU DERSİN AMACI:
Programın akışını yöneten koşul yapılarını (If-Else), tekrarlı işlemleri otomatize
eden döngüleri (For-While) ve Python'un güçlü fonksiyonel araçlarını (Map, Filter, Reduce)
kavramak.

İÇERİK:
1. Koşullar (If-Elif-Else): Karar mekanizmaları.
2. Döngüler (Loops): Range, iterasyon ve sonsuz döngü kontrolü.
3. List Comprehension: Tek satırda liste oluşturma sanatı.
4. Fonksiyonel Programlama:
   - Filter: Süzgeçleme.
   - Map: Dönüştürme.
   - Reduce: İndirgeme (Tek bir sonuca varma).

================================================================================
"""

#%% HÜCRE 1: KOŞULLAR (IF-ELIF-ELSE)
print("--- BÖLÜM 1: KOŞULLAR ---")

# Temel Yapı
# 0 hariç her sayının boolean değeri True'dur.
# Clean Code İpucu: "if sayi % 2 == 1:" yerine "if sayi % 2:" kullanılabilir.
sayi = 5
if sayi % 2:
    print(f"{sayi} tek sayıdır.")
else:
    print(f"{sayi} çift sayıdır.")


# İç İçe (Nested) Koşullar - Mülakat Örneği
cinsiyet = "Erkek"
boy = 178

# Mantık Operatörleri (and/or) ile daha temiz yazım:
if (cinsiyet == "Kadın" and boy >= 160) or (cinsiyet == "Erkek" and boy >= 170):
    print("Ön sağlık muayenesini geçebilirsiniz.")
else:
    print("Mülakatı geçemediniz veya hatalı giriş yaptınız.")


# Kullanıcı Giriş Simülasyonu
admin_user = "admin"
admin_pass = "1234"

# input() fonksiyonlarını ayrı satırlarda almak daha okunabilirdir.
kullanici_adi = input("Kullanıcı Adı: ")
parola = input("Parola: ")

if kullanici_adi == admin_user and parola == admin_pass:
    print("Giriş Başarılı!")
elif kullanici_adi == admin_user:
    print("Parola Hatalı!")
else:
    print("Kullanıcı bulunamadı.")


#%% HÜCRE 2: DÖNGÜLER (FOR LOOPS)
print("\n--- BÖLÜM 2: FOR DÖNGÜLERİ ---")

# range(başlangıç, bitiş, adım) -> Bitiş dahil değildir.
print("Range Örneği:", end=" ")
for sayi in range(5, 10):
    print(sayi, end=" ")
print() # Alt satıra geç

# Listeler Üzerinde Gezinme
isimler = ["Ceren", "Levent", "Karan"]
for isim in isimler:
    print(f"İsim: {isim}")

# Tuple ve Unpacking (Paket Açma)
# (x, y) şeklindeki verileri döngüde doğrudan değişkenlere atayabiliriz.
koordinatlar = [(10, 20), (5, 9), (-3, 4)]
print("\nKoordinat Analizi:")
for x, y in koordinatlar:
    print(f"X: {x}, Y: {y} -> Toplam: {x+y}")

# Sözlüklerde Gezinme (.items() metodu)
bilgiler = {
    'Fatih': 'Bilgisayar Müh.',
    'Kaan': 'Makine Müh.',
    'Aliye': 'Gıda Müh.'
}
print("\nMeslek Listesi:")
for isim, meslek in bilgiler.items():
    print(f"{isim} -> {meslek}")


#%% HÜCRE 3: DÖNGÜLER (WHILE LOOPS)
print("\n--- BÖLÜM 3: WHILE DÖNGÜLERİ ---")

# DİKKAT: While döngülerinde artış miktarını (i += 1) unutursanız sonsuz döngüye girer!

# Örnek 1: Sayıları Toplama
sayi = 1
bitis = 5
toplam = 0
print(f"{sayi}'den {bitis}'e kadar toplama:")

while sayi <= bitis:
    toplam += sayi
    sayi += 1
print(f"Sonuç: {toplam}")

# Örnek 2: Listeyi Tersten Yazdırma (Manuel Index Yöntemi)
sayilar = [10, 20, 30, 40]
index = len(sayilar) - 1  # Son elemanın indeksi

print("Tersten Liste:", end=" ")
while index >= 0:
    print(sayilar[index], end=" ")
    index -= 1
print()

# Örnek 3: Sayı Basamaklarını Ayırma ve Toplama
# Girilen sayı: 123 -> İşlem: 1+2+3 = 6
girilen_sayi = 1254
gecici_sayi = girilen_sayi
basamak_toplami = 0
basamaklar = []

while gecici_sayi > 0:
    son_basamak = gecici_sayi % 10    # Mod alarak son rakamı bul
    basamak_toplami += son_basamak
    basamaklar.append(son_basamak)
    gecici_sayi //= 10                # Tam bölme ile son rakamı at

basamaklar.reverse() # Tersten eklediğimiz için düzeltiyoruz
print(f"{girilen_sayi} sayısının basamakları: {basamaklar}")
print(f"Basamakları toplamı: {basamak_toplami}")


#%% HÜCRE 4: MATRİS OLUŞTURMA (IC İÇE WHILE)
print("\n--- BÖLÜM 4: MATRİS ÇİZİMİ ---")
# 4 Satır, 10 Sütunluk '$' işareti çizdirme

satir = 1
while satir <= 4:
    sutun = 1
    while sutun <= 10:
        print("$", end="")
        sutun += 1
    print() # Satır bitince alt satıra geç
    satir += 1


#%% HÜCRE 5: FONKSİYONEL PROGRAMLAMA GİRİŞ (FILTER)
print("\n--- BÖLÜM 5: FILTER (SÜZGEÇ) FONKSİYONU ---")

# Filter: Bir liste içindeki elemanları belirli bir koşula göre eler.
# Yapı: filter(fonksiyon, liste)

sayilar = [3, -2, 5, 6, -9, 0, 12]

# Yöntem 1: Klasik Fonksiyon ile
def pozitif_mi(x):
    return x > 0

pozitifler = list(filter(pozitif_mi, sayilar))
print("Pozitifler (Klasik):", pozitifler)

# Yöntem 2: Lambda (Anonim Fonksiyon) ile - Daha Clean Code
# lambda x: x < 0  -> "Gelen x değeri için, x 0'dan küçükse True dön" demektir.
negatifler = list(filter(lambda x: x < 0, sayilar))
print("Negatifler (Lambda):", negatifler)

ciftler = list(filter(lambda x: x % 2 == 0, sayilar))
print("Çift Sayılar:", ciftler)


#%% HÜCRE 6: MAP FONKSİYONU (DÖNÜŞTÜRME) - EKSİK OLAN KISIM
print("\n--- BÖLÜM 6: MAP (DÖNÜŞTÜRME) FONKSİYONU ---")

# Map: Bir listenin TÜM elemanlarına aynı işlemi uygular.
# Filter eler, Map değiştirir.
# Yapı: map(fonksiyon, liste)

veriler = [1, 2, 3, 4, 5]

# Örnek 1: Her sayının karesini al
kareler = list(map(lambda x: x**2, veriler))
print(f"Orijinal: {veriler}")
print(f"Kareler : {kareler}")

# Örnek 2: İsimleri büyük harfe çevirme
isim_listesi = ["ali", "veli", "ayşe"]
buyuk_isimler = list(map(lambda x: x.upper(), isim_listesi))
print(f"Büyük Harf: {buyuk_isimler}")

# Örnek 3: Çoklu Liste ile Map
# İki listeyi aynı anda toplayabiliriz.
vize = [10, 20, 30]
final = [50, 60, 70]
# x vizeden, y finalden gelir
toplam_not = list(map(lambda x, y: x + y, vize, final))
print(f"Vize+Final Toplamları: {toplam_not}")


#%% HÜCRE 7: REDUCE FONKSİYONU (İNDİRGEME) - EKSİK OLAN KISIM
print("\n--- BÖLÜM 7: REDUCE (İNDİRGEME) FONKSİYONU ---")

# Reduce: Listeyi tek bir sonuca indirger (Örn: Toplamını bulma, çarpımını bulma).
# Not: Python 3'te 'functools' kütüphanesinden çağrılmalıdır.

from functools import reduce

sayilar_listesi = [1, 2, 3, 4, 5]

# Örnek 1: Kümülatif Toplam (1+2+3+4+5)
# x: birikimli toplam, y: sıradaki sayı
toplam_sonuc = reduce(lambda x, y: x + y, sayilar_listesi)
print(f"Reduce ile Toplam: {toplam_sonuc}")

# Örnek 2: Faktöriyel Mantığı (Çarpım)
carpim_sonuc = reduce(lambda x, y: x * y, sayilar_listesi)
print(f"Reduce ile Çarpım (5!): {carpim_sonuc}")

# Örnek 3: En Büyük Sayıyı Bulma
max_sayi = reduce(lambda x, y: x if x > y else y, [10, 52, 99, 4, 21])
print(f"En büyük sayı: {max_sayi}")


#%% HÜCRE 8: LIST COMPREHENSION (ÖZET LİSTELER)
print("\n--- BÖLÜM 8: LIST COMPREHENSION ---")
# Pythoncuların en sevdiği özellik. Map ve Filter'ın daha okunabilir halidir.

ham_veri = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Map Yerine: Her elemanın karesi
kareler_comp = [x**2 for x in ham_veri]
print("Comprehension Kareler:", kareler_comp)

# Filter Yerine: Sadece çift sayılar
ciftler_comp = [x for x in ham_veri if x % 2 == 0]
print("Comprehension Çiftler:", ciftler_comp)

# Map + Filter Bir Arada: Çiftlerin karesi
cift_kareler = [x**2 for x in ham_veri if x % 2 == 0]
print("Çiftlerin Kareleri:", cift_kareler)