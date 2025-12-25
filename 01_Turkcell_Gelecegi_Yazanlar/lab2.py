"""
================================================================================
DERS: PYTHON VERİ YAPILARI (DATA STRUCTURES) DETAYLI ANALİZ
================================================================================

BU DERSİN AMACI:
Python'daki temel veri yapılarını (String, Tuple, List, Set, Dictionary) derinlemesine
incelemek, aralarındaki farkları (Mutable/Immutable) ve özel metodlarını öğrenmek.

İÇERİK ÖZETİ:
1. String Karşılaştırma & ASCII: Metinlerin arka plandaki sayısal değerleri.
2. Tuple (Demet): Değiştirilemeyen (Immutable) güvenli listeler.
3. Number Systems: 2'lik (Bin), 8'lik (Oct) ve 16'lık (Hex) taban dönüşümleri.
4. List (Liste): En esnek, değiştirilebilir (Mutable) veri yapısı.
5. Set (Küme): Eşsiz ve sırasız elemanlar, küme matematiği (Kesişim, Fark).
6. Dictionary (Sözlük): Anahtar-Değer (Key-Value) ilişkisi ve JSON mantığı.

================================================================================
"""

#%% HÜCRE 1: String Karşılaştırma ve ASCII Mantığı
print("--- BÖLÜM 1: STRING KARŞILAŞTIRMA & ASCII ---")

isim = "Fatih"
print(f"Eşitlik Kontrolü (Fatih == Fatih): {isim == 'Fatih'}")
print(f"Büyük/Küçük Harf (Fatih == FATİH): {isim == 'FATİH'}") # False

# Stringlerde Büyüklük/Küçüklük (ASCII Değerine Göre)
# Python sözlük sırasına (ASCII kodlarına) bakar.
print("\nASCII Karşılaştırması:")
print(f"'a' > 'B' sonucu: {'a' > 'B'}") # True, çünkü küçük harflerin ASCII kodu daha büyüktür.

# Kanıt (ord fonksiyonu karakterin ASCII kodunu verir):
print(f"a harfinin kodu: {ord('a')}") # 97
print(f"A harfinin kodu: {ord('A')}") # 65
print(f"B harfinin kodu: {ord('B')}") # 66

kelime1 = "ahmet"
kelime2 = "Mehmet"
# 'a' (97), 'M' (77)'den büyüktür.
print(f"'{kelime1}' < '{kelime2}': {kelime1 < kelime2}") 

# Lowercase yaparak adil karşılaştırma
print(f"Lower sonrası karşılaştırma: {kelime1.lower() < kelime2.lower()}")


#%% HÜCRE 2: NoneType ve Tuple (Demetler)
print("\n--- BÖLÜM 2: TUPLE (IMMUTABLE / DEĞİŞTİRİLEMEZ) ---")

# NoneType: Henüz değeri olmayan değişkenler için kullanılır.
sehir = None
print(f"Değişken Tipi: {type(sehir)}")

# TUPLE ÖZELLİKLERİ:
# 1. Parantez () ile tanımlanır.
# 2. Immutable: Elemanları sonradan DEĞİŞTİRİLEMEZ (Read-only).
# 3. Daha az yer kaplar, daha hızlıdır.

tup1 = (15, 26, 17, 25)
tup2 = ("ahmet", "mehmet")
tup3 = (5+4j, "Melih", 74.8, 159)

# HATA ÖRNEĞİ:
# tup1[0] = 174  # TypeError: 'tuple' object does not support item assignment

# Tuple Birleştirme
tup4 = tuple([79, 125, 14.69]) # Listeden tuple'a çevirme
butun_tupler = tup1 + tup2 + tup3 + tup4
print("Birleştirilmiş Tuple:", butun_tupler)

# Slicing (Dilimleme)
print("Slicing [1:] :", tup1[1:])
print("Slicing [::2] (2'şer atla):", tup1[0:len(tup1):2])

# Methodlar
print(f"26 sayısı kaç kere geçiyor?: {tup1.count(26)}")


#%% HÜCRE 3: Sayı Sistemleri (Conversion)
print("\n--- BÖLÜM 3: SAYI SİSTEMLERİ ---")

sayi = 19
print(f"Decimal (10'luk): {sayi}")
print(f"Binary  (2'lik) : {bin(sayi)}") # 0b ile başlar
print(f"Octal   (8'lik) : {oct(sayi)}") # 0o ile başlar
print(f"Hex     (16'lık): {hex(sayi)}") # 0x ile başlar


#%% HÜCRE 4: Listeler (Mutable / Değiştirilebilir)
print("\n--- BÖLÜM 4: LISTELER ---")

# Listeler köşeli parantez [] ile tanımlanır. Değiştirilebilir.
isimler = ['Fatih', 'Kaan', 'Gül', 'Manolya']

