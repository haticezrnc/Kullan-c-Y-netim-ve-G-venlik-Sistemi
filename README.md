# Kullanıcı-Yönetim-ve-Güvenlik-Sistemi
Güvenli kullanıcı kayıt ve giriş sistemi. Şifreler hashlenir, giriş sonrası API'den veri çekilir ve dosyaya kaydedilir.
# Kullanıcı Yönetim ve Güvenlik Sistemi

Bu Python projesi, kullanıcıların kayıt olmasını, güvenli bir şekilde giriş yapmasını ve giriş sonrası bir web API'sinden veri çekip bu verileri kaydetmesini sağlar.

---

## Özellikler

- **Güvenli Kayıt ve Giriş**:
  - Şifreler, `SHA-256` algoritmasıyla hashlenir ve `salt` kullanılarak güvenli hale getirilir.
- **API Entegrasyonu**:
  - Giriş sonrası, bir web API'sinden veri çekilir.
  - Çekilen veriler hem terminalde gösterilir hem de dosyaya kaydedilir.
- **Hata Yönetimi**:
  - Kullanıcı hataları ve sistem hataları detaylı bir şekilde ele alınır.
- **Dosya Yönetimi**:
  - Kullanıcı bilgileri ve çekilen veriler dosyada saklanır.

---

## Kurulum

### Gereksinimler

- **Python 3.7** veya üzeri yüklü olmalıdır.
- Gerekli Python kütüphaneleri:
  - `requests`
  - `hashlib` (Python ile birlikte gelir).

### Adım 1: Depoyu Klonlayın

```bash
git clone https://github.com/kullaniciadi/kullanici-yonetim-sistemi.git
cd kullanici-yonetim-sistemi

### Adım 2: Gerekli Kütüphaneleri Yükleyin
pip install requests

Kullanım

Projeyi Çalıştırın:
python main.py
Kullanıcı Kayıt ve Giriş İşlemleri:
Sistem, kayıtlı kullanıcı bilgilerinin saklandığı kullanici_verileri.txt dosyasını kullanır.
Şifreler hashlenmiş olarak saklanır.
Giriş Yapıldıktan Sonra:
Web API'sinden veri çekilir ve cekilen_veriler.txt dosyasına kaydedilir.
İlk 5 gönderi terminalde gösterilir.
Örnek Kullanım

Terminalde:
Kayıt Ol:

--- Kullanıcı Yönetim Sistemi ---
1. Kayıt Ol
2. Giriş Yap
3. Çıkış
Seçiminizi yapın (1-3): 1
Kullanıcı adı: test_user
Şifre: test_password
Kayıt başarılı!
Giriş Yap:

--- Kullanıcı Yönetim Sistemi ---
1. Kayıt Ol
2. Giriş Yap
3. Çıkış
Seçiminizi yapın (1-3): 2
Kullanıcı adı: test_user
Şifre: test_password
Giriş başarılı!
API'den veri çekiliyor...
API'den Çekilen İlk 5 Veri:
ID: 1, Başlık: sunt aut facere repellat provident occaecati excepturi optio reprehenderit
ID: 2, Başlık: qui est esse
...
Proje Yapısı

kullanici-yonetim-sistemi/
│
├── main.py                 # Ana Python dosyası
├── kullanici_verileri.txt  # Kullanıcı bilgilerini saklayan dosya
├── cekilen_veriler.txt     # Çekilen verileri saklayan dosya
└── README.md               # Proje açıklama dosyası
Lisans

Bu proje MIT Lisansı ile lisanslanmıştır. Daha fazla bilgi için LICENSE dosyasını inceleyebilirsiniz
