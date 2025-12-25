"""
================================================================================
DERSİN AMACI VE ÖZETİ: HAM VERİDEN BİLGİYE YOLCULUK
================================================================================

BU DERSİN TEMEL AMACI:
Klasik programlama döngülerinden (for loops) çıkarak, veriyi "vektörel" olarak
işlemeyi ve ham veriyi anlamlı bilgiye dönüştürmeyi öğrenmek.

KAZANILAN 3 TEMEL YETKİNLİK:

1. NumPy (Hız ve Matematik Motoru):
   - Sorun: Klasik listeler yavaştır ve matematiksel işlemler zordur.
   - Çözüm: Broadcasting özelliği ile milyonlarca veriyi döngüsüz, tek satırda işlemek.
   - Kritik Kavram: Veriyi tekil sayı değil, çok boyutlu matris olarak görmek.

2. Pandas (Veri Manipülasyonu):
   - Sorun: Veriler dağınık, eksik ve karmaşık gelir.
   - Çözüm: Veriyi filtrelemek, temizlemek ve şekillendirmek (Excel'in kod hali).
   - Kritik Yetenekler: Filtering (Seçme), Aggregation (Toplulaştırma), Feature Engineering.

3. EDA (Keşifçi Veri Analizi):
   - Amaç: Modele körü körüne dalmadan önce verinin röntgenini çekmek.
   - Yöntem: `check_df` ve `grab_col_names` gibi fonksiyonlarla veri setini
     saniyeler içinde analiz edip, kategorik/sayısal ayrımını otomatize etmek.

NEDEN ÖNEMLİ? (MÜHENDİSLİK VİZYONU):
Yapay Zeka ve Görüntü İşleme projelerinde modeller, veriyi bu formatlarda bekler.
Burada öğrendiğin "Matris Yönetimi" ve "Veri Temizliği", kuracağın gelişmiş
modellerin temel taşıdır.

Tarih: 25.12.2025
================================================================================
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Pandas görüntüleme ayarları (Tüm sütunları görmek için)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

print("--- BÖLÜM 1: NUMPY TEMELLERİ ---\n")

# 1. Neden NumPy? (Hız ve Kolaylık)
print("Welcome to NumPy")

# Klasik Python Listesi ile İşlem
# Python listelerinde matematiksel işlem için döngü gerekir.
python_listesi = [1, 2, 3, 4]
python_sonuc = []
for sayi in python_listesi:
    python_sonuc.append(sayi * 2)
print("Klasik Python listesi:", python_sonuc)

# NumPy Array (Vektörizasyon) ile İşlem
# Döngüye gerek yoktur, tüm listeyi tek seferde çarpar (Broadcasting).
numpy_array = np.array([1, 2, 3, 4])
print("Numpy array sonucu:", numpy_array * 2)


print("\n--- BÖLÜM 2: ARRAY OLUŞTURMA VE ÖZELLİKLERİ ---\n")

# Array Oluşturma
veri_array = np.array([1, 2, 3, 4, 5])
print("Array:", veri_array)

# Rastgele Veri Üretme (0-100 arası 10 not)
rastgele_notlar = np.random.randint(0, 101, 10)
print("Rastgele notlar:", rastgele_notlar)

# Boyut İnceleme (Shape & Ndim)
ornek_veri = np.random.randint(1, 10, 6)
print("Verimiz:", ornek_veri)
print("Array'in boyut sayısı (ndim):", ornek_veri.ndim)  # Boyut sayısı
print("Notlar arrayinin şekli (shape):", rastgele_notlar.shape)  # (Satır, Sütun)

# Reshape (Yeniden Şekillendirme)
duz_array = np.arange(1, 10)  # 1'den 9'a kadar sayılar
print("Düz hali:", duz_array)

matris_3x3 = duz_array.reshape(3, 3)
print("Matris hali:\n", matris_3x3)
print("Matrisin boyutu:", matris_3x3.shape)


print("\n--- BÖLÜM 3: INDEXING & FILTERING (VERİ SEÇME) ---\n")

# İndeksleme ve Dilimleme (Slicing)
dizi = np.array([10, 20, 30, 40, 50])
print("İlk eleman:", dizi[0])
print("1-4 arası (4 dahil değil):", dizi[1:4])

dizi[0] = 99
print("Değiştirilmiş dizi:", dizi)

# Koşullu Seçim (Fancy Indexing)
ogrenci_notlari = np.array([55, 67, 45, 89, 23, 76, 34, 90])
print("50'den küçük mü?:", ogrenci_notlari < 50)  # True/False döner

# Notu 50'den düşük olanları filtrele
kalanlar = ogrenci_notlari[ogrenci_notlari < 50]
print("50'den düşük notlar:", kalanlar)

# Toplu İşlem (Broadcasting)
print("Herkesin yeni notu (+5 puan):", np.array([10, 20, 30, 40]) + 5)


print("\n--- BÖLÜM 4: İSTATİSTİKSEL İŞLEMLER ---\n")

analiz_notlari = np.array([55, 67, 45, 89, 23])
print("Notların ortalaması:", np.mean(analiz_notlari))
print("Notların medyanı:", np.median(analiz_notlari))
print("En yüksek not:", np.max(analiz_notlari))


print("\n--- BÖLÜM 5: PANDAS & SEABORN GİRİŞ ---\n")

print("Welcome to Pandas & Seaborn")
# Pandas Series vs NumPy Array
# Fark: Pandas serilerinin etiketli indeksleri vardır.
numpy_puanlar = np.array([10, 20, 30, 40])
pandas_serisi = pd.Series([10, 20, 30, 40])

print("Numpy array:", numpy_puanlar)
print("Pandas series:\n", pandas_serisi)
print("Tip:", type(pandas_serisi))
print("Series indexleri:", pandas_serisi.index)
print("Series değerleri:", pandas_serisi.values)
print("Veri tipi:", pandas_serisi.dtype)
print("İlk 3 kayıt (head):", pandas_serisi.head(3))


print("\n--- BÖLÜM 6: VERİ OKUMA VE İNCELEME ---\n")

# Örnek veri seti oluşturup CSV kaydetme (Senaryo gereği)
data_dict = {
    'PRICE': [39, 49, 29, 19, 39, 49, 29, 39, 59, 19],
    'SOURCE': ['android', 'ios', 'android', 'android', 'ios', 'ios', 'android', 'ios', 'android', 'ios'],
    'SEX': ['male', 'female', 'male', 'female', 'male', 'female', 'female', 'male', 'female', 'male'],
    'COUNTRY': ['usa', 'tur', 'bra', 'bra', 'deu', 'tur', 'fra', 'usa', 'deu', 'fra'],
    'AGE': [17, 21, 35, 41, 18, 54, 33, 46, 25, 15]
}
df_temp = pd.DataFrame(data_dict)
df_temp.to_csv('persona.csv', index=False)

# Veriyi okuma
df = pd.read_csv("persona.csv")

# Titanic veri setini yükleme (Ana çalışma bununla yapılacak)
df = sns.load_dataset("titanic")

print("İlk 5 satır:\n", df.head())
print("\nVeri Seti Bilgisi:")
df.info()
print("\nSütun İsimleri:", df.columns)
print("\nİstatistiksel Özet:\n", df.describe().T)
print("\nBoş Değer Sayıları:\n", df.isnull().sum())
print("\nCinsiyet Dağılımı:\n", df["sex"].value_counts())


print("\n--- BÖLÜM 7: VERİ MANİPÜLASYONU (SEÇME & SİLME) ---\n")

# İndeks işlemleri
print("Index bilgisi:", df.index)
print("İlk 5 satır (slicing):", df[0:5])

# Satır Silme (Drop)
silinecek_indexler = [0, 1, 2]
# inplace=True demezsek kalıcı silinmez, sadece gösterir.
print("Silinmiş hali (önizleme):\n", df.drop(silinecek_indexler, axis=0).head())

# Kalıcı Silme
df.drop(silinecek_indexler, axis=0, inplace=True)

# Değişken Seçimi
# Tek [] Series döndürür, Çift [[]] DataFrame döndürür.
print("'age' sütunu var mı?:", "age" in df)
print("Çoklu sütun seçimi:\n", df[["age", "sex"]].head())

# Feature Engineering (Yeni Değişken Üretme)
df["new_age"] = df["age"] * 2
print("Yeni oluşturulan yaş sütunu:\n", df[["age", "new_age"]].head())

# Temizlik: Oluşturulan sütunu silme
df.drop("new_age", axis=1, inplace=True) # axis=1 sütun demektir


print("\n--- BÖLÜM 8: TOPLULAŞTIRMA (AGGREGATION) ---\n")

# Ortalama Yaş
print("Tüm yolcuların yaş ortalaması:", df["age"].mean())

# Groupby: Cinsiyete göre kırılım
print("Cinsiyete göre yaş ortalaması:\n", df.groupby("sex")["age"].mean())

# Gelişmiş Groupby: Hem ortalama yaş hem toplam hayatta kalan sayısı
print("Detaylı Analiz:\n", df.groupby("sex").agg({"age": "mean", "survived": "sum"}))

# Pivot Tablo (Excel benzeri yapı)
pivot_ozet = df.pivot_table("survived", index="sex", columns="class", observed=False) # observed uyarısını önlemek için
print("Pivot Tablo (Hayatta Kalma Oranları):\n", pivot_ozet)


print("\n--- BÖLÜM 9: BİRLEŞTİRME (JOIN OPERATIONS) ---\n")

# Örnek Veri Setleri
df_calisanlar = pd.DataFrame({
    'employees': ['ali', 'veli', 'ayşe', 'fatma'],
    'start_date': [2010, 2012, 2014, 2016]
})
df_departmanlar = pd.DataFrame({
    'employees': ['ali', 'veli', 'ayşe', 'fatma'],
    'department': ['IT', 'HR', 'Finance', 'Marketing']
})

# Merge (SQL Join mantığı)
birlestirilmis_df = pd.merge(df_calisanlar, df_departmanlar, on="employees")
print("Birleştirilmiş DataFrame:\n", birlestirilmis_df)


print("\n--- BÖLÜM 10: VERİ GÖRSELLEŞTİRME ---\n")

# Basit Bar Grafiği
df["sex"].value_counts().plot(kind="bar")
plt.title("Cinsiyet Dağılımı")
plt.show(block=True)


print("\n--- BÖLÜM 11: GELİŞMİŞ KEŞİFÇİ VERİ ANALİZİ (EDA) ---\n")

# Veri setini sıfırlayalım (Temiz başlangıç)
df = sns.load_dataset("titanic")

def check_df(dataframe, head=5):
    """
    Veri setine hızlı bir genel bakış atar.
    Boyut, tipler, ilk/son elemanlar, boş değerler ve istatistikleri gösterir.
    """
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    # numeric_only=True: Sadece sayısal sütunların istatistiğini al (Hata önleyici)
    print(dataframe.quantile([0, 0.25, 0.5, 0.75, 0.95, 0.99, 1], numeric_only=True).T)

check_df(df)

def grab_col_names(dataframe, cat_th=10, car_th=20):
    """
    Veri setindeki değişkenleri türlerine göre ayrıştırır:
    - Kategorik (cat_cols)
    - Sayısal (num_cols)
    - Kategorik görünümlü Kardinal (cat_but_cardinal) -> Örn: İsimler
    """
    # 1. Tip olarak kategorik olanlar (Object, Bool vb.)
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    
    # 2. Sayısal görünümlü ama aslında kategorik olanlar (Örn: survived 0-1, pclass 1-2-3)
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and
                   dataframe[col].dtypes != "O"]
    
    # 3. Kategorik görünümlü ama kardinal (Çok fazla eşsiz değer var, bilgi taşımaz. Örn: İsim)
    cat_but_cardinal = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and
                        dataframe[col].dtypes == "O"]
    
    # Listeleri birleştir ve temizle
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_cardinal]
    
    # Sayısal değişkenleri bul
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    num_cols = [col for col in num_cols if col not in num_but_cat]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_cardinal: {len(cat_but_cardinal)}')

    return cat_cols, num_cols, cat_but_cardinal

# Fonksiyonu çalıştır
cat_cols, num_cols, cat_but_cardinal = grab_col_names(df)
print("Kategorik değişkenler:", cat_cols)


def cat_summary(dataframe, col_name, plot=False):
    """Kategorik değişkenlerin sınıf oranlarını gösterir."""
    print(pd.DataFrame({
        col_name: dataframe[col_name].value_counts(),
        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)
    }))
    print("##########################################")
    
    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

# Kategorik değişkenleri görselleştir
print("\n--- Kategorik Değişken Analizi ---")
for col in cat_cols:
    # Boolean tipindekileri görselleştirirken hata almamak için int'e çeviriyoruz veya pas geçiyoruz
    if dataframe[col].dtypes == "bool":
        dataframe[col] = dataframe[col].astype(int)
    cat_summary(df, col, plot=True)


def num_summary(dataframe, numerical_col, plot=False):
    """Sayısal değişkenlerin istatistiksel özetini ve histogramını verir."""
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)
    
    if plot:
        dataframe[numerical_col].hist(bins=20)
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)

# Sayısal değişkenleri görselleştir
print("\n--- Sayısal Değişken Analizi ---")
for col in num_cols:
    num_summary(df, col, plot=True)

print("\nAnaliz tamamlandı!")