# Ekleme (Append vs Extend)
isimler = isimler + ["Ahmet", "Mehmet"] # Liste birleştirme
isimler.append("AppendİleEklenen")      # Tek eleman ekler
print("Ekleme Sonrası:", isimler)

# Güncelleme
isimler[0] = "Ceren" # 0. indexi değiştir
isimler[1:4] = ["Selim", "Oya", "Zehra"] # Çoklu güncelleme
print("Güncelleme Sonrası:", isimler)

# Silme
del isimler[5] # 5. indexi sil
isimler.remove("Oya") # Değere göre sil (İlk bulduğunu siler)
son_eleman = isimler.pop() # Son elemanı siler ve değişkene atar
print(f"Silinen son eleman: {son_eleman}")
print("Silme Sonrası:", isimler)

# Karışık Liste ve Methodlar
karisik_liste = isimler + [28, 35]
karisik_liste.extend([True, 14.7]) # Liste genişletme
karisik_liste.reverse() # Ters çevirme
print("Ters Çevrilmiş Karışık Liste:", karisik_liste)

# Sıralama (Sort) - Sadece aynı tip verilerde çalışır
sayi_listesi = [2, 5, -5, 8, 4, 3, 10, -9]
sayi_listesi.sort()
print("Sıralanmış Sayılar:", sayi_listesi)


#%% HÜCRE 5: Çok Boyutlu Listeler (Nested Lists)
print("\n--- BÖLÜM 5: NESTED (İÇ İÇE) YAPILAR ---")

# Liste içinde liste veya tuple içinde sözlük olabilir.
bilgiler = [
    ({"185": "Fatih"}, {"192": "Melek"}), # 0. İndex: Tuple içinde Dict
    ("İstanbul", "Denizli")               # 1. İndex: Tuple içinde String
]

print("Tüm Yapı:", bilgiler)
print("İlk eleman (Tuple):", bilgiler[0])
print("İlk elemanın ilki (Dict):", bilgiler[0][0])
print("Spesifik Değer Erişimi:", bilgiler[0][0]["185"]) # 'Fatih' değerine ulaşmak


#%% HÜCRE 6: Set (Kümeler)
print("\n--- BÖLÜM 6: SET (KÜMELER) ---")

# Özellikler: Eşsizdir (Unique), Sırasızdır (Unordered), İndexlenemez.
set1 = {5, 12, 2, 6, 12, 5} # Tekrar edenleri otomatik siler
print("Set1 (Tekrarsız):", set1)

# Ekleme / Çıkarma
set1.add(150)
set1.discard(12) # Varsa siler, yoksa hata vermez (Remove hata verir)
print("Ekle/Çıkar Sonrası:", set1)

# Küme İşlemleri (Matematiksel)
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(f"Kesişim (Intersection): {A.intersection(B)}") # {4, 5}
print(f"Fark (Difference A-B): {A.difference(B)}")    # {1, 2, 3}
print(f"Birleşim (Union): {A.union(B)}")              # {1..8}
print(f"Alt Küme mi?: { {1,2}.issubset(A) }")         # True


#%% HÜCRE 7: Dictionary (Sözlükler)
print("\n--- BÖLÜM 7: DICTIONARY (SÖZLÜKLER) ---")

# Anahtar (Key) - Değer (Value) yapısı. JSON formatına benzer.
ogrenci_ders = {
    'Okan': 'Makine Öğrenmesi',
    'Ceren': 'NLP',
    'Tolga': [ # Value bir liste olabilir
        {'Ders': 'Veri Tabanı', 'Hoca': 'Gülşah'}, # Listenin içi sözlük olabilir
        {'Ders': 'NLP', 'Hoca': 'Burak'}
    ]
}

# Erişim
print(f"Ceren'in Dersi: {ogrenci_ders['Ceren']}")
print(f"Tolga'nın 2. dersinin hocası: {ogrenci_ders['Tolga'][1]['Hoca']}")

# Methodlar
print(f"Keys: {ogrenci_ders.keys()}")
print(f"Values: {ogrenci_ders.values()}")

# Get Metodu (Hata almamak için güvenli erişim)
print(f"Okan var mı?: {ogrenci_ders.get('Okan')}")
print(f"Ahmet var mı?: {ogrenci_ders.get('Ahmet', 'Kayıt Bulunamadı!')}")

# Güncelleme
yeni_veri = {'Ahmet': 'Bilgisayar 101'}
ogrenci_ders.update(yeni_veri)
print("Güncellenmiş Sözlük:", ogrenci_ders)

# Zip ile Sözlük Oluşturma
anahtarlar = [1, 2, 3]
degerler = ["A", "B", "C"]
ziplenmis = dict(zip(anahtarlar, degerler))
print("Zip ile oluşturulan:", ziplenmis)