"""
================================================================================
DERSİN AMACI VE ÖZETİ: PYTHON VERİ YAPILARI VE ALGORİTMA TEMELLERİ
================================================================================

BU DERSİN TEMEL AMACI:
Veri Bilimi ve Yapay Zeka projelerinin temeli olan Python veri yapılarını
(Listeler, Sözlükler, Demetler) ve algoritma kurmak için gerekli olan
kontrol yapılarını (Fonksiyonlar, Döngüler, Koşullar) kavramak.

KAZANILAN 4 TEMEL YETKİNLİK:

1. Veri Yapıları (Data Structures):
   - List & Dict: Veriyi organize etmek, depolamak ve etiketlemek.
   - Tuple & Set: Değişmez (güvenli) ve benzersiz veri setleri oluşturmak.
   - Analoji: Market sepeti (List), Ürün etiketi (Dict), Kimlik (Tuple).

2. String Manipülasyonu (Metin İşleme):
   - NLP (Doğal Dil İşleme) için temel teşkil eden metin temizleme,
     parçalama ve dönüştürme işlemleri.

3. Fonksiyonlar (DRY Prensibi - Don't Repeat Yourself):
   - Kod tekrarını önlemek için "küçük robotlar" (fonksiyonlar) inşa etmek.
   - Return vs Print farkını anlamak (Veriyi kullanmak vs. sadece görmek).

4. Algoritma Akışı (Flow Control):
   - If/Else: Karar mekanizmaları kurmak.
   - Loops (Döngüler): Binlerce veriyi tek tek işlemek yerine otomatize etmek.

NEDEN ÖNEMLİ? (MÜHENDİSLİK VİZYONU):
Bir Yapay Zeka modeli eğitmeden önce veriyi temizlemeniz, şekillendirmeniz ve
belirli kurallara göre işlemeniz gerekir. Bu ders, o "veri ön işleme"
sürecinin alfabesidir.

Tarih: 25.12.2025
================================================================================
"""

print('***** Yapay Zeka Bootcamp Başlıyor *****\n')

print("--- BÖLÜM 1: STRING (METİN) İŞLEMLERİ ---")
# Veri Tipi: String
# Örneğin Instagram'daki bir yorum veya tıklama veriye dönüşür.
nereden_ogrenilir = 'Miuul Data Science'

# Slicing (Dilimleme) -> [başla : bitir : adım]
# Not: Bitiş indeksi dahil edilmez.
print("İlk 5 karakter:", nereden_ogrenilir[0:5])

# Metin Metodları
print("Uzunluk:", len(nereden_ogrenilir))
print("Büyük harf:", nereden_ogrenilir.upper())
print("Küçük harf:", nereden_ogrenilir.lower())
print("Değiştir:", nereden_ogrenilir.replace('Data', 'VERİ'))

# İçerme Kontrolü (Case Sensitive - Büyük/Küçük harf duyarlı)
print("'data' var mı?:", 'data' in nereden_ogrenilir)  # False
print("'Data' var mı?:", 'Data' in nereden_ogrenilir)  # True


print("\n--- BÖLÜM 2: LISTELER (LISTS) ---")
# Listeler: Değiştirilebilir, sıralı, farklı türleri barındırabilir.
# Analoji: Market sepeti.

sepet = ["elma", "süt", "ekmek", 100]
print("İlk eleman:", sepet[0])

# Eleman Değiştirme
sepet[1] = 'çikolatalı süt'
print("Güncel sepet:", sepet)

# Ekleme ve Çıkarma
sepet.append("Yumurta")  # Sona ekler
print("Ekleme sonrası:", sepet)

sepet.pop(0)  # 0. indexteki elemanı (elma) siler
print("Silme sonrası:", sepet)

# Çok Boyutlu Listeler (Nested Lists)
mixed = [1, 2, "a", True, [10, 20, 30]]
print("İç içe listeden veri çekme:", mixed[4][1])  # 20 değerine ulaşır


print("\n--- BÖLÜM 3: SÖZLÜKLER (DICTIONARIES) ---")
# Sözlükler: Anahtar (Key) ve Değer (Value) çiftleri.
# Analoji: Bir ürünün etiketi. Sıralama önemli değildir, erişim anahtarla yapılır.

urun = {
    "marka": "Nike",
    "fiyat": 2000,
    "renk": "Beyaz"
}

# Veriye Erişim
print("Ürün Markası:", urun["marka"])

