from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Veritabanı Modeli
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    last_score = db.Column(db.Integer)
    highest_score = db.Column(db.Integer)

# Ana Sayfa
@app.route('/')
def home():
    return render_template('index.html')

# Sınav Sayfası
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    highest_score_user = User.query.order_by(User.highest_score.desc()).first()
    
    # Kullanıcının kişisel skor bilgilerini al
    username = request.args.get('username')  # "Yeniden Dene" butonundan gelen kullanıcı adı
    user = None
    if username:
        user = User.query.filter_by(username=username).first()
    
    if request.method == 'POST':
        # Sınav sonuçlarını işle ve veritabanına kaydet
        score = calculate_score(request.form)
        username = request.form['username']
        user = User.query.filter_by(username=username).first()
        if user:
            user.last_score = score
            if score > user.highest_score:
                user.highest_score = score
        else:
            new_user = User(username=username, last_score=score, highest_score=score)
            db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('result', score=score, username=username))
    
    # GET isteği için skor bilgilerini gönder
    return render_template('quiz.html', highest_score_user=highest_score_user, user=user)

# Sınav Sonuç Sayfası
@app.route('/result')
def result():
    score = request.args.get('score')
    username = request.args.get('username')
    user = User.query.filter_by(username=username).first()
    highest_score_user = User.query.order_by(User.highest_score.desc()).first()
    return render_template('result.html', score=score, user=user, highest_score_user=highest_score_user)

# Sınav Puanını Hesapla
def calculate_score(answers):
    correct_answers = {
        'q1': '24',  # Soru 1: Bir gün kaç saattir?
        'q2': 'ankara',  # Soru 2: Türkiye'nin başkenti neresidir? (küçük harf)
        'q3': 'flask',  # Soru 3: Python ile web geliştirme için hangi kütüphane kullanılır? (küçük harf)
        'q4': 'tensorflow',  # Soru 4: Bilgisayar görüşü için hangi kütüphane kullanılır? (küçük harf)
        'q5': 'nltk'  # Soru 5: Doğal Dil İşleme için hangi kütüphane kullanılır? (küçük harf)
    }
    score = 0
    for q, a in answers.items():
        # Kullanıcının cevabını küçük harfe çevir
        user_answer = a.lower().strip()  # strip() ile boşlukları temizle
        if q in correct_answers and user_answer == correct_answers[q]:
            score += 20  # Her soru 20 puan
    return score

# Uygulamayı Çalıştır
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)