from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Film/dizi listesi (başlangıçta içinde örnek veriler var)
filmler = [
    {"id": 1, "isim": "Me Before You", "tur": "Romantic Drama", "yil": 2010, "yorum": " I enjoyed so much.", "izlendi": True},
    {"id": 2, "isim": "Breaking Bad", "tur": "Drama", "yil": 2008, "yorum": " I would not recommend it ", "izlendi": False},
]

# Anasayfa route'u - tüm filmleri listeler
@app.route('/')
def index():
    return render_template('index.html', filmler=filmler)

# Film/dizi ekleme sayfası (GET ile form gösterir, POST ile formdan gelen veriyi alır)
@app.route('/add', methods=['GET', 'POST'])
def add_film():
    if request.method == 'POST':
        yeni_film = {
            "id": len(filmler) + 1,
            "isim": request.form['isim'],
            "tur": request.form['tur'],
            "yil": int(request.form['yil']),
            "yorum": request.form['yorum'],
            "izlendi": 'izlendi' in request.form
        }
        filmler.append(yeni_film)
        return redirect(url_for('index'))
    return render_template('add_film.html')

if __name__ == '__main__':
    app.run(debug=True)