# Güncelleme ve Yeni Veri Ekleme
urun["fiyat"] = 4000  # Zam geldi
urun["beden"] = 42    # Yeni özellik
print("Güncel Ürün Etiketi:", urun)


print("\n--- BÖLÜM 4: DEMETLER (TUPLES) & KÜMELER (SETS) ---")

# TUPLE (DEMET) -> ()
# Listeye benzer ama DEĞİŞTİRİLEMEZ (Immutable).
# Analoji: TC Kimlik No, Doğum Tarihi (Güvenlik gerektiren veriler).
kimlik = ("Ali", 123456789)
print("Kimlik Sahibi:", kimlik[0])
# kimlik[0] = "Veli"  # Bu kod hata verir (TypeError), çünkü tuple değiştirilemez.

# SET (KÜME) -> {}
# Eşsiz elemanlardan oluşur, sıra yoktur.
# Analoji: Piyango torbası (Her sayıdan bir tane olur).
sayilar = {1, 2, 2, 2, 3, 4}
print("Tekrarsız Küme:", sayilar)  # 2'leri teke düşürür


print("\n--- BÖLÜM 5: FONKSİYONLAR (FUNCTIONS) ---")
# Fonksiyonlar bizim küçük robotlarımızdır.
# DRY (Don't Repeat Yourself) prensibi için kullanılır.

def calculate(x):
    """Verilen sayıyı 2 ile çarpar ve ekrana basar."""
    print("İşlem sonucu:", x * 2)

calculate(5)

# Çok Parametreli Fonksiyon ve Docstring
def summer(a, b):
    """
    İki sayının toplamını ekrana bastırır.
    
    Args:
        a (int, float): Birinci sayı
        b (int, float): İkinci sayı
    """
    print("Toplam:", a + b)

summer(4, 5)
summer(b=5, a=4)  # Parametre ismini vererek sıra bağımsız çağırma

# Global ve Local Değişkenler (Scope)
store = []  # Global değişken (Evin salonu, herkes erişir)

def add_element(a, b):
    result = a * b       # Local değişken (Sadece fonksiyon içinde yaşar)
    store.append(result) # Global listeye etki eder
    print(f"Çarpım: {result}, Sepetin son durumu: {store}")

add_element(2, 5)
add_element(7, 10)

# Return vs Print
# Print sadece gösterir, Return değeri "ele verir".
def divide(a, b=1): # b girilmezse varsayılan olarak 1 al
    return a / b

sonuc = divide(10, 2)
print("Return edilen değerin 10 katı:", sonuc * 10)


print("\n--- BÖLÜM 6: KOŞULLAR (IF-ELSE) ---")

def number_check(number):
    if number > 10:
        print(f"{number} sayısı 10'dan büyüktür.")
    elif number < 10:
        print(f"{number} sayısı 10'dan küçüktür.")
    else:
        print(f"{number} sayısı 10'a eşittir.")

number_check(5)
number_check(11)


print("\n--- BÖLÜM 7: DÖNGÜLER (LOOPS) ---")

numbers = [1, 2, 3, 4, 5]
students = ["Ali", "Ayşe", "Mehmet", "Zeynep"]

# For Döngüsü
for num in numbers:
    # end=" " yan yana yazdırmak için kullanılır
    print(f"{num}'in karesi: {num**2}")

# String üzerinde döngü
for student in students:
    print(student.upper(), end=", ")
print() # Alt satıra geç

# While Döngüsü
print("While döngüsü:")
count = 1
while count <= 3:
    print(count, end=" ")
    count += 1
print()

# Break ve Continue
print("\nBreak Örneği (3'ü görünce dur):")
for num in numbers:
    if num == 3:
        break
    print(num, end=" ") # 3'e gelince döngü kırılır, 3 yazılmaz.

print("\n\nContinue Örneği (3'ü atla):")
for num in numbers:
    if num == 3:
        continue
    print(num, end=" ") # 3'ü atlar, 4 ve 5'i yazar.
print()

print("\n--- UYGULAMA: Kelime Uzunlukları ---")
words = ["apple", "banana", "cat", "hi"]
for w in words:
    print(f"{w} -> {len(w)} harf")

print("\n***** Ders Sonu *****")

# NOT: Aşağıdaki kısım bir sonraki dersin (Pandas/Veri Analizi) konusudur.
"""
# GELECEK DERS PREVIEW:
import pandas as pd
import seaborn as sns

df = sns.load_dataset('titanic')
print(df.head())
"""