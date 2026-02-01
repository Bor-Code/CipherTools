import itertools

def wordlist_olustur():
    print("\n--- 📝 WORDLIST OLUŞTURUCU ---")
    print("1. 4 Haneli PIN Kodları (0000-9999)")
    print("2. Özel Kombinasyon (Ad + Sayı)")
    print("3. Basit Harf Kombinasyonları (Brute Force)")
    secim = input("Seçiminiz: ")
    dosya_adi = "my_wordlist.txt"
    if secim == '1':
        print(f"'{dosya_adi}' dosyasına yazılıyor...")
        with open(dosya_adi, "w") as f:
            for i in range(10000):
                f.write(str(i).zfill(4) + "\n")
        print("✅ Tamamlandı!")
    elif secim == '2':
        hedef = input("Hedef kelime girin: ")
        with open(dosya_adi, "w") as f:
            ozel_ekler = ["1", "123", "2023", "2024"]
            f.write(hedef + "\n")
            for ek in ozel_ekler:
                f.write(hedef + ek + "\n")
        print("✅ Tamamlandı!")
    elif secim == '3':
        karakterler = input("Karakterleri girin (Örn: abc): ")
        uzunluk = int(input("Uzunluk: "))
        print("Oluşturuluyor...")
        with open(dosya_adi, "w") as f:
            for p in itertools.product(karakterler, repeat=uzunluk):
                f.write("".join(p) + "\n")
        print("✅ Tamamlandı!")