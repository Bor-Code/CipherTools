import hashlib

def hash_hesapla(metin):
    print("\n--- 🔒 HASH OLUŞTURUCU ---")
    veri = metin.encode('utf-8') 
    md5_degeri = hashlib.md5(veri).hexdigest()
    sha1_degeri = hashlib.sha1(veri).hexdigest()
    sha256_degeri = hashlib.sha256(veri).hexdigest()
    print(f"\n📢 GİRİLEN METİN: {metin}")
    print("-" * 50)
    print(f"🔴 MD5    : {md5_degeri}")
    print(f"🟡 SHA-1  : {sha1_degeri}")
    print(f"🟢 SHA-256: {sha256_degeri}")
    print("-" * 50)