import customtkinter as ctk
import hashlib
import itertools
import threading
import os
from tkinter import filedialog, messagebox

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class CipherToolsApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CipherTools Pro - Cyber Security Suite")
        self.geometry("700x500")
        self.resizable(False, False)

        self.logo_label = ctk.CTkLabel(self, text="🛡️ CipherTools v2.0", font=ctk.CTkFont(size=24, weight="bold"))
        self.logo_label.pack(pady=20)

        self.tabview = ctk.CTkTabview(self, width=650, height=400)
        self.tabview.pack(padx=20, pady=10)

        self.tab_gen = self.tabview.add("Hash Oluştur")
        self.tab_crack = self.tabview.add("Hash Kırıcı")
        self.tab_file = self.tabview.add("Dosya Kontrol")
        self.tab_word = self.tabview.add("Wordlist Yap")

        self.setup_generator_tab()
        self.setup_cracker_tab()
        self.setup_file_tab()
        self.setup_wordlist_tab()

    def setup_generator_tab(self):
        lbl = ctk.CTkLabel(self.tab_gen, text="Metni girin, kriptografik özetini alın.", font=("Arial", 14))
        lbl.pack(pady=10)

        self.gen_entry = ctk.CTkEntry(self.tab_gen, width=400, placeholder_text="Metni buraya yazın...")
        self.gen_entry.pack(pady=10)

        btn = ctk.CTkButton(self.tab_gen, text="Hash Hesapla", command=self.run_generator)
        btn.pack(pady=10)

        self.gen_textbox = ctk.CTkTextbox(self.tab_gen, width=500, height=150)
        self.gen_textbox.pack(pady=10)

    def run_generator(self):
        text = self.gen_entry.get()
        if not text: return
        
        veri = text.encode('utf-8')
        md5 = hashlib.md5(veri).hexdigest()
        sha1 = hashlib.sha1(veri).hexdigest()
        sha256 = hashlib.sha256(veri).hexdigest()

        result = f"Girdi: {text}\n\nMD5:\n{md5}\n\nSHA-1:\n{sha1}\n\nSHA-256:\n{sha256}"
        self.gen_textbox.delete("0.0", "end")
        self.gen_textbox.insert("0.0", result)

    def setup_cracker_tab(self):
        lbl = ctk.CTkLabel(self.tab_crack, text="MD5 Hash ve Wordlist dosyasını seçin.", font=("Arial", 14))
        lbl.pack(pady=10)

        self.crack_entry = ctk.CTkEntry(self.tab_crack, width=400, placeholder_text="Kırılacak MD5 Hash'i yapıştır...")
        self.crack_entry.pack(pady=5)

        self.crack_file_btn = ctk.CTkButton(self.tab_crack, text="Wordlist Seç (.txt)", command=self.select_wordlist, fg_color="gray")
        self.crack_file_btn.pack(pady=5)

        self.crack_start_btn = ctk.CTkButton(self.tab_crack, text="SALDIRIYI BAŞLAT 🚀", command=self.start_cracking_thread, fg_color="red")
        self.crack_start_btn.pack(pady=20)

        self.crack_status = ctk.CTkLabel(self.tab_crack, text="Durum: Bekleniyor...", text_color="orange")
        self.crack_status.pack()
        
        self.selected_wordlist = None

    def select_wordlist(self):
        filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if filename:
            self.selected_wordlist = filename
            self.crack_file_btn.configure(text=f"Seçildi: {os.path.basename(filename)}")

    def start_cracking_thread(self):
        threading.Thread(target=self.run_cracker, daemon=True).start()

    def run_cracker(self):
        target = self.crack_entry.get().strip()
        if not target or not self.selected_wordlist:
            self.crack_status.configure(text="Hata: Hash veya Dosya eksik!", text_color="red")
            return

        self.crack_status.configure(text="Saldırı sürüyor... Lütfen bekleyin.", text_color="yellow")
        self.crack_start_btn.configure(state="disabled")

        try:
            with open(self.selected_wordlist, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    word = line.strip()
                    if hashlib.md5(word.encode()).hexdigest() == target:
                        self.crack_status.configure(text=f"✅ ŞİFRE BULUNDU: {word}", text_color="#00FF00", font=("Arial", 18, "bold"))
                        self.crack_start_btn.configure(state="normal")
                        return
            
            self.crack_status.configure(text="❌ Şifre listede bulunamadı.", text_color="red")
        except Exception as e:
            self.crack_status.configure(text=f"Hata: {str(e)}", text_color="red")
        
        self.crack_start_btn.configure(state="normal")

    def setup_file_tab(self):
        lbl = ctk.CTkLabel(self.tab_file, text="Dosya bütünlüğünü doğrula.", font=("Arial", 14))
        lbl.pack(pady=10)

        self.file_path_lbl = ctk.CTkLabel(self.tab_file, text="Dosya seçilmedi", text_color="gray")
        self.file_path_lbl.pack(pady=5)

        btn_sel = ctk.CTkButton(self.tab_file, text="Dosya Seç", command=self.select_integrity_file)
        btn_sel.pack(pady=5)

        self.file_hash_result = ctk.CTkTextbox(self.tab_file, width=500, height=80)
        self.file_hash_result.pack(pady=10)

        self.orig_hash_entry = ctk.CTkEntry(self.tab_file, width=400, placeholder_text="Orijinal SHA-256 değerini yapıştır (Opsiyonel)")
        self.orig_hash_entry.pack(pady=5)

        btn_check = ctk.CTkButton(self.tab_file, text="Karşılaştır", command=self.compare_hashes)
        btn_check.pack(pady=5)

        self.compare_result_lbl = ctk.CTkLabel(self.tab_file, text="")
        self.compare_result_lbl.pack()

    def select_integrity_file(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.file_path_lbl.configure(text=os.path.basename(filename))
            sha256_hash = hashlib.sha256()
            with open(filename, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            self.calculated_hash = sha256_hash.hexdigest()
            self.file_hash_result.delete("0.0", "end")
            self.file_hash_result.insert("0.0", self.calculated_hash)

    def compare_hashes(self):
        orig = self.orig_hash_entry.get().strip()
        if not orig:
            return
        if orig == self.calculated_hash:
            self.compare_result_lbl.configure(text="✅ DOĞRULANDI: Dosya Orijinal.", text_color="green", font=("Arial", 16, "bold"))
        else:
            self.compare_result_lbl.configure(text="🚨 DİKKAT: Hashler uyuşmuyor!", text_color="red", font=("Arial", 16, "bold"))

    def setup_wordlist_tab(self):
        lbl = ctk.CTkLabel(self.tab_word, text="Hızlı Wordlist Oluşturucu", font=("Arial", 14))
        lbl.pack(pady=10)
        
        self.wl_combo = ctk.CTkComboBox(self.tab_word, values=["4 Haneli PIN (0000-9999)", "Kişiye Özel Kombinasyon"])
        self.wl_combo.pack(pady=10)

        self.wl_input = ctk.CTkEntry(self.tab_word, placeholder_text="Hedef kelime (Sadece Kişiye Özel için)")
        self.wl_input.pack(pady=10)

        btn = ctk.CTkButton(self.tab_word, text="Oluştur ve Kaydet", command=self.generate_wordlist)
        btn.pack(pady=10)
        
        self.wl_status = ctk.CTkLabel(self.tab_word, text="")
        self.wl_status.pack()

    def generate_wordlist(self):
        choice = self.wl_combo.get()
        filename = "wordlist_gui.txt"
        
        try:
            with open(filename, "w") as f:
                if "PIN" in choice:
                    for i in range(10000):
                        f.write(str(i).zfill(4) + "\n")
                else:
                    target = self.wl_input.get()
                    if not target:
                        self.wl_status.configure(text="Hata: Kelime girin!", text_color="red")
                        return
                    ekler = ["1", "123", "1903", "1905", "1907", "2024", "2025"]
                    f.write(target + "\n")
                    for ek in ekler:
                        f.write(target + ek + "\n")
                        f.write(ek + target + "\n")
            
            self.wl_status.configure(text=f"✅ '{filename}' oluşturuldu!", text_color="green")
        except Exception as e:
             self.wl_status.configure(text=f"Hata: {e}", text_color="red")

if __name__ == "__main__":
    app = CipherToolsApp()
    app.mainloop()