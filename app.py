from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
from difflib import SequenceMatcher  # Metinler arası benzerlik oranını hesaplamak için kullanılır

app = Flask(__name__)
app.secret_key = "gizli_bir_anahtar_buraya"  # Oturum (session) verilerini güvenli tutmak için kullanılır



# Eş anlamlı ve zıt anlamlı kelimelerin bulunduğu CSV dosyaları yükleniyor
es_df = pd.read_csv("es_anlam.csv")    # Kolonlar: Kelime, Anlam1, Anlam2, Anlam3
zit_df = pd.read_csv("zit_anlam.csv")  # Kolonlar: Kelime, Zıt Anlam1, Zıt Anlam2, Zıt Anlam3



# Rastgele bir kelime seçer ve bu kelimenin eş veya zıt anlamlarını döndürür
def kelime_sec(tip):
    if tip == "es":
        satir = es_df.sample(1).iloc[0]  # CSV'den rastgele bir satır seç
        anlamlar = [satir["Anlam1"], satir["Anlam2"], satir["Anlam3"]]
    else:  # "zit" için
        satir = zit_df.sample(1).iloc[0]
        anlamlar = [satir["Zıt Anlam1"], satir["Zıt Anlam2"], satir["Zıt Anlam3"]]
    return satir["Kelime"], anlamlar



# Doğal Dil İşleme (NLP) yöntemi: Kullanıcının cevabıyla doğru cevaplar arasındaki benzerliği ölçer
def benzerlik_orani(girilen, dogru_kelimeler):
    # SequenceMatcher iki metin arasındaki benzerlik oranını 0 ile 1 arasında döndürür
    oranlar = [SequenceMatcher(None, girilen.lower(), d.lower()).ratio() for d in dogru_kelimeler]
    return max(oranlar)  # En yüksek benzerlik oranını al




# Girilen kelimeye karşılık gelen doğru anlamları (eş/zıt) getirir
def dogrulari_getir(tip, kelime):
    if tip == "es":
        satir = es_df[es_df["Kelime"] == kelime].iloc[0]
        return [satir["Anlam1"], satir["Anlam2"], satir["Anlam3"]]
    else:
        satir = zit_df[zit_df["Kelime"] == kelime].iloc[0]
        return [satir["Zıt Anlam1"], satir["Zıt Anlam2"], satir["Zıt Anlam3"]]



# Ana sayfa: Kullanıcıdan eş anlamlı mı zıt anlamlı mı oynamak istediği bilgisi alınır
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        tip = request.form["tip"]
        session["puan"] = 0  # Oyuna başlarken puanı sıfırla
        return redirect(url_for("oyun", tip=tip))  # Oyun sayfasına yönlendir
    return render_template("index.html")




# Oyun sayfası: Kelime gösterilir ve kullanıcıdan anlamı yazması istenir
@app.route("/oyun", methods=["GET", "POST"])
def oyun():
    if request.method == "GET":
        tip = request.args.get("tip")  # Kullanıcının seçtiği oyun tipi (eş/zıt)
        if not tip:
            return redirect(url_for("index"))  # Tip seçilmediyse ana sayfaya dön
        kelime, _ = kelime_sec(tip)  # Yeni kelime seç
        puan = session.get("puan", 0)
        return render_template("oyun.html", tip=tip, kelime=kelime, puan=puan)

    # POST ile gelen verileri al
    tip = request.form.get("tip")
    kelime = request.form.get("kelime")
    cevap = request.form.get("cevap")
    puan = session.get("puan", 0)

    # Doğru anlamları getir ve kullanıcı cevabıyla karşılaştır
    dogrular = dogrulari_getir(tip, kelime)
    oran = benzerlik_orani(cevap, dogrular)



    # Benzerlik oranına göre kullanıcıya mesaj göster ve puan güncelle
    if oran > 0.8:
        mesaj = "Tebrikler!  🎉"
        puan += 5
    elif oran > 0.5:
        mesaj = "Yaklaştın, biraz daha dikkat 👀"
    else:
        mesaj = "Uzak kaldın biraz daha düşün 😕"

    session["puan"] = puan  # Güncellenmiş puanı sakla

    # Sonuç sayfasını göster
    return render_template("result.html", cevap=cevap, kelime=kelime, mesaj=mesaj,
                           dogrular=dogrular, oran=oran, tip=tip, puan=puan)




# Uygulamayı çalıştır
if __name__ == "__main__":
    app.run(debug=True)







