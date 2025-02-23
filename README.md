# Python PRO DST Supply Project

Bu proje, **Kodland Eğitmenlik Sınavı** kapsamında geliştirilmiştir. Amaç, **Flask** ve **veritabanı** kullanarak gençlere yönelik **dinamik bir sınav web sitesi** oluşturmaktır.

## 🚀 Proje Özellikleri

- 📌 **Sınav İçeriği**:  
  - Python ile sohbet botu otomasyonu (Discord.py)  
  - Python ile web geliştirme (Flask)  
  - Python ile yapay zeka geliştirme  
  - Bilgisayar görüşü (TensorFlow, ImageAI)  
  - Doğal Dil İşleme (NLTK, BeautifulSoup)  

- 🗃 **Veritabanı**: Flask-SQLAlchemy kullanılarak ilişkisel veritabanı yönetimi sağlanmıştır.  
- 🎯 **Sonuç Gösterimi**:  
  - Kullanıcı sınavı tamamladığında aldığı puanı görüntüler.  
  - Kullanıcı en son aldığı ve en yüksek puanlarını görebilir.  
- 📊 **Genel İstatistikler**:  
  - Tüm kullanıcılar arasında alınan **en yüksek puan** ve mevcut kullanıcının **en yüksek puanı** ekranın sağ üst köşesinde gösterilir.  
- 👨‍💻 **Yazar Bilgisi**: Web sitesinin her sayfasının alt kısmında yazar hakkında bilgi bulunmaktadır.  

---

## 📥 Kurulum ve Çalıştırma

1. **Depoyu Klonlayın**:
   ```bash
   git clone https://github.com/Aliemree/python_pro_dst_supply_project.git
2. **Gerekli Paketleri Yükleyin**:
   ```bash
   pip install -r requirements.txt
3. **Veritabanını Oluşturun**:
   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
4. **Uygulamayı Başlatın**:
   ```bash
   python app.py
## 🌐 Canlı Demo

Proje **PythonAnywhere** üzerinde yayında!  
🔗 **Canlı Demo:** [Buraya Tıklayarak İnceleyebilirsiniz](https://kullaniciadi.pythonanywhere.com/)  

## 📂 Proje Yapısı

📦 python_pro_dst_supply_project ├── 📂 static/ # CSS, JavaScript ve medya dosyaları ├── 📂 templates/ # HTML şablon dosyaları ├── 📂 models/ # Veritabanı modelleri ├── 📂 routes/ # Flask uygulama rotaları ├── app.py # Ana uygulama dosyası ├── config.py # Yapılandırma ayarları ├── requirements.txt # Gerekli bağımlılıklar ├── README.md # Proje dokümantasyonu └── LICENSE # Lisans bilgisi

---

## 🔧 Kullanılan Teknolojiler

Bu projede aşağıdaki teknolojiler kullanılmıştır:

- 🐍 **Python 3.x**  
- 🌐 **Flask** - Web framework  
- 🗃 **Flask-SQLAlchemy** - Veritabanı yönetimi  
- 🛠 **SQLite** (tercihe bağlı **PostgreSQL** veya **MySQL**)  
- 🎨 **HTML, CSS, JavaScript** - Ön yüz geliştirme  
- ☁ **PythonAnywhere** - Hosting platformu  

---

## 🤝 Katkıda Bulunanlar

Bu projeye katkı sağlayan kişiler:

👤 **Ali Emre**  
📌 **Proje Geliştiricisi ve Tasarımcısı**  

Eğer projeye katkıda bulunmak istiyorsanız:

1. Bu depoyu **fork** edin.  
2. Kendi branch’inizde değişiklik yapın.  
3. **Pull request (PR)** oluşturun.  

Her türlü katkıya açığız! 🚀  

---

## 📜 Lisans

Bu proje **MIT Lisansı** altında lisanslanmıştır. Daha fazla bilgi için [LICENSE](LICENSE) dosyasına göz atabilirsiniz.

---

📌 **Bu proje, gençlere yönelik interaktif ve öğretici bir sınav platformu sunmayı amaçlamaktadır. Katkılarınız ve geri bildirimleriniz için teşekkür ederiz!** 🎯🚀
