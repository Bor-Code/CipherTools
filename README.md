# CipherTools – Şifreleme Araçları

Şifreleme mi, şifre kırma mı, yoksa her ikisi mi? CipherTools, bunların hepsini tek bir çatı altında sana sunuyor. İster yeni başlayan biri ol, ister deneyimli bir geliştirici — bu araç sana özel.

---

## Bir Bakışta Ne Yapıyor?

CipherTools, üç temel yetenek üzerine kurulu bir Python projesi:

**1. Şifreleme (Generator)** — Yazdığın mesajı klasik yöntemlerle şifreler. Caesar mi, Vigenère mi, senin tercih ettiğin.

**2. Şifre Kırma (Cracker)** — Elinde bir şifreli metin var ama anahtarı yok mu? Otomatik tekniklerle onu çözmeye çalışır.

**3. Grafik Arayüz (GUI)** — Hiç terminal üzerinden vakit kaybetmek istemiyorsanız, kullanıcı dostu bir arayüzle her şeyi fare tıklıyla yapabilirsiniz.

Bunun yanı sıra projede birkaç yardımcı modül de var: kelime listesi oluşturan bir fabrika (`list_maker.py`), dosya bütünlüğünü kontrol eden bir bekçi (`file_checker.py`) ve her şeyin başladığı kapı (`main.py`).

---

## Proje Yapısı

```text
CipherTools/
│
├── main.py            # Uygulamanın başladığı nokta
├── gui_app.py         # Grafik arayüz
├── generator.py       # Şifreleme ve şifre çözme motoru
├── cracker.py         # Şifre kırma motoru
├── list_maker.py      # Kelime listesi oluşturucu
├── file_checker.py    # Dosya kontrolü
```

## Her Modül Ne İş Yapıyor?

**main.py** — Projenin kapıcısı. Çalıştırıldığında, kullanıcının GUI mi yoksa terminal mi istediğini anlar ve ona göre yönlendirir. Şifreleme mantığıyla hiç ilgilenmez, sadece yönlendirir.

**gui_app.py** — Grafik arayüzün kendisi. Python'ın tkinter (veya customtkinter) kütüphanesine dayanır. Şifre türünü seç, metni yaz, sonucu gör — hepsi burada.

**generator.py** — Asıl şifreleme işinin yapıldığı yer. Sezar şifresi (harf kaydırma), Vigenère şifresi (anahtar kelime tabanlı kaydırma) ve MD5/SHA-256 gibi hash işlemleri burada yaşar.

**cracker.py** — Anahtarsız şifre kırma denemelerinin merkezi. Brute force (tüm olasılıkları dener) ve dictionary attack (kelime listesi kullanır) gibi iki farklı yöntem kullansa da hedef aynı: şifrenin anahtarını bulmak.

**list_maker.py** — Kırma saldırıları için kelime listesi üretir. Örneğin 0000'den 9999'a kadar her PIN kodu, veya özel kombinasyonlar yapabilirsin burada.

**file_checker.py** — Dosya yollarını, formatlarını ve hash kontrolüyle bütünlüğünü denetler. Yanlış bir dosya yüklediğinde seni önceden uyarır.

---

## Başlangıç

### Ne Gerekli?

- Python 3.7 veya üzeri bir sürüm
- Standart kütüphaneler kullanıldığı için genellikle ekstra bir şey yüklemen gerekmez. Yalnızca `customtkinter` kullanıldıysa: `pip install customtkinter`

### Kurulum

Önce depoyu bilgisayarına al:
```bash
git clone https://github.com/Bor-Code/CipherTools.git
cd CipherTools
```

### Çalıştırma

GUI ile başlatmak için yalnızca şu kadar yeterli:
```bash
python main.py
```

Terminal üzerinden kullanmak istersen, komutlar da mümkün. Örneğin "Merhaba Dunya" ifadesini Caesar şifresiyle 3 kaydırma ile şifrelemek için:
```bash
python main.py --encrypt --cipher caesar --key 3 --text "Merhaba Dunya"
```

