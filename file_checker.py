import hashlib

def dosya_dogrula():
    print("\n--- 📂 DOSYA BÜTÜNLÜK KONTROLÜ ---")
    print("İpucu: Dosya aynı klasörde olmalı veya tam yolunu yazmalısınız.")
    dosya_yolu = input("Dosya adını girin (Örn: image.png): ")
    try:
        sha256_hash = hashlib.sha256()
        with open(dosya_yolu, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        dosya_hash = sha256_hash.hexdigest()
        print(f"\nDosyanın SHA-256 Değeri:\n{dosya_hash}")
        orijinal_hash = input("\nKarşılaştırmak için orijinal hash değerini girin (Yoksa Enter'a bas): ").strip()
        if orijinal_hash:
            if orijinal_hash == dosya_hash:
                print("✅ DOĞRULANDI: Dosya orijinal ve güvenli.")
            else:
                print("🚨 UYARI: Hashler uyuşmuyor! Dosya değiştirilmiş veya bozuk olabilir!")       
    except FileNotFoundError:
        print("HATA: Belirtilen dosya bulunamadı.")