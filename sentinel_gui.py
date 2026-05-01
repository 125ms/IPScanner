import customtkinter as ctk
import socket
from threading import Thread


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ScannerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sentinel Network Scanner")
        self.geometry("500x400")

        self.label = ctk.CTkLabel(self, text="Introduce IP o Dominio:", font=("Roboto", 16))
        self.label.pack(pady=20)

        self.entry = ctk.CTkEntry(self, placeholder_text="127.0.0.1", width=300)
        self.entry.pack(pady=10)

        self.btn_scan = ctk.CTkButton(self, text="Iniciar Escaneo", command=self.start_scan_thread)
        self.btn_scan.pack(pady=20)

        self.textbox = ctk.CTkTextbox(self, width=450, height=200)
        self.textbox.pack(pady=10)

    def start_scan_thread(self):
        Thread(target=self.scan_ports).start()
    
    def scan_ports(self):
        target = self.entry.get()
        self.textbox.delete("0.0", "end")
        self.textbox.insert("end", f"Escaneando: {target}...\n" + "-"*30 + "\n")

        common_ports = [22, 80, 443, 8080, 3306]
        for port in common_ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))

            if result == 0:
                self.textbox.insert("end", f"[+] Puerto {port}: ABIERTO\n")
            else:
                self.textbox.insert("end", f"[-] Puerto {port}: Cerrado\n")
            s.close()

        self.textbox.insert("end", "\nEscaneo finalizado.")

if __name__ == "__main__":
    app = ScannerApp()
    app.mainloop()