---

## Nasıl Çalışır?

### Şifreleme Akışı

Kullanıcı bir metin ve anahtar girince `main.py` bunları alır ve `generator.py`'ye teslim eder. Generator algoritma mantığını uygular ve sonucu döndürür. Yani:

```
Sen → main.py → generator.py → Şifreli Metin
```

### Kırma Akışı

Elinde yalnızca şifreli metin varsa bu sefer yol farklı: `list_maker.py` anahtar adayları üretir, `cracker.py` bunları tek tek dener, ta ki doğru anahtarı bulana kadar.

```
Şifreli Metin → main.py → list_maker.py → cracker.py → Çözülen Metin + Anahtar
```

---

## Kullanım Örnekleri

### Sezar Şifresi ile Şifreleme

Arayüzü aç, metni ve anahtarı gir, "Şifrele"ye bas.

| | |
|---|---|
| **Girdi** | Saldir |
| **Anahtar** | 3 |
| **Çıktı** | Vdolgx |

### MD5 Hash Kırma

Bir MD5 özeti elde ettin ve arkasında ne olduğunu bulmak istiyorsun. List Maker sekmesinden bir kelime listesi oluştur, ardından Cracker sekmesine geç, hash'i yapıştır ve başlat. Sistem kelime kelime dener.

---

## Mimari Diyagram

Projenin genel yapısını anlamak için şöyle bir zihinsel harita düşün:

```
┌─────────────────────────────────────────────────┐
│                   CipherTools                   │
│                                                 │
│  ┌──────────┐        ┌────────────────────┐     │
│  │  main.py │───────▶│    gui_app.py      │     │
│  │ (Kontrol)│        │     (Arayüz)       │     │
│  └────┬─────┘        └────────────────────┘     │
│       │                                         │
│       ├─▶  generator.py   (Şifreleme Motoru)    │
│       │                                         │
│       ├─▶  cracker.py     (Kırma Motoru)        │
│       │         │                               │
│       │         ▼                               │
│       │    list_maker.py  (Wordlist Üretici)    │
│       │                                         │
│       └─▶  file_checker.py (Dosya Kontrolü)     │
└─────────────────────────────────────────────────┘
```

`main.py` merkezde oturmakta ve diğer tüm modülleri yönetmektedir. Arayüz kullanılırsa `gui_app.py` devreye girer; terminal tercih edilirse her şey `main.py` üzerinden yürür.

---

## Katkıda Bulunmak Ister Misin?

Tabii ki ister! Şöyle yapabilirsin:

1. Depoyu fork'la.
2. Yeni bir branch oluştur: `git checkout -b feature/yeni-ozellik`
3. Değişikliklerini yap ve commit'le.
4. Branch'ini push'la: `git push origin feature/yeni-ozellik`
5. GitHub'da bir Pull Request açın.

---

## Lisans

Bu proje **MIT Lisansı** ile lisanslanmış olup eğitim ve savunma amaçlı geliştirilmiştir.

---

# CipherTools – Encryption Tools

Encryption, decryption, or both? CipherTools offers you all of these under one roof. Whether you're a beginner or an experienced developer — this tool is for you.

---

## What Does It Do at a Glance?

CipherTools is a Python project built on three core capabilities:

**1. Encryption (Generator)** — Encrypts your message using classic methods. Caesar? Vigenère? Your choice.

**2. Cracking (Cracker)** — Got an encrypted text but no key? It tries to decrypt it using automated techniques.

**3. Graphical User Interface (GUI)** — If you don't want to waste time in the terminal, you can do everything with a mouse click using a user-friendly interface.

In addition, the project includes several helper modules: a factory that generates word lists (`list_maker.py`), a guard that checks file integrity (`file_checker.py`), and the gateway where everything begins (`main.py`).

---

## Project Structure

