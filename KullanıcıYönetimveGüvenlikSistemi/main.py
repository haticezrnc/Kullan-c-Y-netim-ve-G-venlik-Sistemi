import hashlib
import requests
import os


def kullanici_kayit():
    """Kullanıcı kaydı oluşturma."""
    print("Kullanıcı Kayıt")
    kullanici_adi = input("Kullanıcı adı: ").strip()
    sifre = input("Şifre: ").strip()

    # Şifreyi hashle
    salt = "guvenli_salt"  # Sabit bir salt
    sifre_hash = hashlib.sha256((sifre + salt).encode()).hexdigest()

    # Kullanıcıyı dosyaya kaydet
    try:
        with open("kullanici_verileri.txt", "a") as dosya:
            dosya.write(f"{kullanici_adi},{sifre_hash}\n")
        print("Kayıt başarılı!")
    except Exception as e:
        print(f"Hata: {e}")


def kullanici_giris():
    """Kullanıcı giriş işlemi."""
    print("Kullanıcı Giriş")
    kullanici_adi = input("Kullanıcı adı: ").strip()
    sifre = input("Şifre: ").strip()

    # Şifreyi hashle
    salt = "guvenli_salt"
    sifre_hash = hashlib.sha256((sifre + salt).encode()).hexdigest()

    try:
        with open("kullanici_verileri.txt", "r") as dosya:
            for satir in dosya:
                kayitli_kullanici, kayitli_hash = satir.strip().split(",")
                if kullanici_adi == kayitli_kullanici and sifre_hash == kayitli_hash:
                    print("Giriş başarılı!")
                    return True
        print("Giriş başarısız! Kullanıcı adı veya şifre yanlış.")
        return False
    except FileNotFoundError:
        print("Kayıtlı kullanıcı bulunamadı! Lütfen önce kayıt olun.")
        return False
    except Exception as e:
        print(f"Hata: {e}")
        return False


def api_veri_cek():
    """Giriş sonrası API'den veri çeker."""
    try:
        print("API'den veri çekiliyor...")
        response = requests.get("https://jsonplaceholder.typicode.com/posts")
        response.raise_for_status()
        veriler = response.json()

        # İlk 5 gönderiyi göster
        print("API'den Çekilen İlk 5 Veri:")
        for veri in veriler[:5]:
            print(f"ID: {veri['id']}, Başlık: {veri['title']}")

        # Verileri dosyaya kaydet
        with open("cekilen_veriler.txt", "w") as dosya:
            for veri in veriler[:5]:
                dosya.write(f"ID: {veri['id']}, Başlık: {veri['title']}\n")
        print("Veriler dosyaya kaydedildi.")
    except requests.exceptions.RequestException as e:
        print(f"API hatası: {e}")
    except Exception as e:
        print(f"Hata: {e}")


def ana_menu():
    """Ana menü."""
    while True:
        print("\n--- Kullanıcı Yönetim Sistemi ---")
        print("1. Kayıt Ol")
        print("2. Giriş Yap")
        print("3. Çıkış")
        secim = input("Seçiminizi yapın (1-3): ").strip()

        if secim == "1":
            kullanici_kayit()
        elif secim == "2":
            if kullanici_giris():
                api_veri_cek()
        elif secim == "3":
            print("Sistemden çıkılıyor...")
            break
        else:
            print("Geçersiz seçim! Lütfen 1-3 arasında bir seçim yapın.")


if __name__ == "__main__":
    ana_menu()
