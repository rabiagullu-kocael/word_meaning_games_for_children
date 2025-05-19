
# 📚 Anlam Oyunu - NLP Tabanlı Türkçe Kelime Oyunu

Anlam Oyunu, kullanıcıya verilen kelimenin *eş* veya *zıt anlamlısını* tahmin etmeye dayalı, eğitici ve interaktif bir *web tabanlı oyundur*.

---

## 🚀 Teknolojiler

* **Python + Flask**: Backend sunucusu ve yönlendirme
* **HTML + CSS + Jinja2**: Basit kullanıcı arayüzü
* **CSV**: Kelime verilerinin saklanması
* **Zemberek-NLP**: Türkçe morfolojik analiz
* **sentence-transformers**: Anlamsal benzerlik karşılaştırması
* **Levenshtein Mesafesi**: Yazım hatası toleransı

---

## 🤖 NLP Kullanımı

* Kullanıcı cevabının kökünü ve yapısını Zemberek ile analiz eder
* Anlam benzerliği, sentence-transformers ile hesaplanır (embedding similarity)
* Giriş ile veri kümesindeki doğru cevaplar karşılaştırılır
* Anlamsal eşleşmeye ve yazım toleransına göre doğru/yanlış sonucu döner

---

## ⚙️ Uygulama Akışı

1. Oyun türü seçilir (eş/zıt anlam)
2. Rastgele kelime gösterilir
3. Kullanıcı girdi sağlar
4. NLP analizleriyle doğruluk kontrolü yapılır
5. Sonuç ve puan gösterilir

---

## 📁 Dosya Yapısı

```
├── app.py                 # Flask uygulaması
├── templates/
│   ├── index.html         # Oyun türü seçimi
│   ├── oyun.html          # Oyun arayüzü
│   └── sonuc.html         # Sonuç ekranı
├── es_anlam.csv           
├── zit_anlam.csv        # Eş/zıt anlamlı kelime veri seti
```

---

## 🔧 Geliştirilebilir olan eklentiler:

* Kullanıcı oturumları ve skor takibi
* Genişletilmiş kelime verisi
* Cümle düzeyinde anlam analizi
* Boşluk doldurma eklentisi

---

NOT:Verisetini kendim düzenledim bu yüzden gözden kaçan hatalar olmuş olabilir.
Ayrıca es_anlam_cumle.csv ve zit_anlam_cumle.csv 
verisetleri boşluk doldurma oyunu eklentisi için düzenledim.En kısa zamanda bu eklenti yüklenecektir:
Ayrıca burada kullanılacak olan modeli de eğittim.Bert tabanlı bu model boşluk doldurmada girilen inputu doğru mu diye kontrol etmektedir.
Doğruluk oranı %94.  

Bu dosyaya train.ipynb 'den ulaşabilirsiniz.