```text
CipherTools/
│
├── main.py            # Where the application starts
├── gui_app.py         # Graphical interface
├── generator.py       # Encryption and decryption engine
├── cracker.py         # Password cracking engine
├── list_maker.py      # Word list generator
├── file_checker.py    # File checker
└── .gitignore         # Git ignore rules
```

---

## What Does Each Module Do?

**main.py** — The project's gatekeeper. When run, it understands whether the user wants the GUI or the terminal and directs them accordingly. It has nothing to do with the encryption logic, it just directs.

**gui_app.py** — The graphical interface itself. It relies on Python's tkinter (or customtkinter) library. Select the encryption type, enter the text, see the result — it's all here.

**generator.py** — Where the actual encryption work happens. Caesar cipher (letter shift), Vigenère cipher (keyword-based shift), and hash operations like MD5/SHA-256 live here.

**cracker.py** — The hub for key-less password cracking attempts. Although it uses two different methods, brute force (tries all possibilities) and dictionary attack (uses a word list), the goal is the same: to find the password key.

**list_maker.py** — Generates word lists for cracking attacks. For example, you can generate every PIN code from 0000 to 9999, or create custom combinations here.

**file_checker.py** — Checks file paths, formats, and integrity with hash verification. It warns you in advance if you load an incorrect file.

---

## Getting Started

### What's Required?

- Python 3.7 or higher
- Since standard libraries are used, you usually don't need to install anything extra. Only if `customtkinter` is used: `pip install customtkinter`

### Installation

First, clone the repository to your computer:
```bash
git clone https://github.com/Bor-Code/CipherTools.git
cd CipherTools
```

### Running

To start with the GUI, just do this:
```bash
python main.py
```

If you want to use it via the terminal, commands are also possible. For example, to encrypt the phrase "Hello World" with the Caesar cipher using a 3-shift:
```bash
python main.py --encrypt --cipher caesar --key 3 --text "Hello World"
```

---

## How Does It Work?

### Encryption Flow

When the user enters text and a key, `main.py` takes them and passes them to `generator.py`. Generator applies the algorithm logic and returns the result. So:

```
You → main.py → generator.py → Encrypted Text
```

### Decryption Flow

If you only have the encrypted text, the process is different: `list_maker.py` generates key candidates, `cracker.py` tries them one by one until it finds the correct key.

```
Encrypted Text → main.py → list_maker.py → cracker.py → Decrypted Text + Key
```

---

## Usage Examples

### Encryption with Caesar Cipher

Open the interface, enter the text and key, press "Encrypt".

| | |
|---|---|
| **Input** | Saldir |
| **Key** | 3 |
| **Output** | Vdolgx |

### MD5 Hash Cracking

You have an MD5 hash and want to find out what it stands for. Create a word list using the List Maker tab, then switch to the Cracker tab, paste the hash, and start. The system tries word by word.

---

## Architectural Diagram

To understand the overall structure of the project, think of a mental map like this:

```
┌─────────────────────────────────────────────────┐
│                   CipherTools                   │
│                                                 │
│  ┌──────────┐        ┌────────────────────┐     │
│  │  main.py │───────▶│    gui_app.py      │     │
│  │ (Control)│        │     (Interface)    │     │
│  └────┬─────┘        └────────────────────┘     │
│       │                                         │
│       ├─▶  generator.py   (Encryption Engine)   │
│       │                                         │
│       ├─▶  cracker.py     (Cracking Engine)     │
│       │         │                               │
│       │         ▼                               │
│       │    list_maker.py  (Wordlist Generator)  │
│       │                                         │
│       └─▶  file_checker.py (File Checker)       │
└─────────────────────────────────────────────────┘
```

`main.py` sits at the center and manages all other modules. If the GUI is used, `gui_app.py` comes into play; if the terminal is preferred, everything runs through `main.py`.

---

## Want to Contribute?

Of course you do! Here's how:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/new-feature`
3. Make your changes and commit them.
4. Push your branch: `git push origin feature/new-feature`
5. Open a Pull Request on GitHub.

---

## License

This project is licensed under the **MIT License** and has been developed for educational and defense purposes.
