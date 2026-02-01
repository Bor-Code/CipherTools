import hashlib
import string
import time

class Renk:
    YESIL = '\033[92m'
    KIRMIZI = '\033[91m'
    SARI = '\033[93m'
    RESET = '\033[0m'

def sezar_coz(pass_text):
    alfabe = string.ascii_lowercase
    pass_text = pass_text.lower()
    print(f"\n{Renk.SARI}--- Sezar Şifresi Olasılıkları Deneniyor ---{Renk.RESET}")
    for anahtar in range(1, 27):
        cozum = ""
        for harf in pass_text:
            if harf in alfabe:
                numara = alfabe.find(harf)
                numara = (numara - anahtar) % 26
                cozum += alfabe[numara]
            else:
                cozum += harf
        print(f"Anahtar {anahtar}: {Renk.YESIL}{cozum}{Renk.RESET}")

def hash_kir(target_hash, wordlist_path="wordlist.txt"):
    print(f"\n{Renk.SARI}--- Sözlük Saldırısı Başlatılıyor ---{Renk.RESET}")
    print(f"Hedef Hash: {target_hash}") 
    try:
        dosya = open(wordlist_path, "r", encoding="utf-8")
    except FileNotFoundError:
        print(f"{Renk.KIRMIZI}Hata: Wordlist dosyası bulunamadı!{Renk.RESET}")
        return
    baslangic_zamani = time.time()   
    for satir in dosya:
        kelime = satir.strip()
        kelime_hash = hashlib.md5(kelime.encode('utf-8')).hexdigest()
        if kelime_hash == target_hash:
            gecen_sure = time.time() - baslangic_zamani
            print(f"\n{Renk.YESIL}[+] ŞİFRE BULUNDU!{Renk.RESET}")
            print(f"Şifre: {Renk.YESIL}{kelime}{Renk.RESET}")
            print(f"Süre: {gecen_sure:.4f} saniye")
            dosya.close()
            return
    print(f"\n{Renk.KIRMIZI}[-] Şifre wordlist içinde bulunamadı.{Renk.RESET}")
    dosya.close()