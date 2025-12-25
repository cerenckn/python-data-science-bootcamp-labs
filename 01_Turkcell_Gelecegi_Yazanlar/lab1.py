"""
================================================================================
DERS: PYTHON GİRİŞ - TEMEL GİRİŞ/ÇIKIŞ İŞLEMLERİ (I/O)
================================================================================

BU DERSİN AMACI:
Python'da ekrana veri yazdırma (print), metinleri biçimlendirme, özel karakterleri
yönetme ve kullanıcıdan veri alma (input) mantığını kavramak.

ÖNEMLİ KAVRAMLAR:
1. Escape Characters (\n, \t): Metin içinde alt satıra geçme veya boşluk bırakma.
2. Parametreler (sep, end): Print fonksiyonunun varsayılan davranışını değiştirme.
3. Raw String (r""): Dosya yolları gibi özel karakter içeren metinleri olduğu gibi okuma.
4. Input: Kullanıcı ile etkileşime girme.

================================================================================
"""

#%% HÜCRE 1: Temel Yazdırma ve Birleştirme
print("--- BÖLÜM 1: TEMEL YAZDIRMA ---")

print("Python Eğitimi")

# String Birleştirme (Concatenation)
# İki metni '+' operatörü ile yapıştırabiliriz.
print("Python" + "Eğitimi")       # Bitişik yazar: PythonEğitimi
print("Python" + " " + "Eğitimi") # Araya boşluk ekler: Python Eğitimi


#%% HÜCRE 2: Kaçış Karakterleri (Escape Sequences)
print("\n--- BÖLÜM 2: KAÇIŞ KARAKTERLERİ ---")

# \n : New Line (Yeni Satır) - İmleci alt satıra indirir.
print("İstanbul\nİzmir\nAnkara")

# \" : Çift tırnak içinde çift tırnak kullanmak için kaçış karakteri gerekir.
# Yanlış: print("Dünyanın en güzel yeri "Ankara'dır"") -> Hata verir5

print("Dünyanın en güzel yeri \"Ankara'dır\"")


#%% HÜCRE 3: Raw String (İşlenmemiş Metin)
print("\n--- BÖLÜM 3: RAW STRING (r) ---")

# Dosya yollarında '\' veya ':' karakterleri bazen kaçış karakteri sanılabilir.
# Başına 'r' koyarak "bunu olduğu gibi oku, yorumlama" deriz.
print(r"C:/Users/crnck") 


#%% HÜCRE 4: Print Parametreleri (end & sep)
print("\n--- BÖLÜM 4: END ve SEP PARAMETRELERİ ---")

# end Parametresi:
# Normalde print() işlemi bitince alt satıra geçer (varsayılan: end="\n").
# Biz bunu değiştirip boşluk (" ") yaparsak yan yana yazar.
print("Python", end=" ")
print("Eğitimi") 
# Çıktı: Python Eğitimi (Alt alta değil)

# sep (Separator) Parametresi:
# Virgülle ayrılan elemanların arasına ne konulacağını belirler.
# Varsayılan boşluktur.
print("Ceren", "Çeken", "2004", sep="-") 
print(2, 3, 2025, sep="/")


#%% HÜCRE 5: Yıldız (*) Operatörü ile Unpacking
print("\n--- BÖLÜM 5: UNPACKING (YILDIZ OPERATÖRÜ) ---")

# Bir stringin her karakterini ayırıp arasına nokta koymak:
# Uzun yol: print("T", "C", sep=".")
# Kısa yol (* ile stringi parçalarına ayırır):
print(*"TC", sep=".") 
# Çıktı: T.C


#%% HÜCRE 6: String Formatlama (Eski ve Yeni Yöntemler)
print("\n--- BÖLÜM 6: STRING FORMATLAMA ---")

# 1. Yöntem: Metin içinde birleştirme (Okunması zordur)
print("Adı: Ceren " "Soyadı:Çeken " "D.Tarihi: 20.09.2004 ")

# 2. Yöntem: .format() metodu (Klasik Yöntem)
# Süslü parantez {} yer tutucudur.
print("Adı: {} Soyadı: {} D.Tarihi: {}".format("Ceren", "Çeken", "20.09.2004"))

# 3. Yöntem: f-string (Modern ve Önerilen Yöntem - Python 3.6+)
ad = "Ceren"
soyad = "Çeken"
print(f"Adı: {ad} Soyadı: {soyad} (Modern f-string)")


#%% HÜCRE 7: Kullanıcıdan Veri Alma (Input)
print("\n--- BÖLÜM 7: KULLANICI GİRİŞİ (INPUT) ---")

# input() fonksiyonu her zaman 'string' (metin) değeri döndürür.
# Matematiksel işlem yapılacaksa int() veya float() ile dönüştürülmelidir.
girdi = input("Lütfen bir sayı giriniz: ")
print("Girdiğiniz sayı:", girdi)


#%% HÜCRE 8: Görev Yönetimi (TODO)
# IDE'lerde (VS Code, PyCharm) TODO etiketleri, yapılacaklar listesinde görünür.
# TODO: Bu kısımdaki input fonksiyonuna hata yakalama (try-except) eklenecek.