import generator     
import cracker     
import file_checker 
import list_maker    

def menu():
    while True:
        print("="*40)
        print("🛡️  CIPHER TOOLS - SİBER GÜVENLİK ARACI")
        print("="*40)
        print("1. Hash Oluştur (Generator)")
        print("2. Hash Kır (Cracker - MD5)")
        print("3. Dosya Doğrula (File Integrity)")
        print("4. Wordlist Oluştur")
        print("5. Çıkış")
        secim = input("Seçiminiz: ")    
        if secim == '1':
            metin = input("Metni girin: ")
            generator.hash_hesapla(metin)       
        elif secim == '2':
            target = input("Kırılacak Hash: ")
            cracker.hash_kir(target)
        elif secim == '3':
            file_checker.dosya_dogrula()       
        elif secim == '4':
            list_maker.wordlist_olustur()       
        elif secim == '5':
            print("Sistemden çıkılıyor... Stay Safe! 🕵️‍♂️")
            break
        else:
            print("Geçersiz seçim!")
if __name__ == "__main__":
    menu()