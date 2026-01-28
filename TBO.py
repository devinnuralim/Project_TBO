import customtkinter as ctk
from tkinter import messagebox
import re

# Konfigurasi Tema
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class AppPendaftaran(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Portal Pendaftaran Mahasiswa")
        self.geometry("550x750")

        # Container Utama
        self.frame = ctk.CTkScrollableFrame(self, corner_radius=20)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.header = ctk.CTkLabel(
            self.frame, text="FORMULIR PENDAFTARAN", font=("Helvetica", 22, "bold")
        )
        self.header.pack(pady=(20, 30))

        # Fields
        self.input_nama = self.buat_field("Nama Lengkap", "Hanya huruf dan spasi")
        self.input_nisn = self.buat_field("NISN", "Tepat 10 digit angka")
        self.input_email = self.buat_field("Email", "username@domain.com")
        self.input_telp = self.buat_field("Nomor Telepon", "0 atau +62...")
        self.input_tgl = self.buat_field("Tanggal Lahir", "DD-MM-YYYY")

        # Button
        self.btn_submit = ctk.CTkButton(
            self.frame,
            text="SUBMIT DATA",
            command=self.proses_validasi,
            height=50,
            font=("Helvetica", 14, "bold"),
        )
        self.btn_submit.pack(pady=40, padx=40, fill="x")

    def buat_field(self, label, placeholder):
        label_obj = ctk.CTkLabel(self.frame, text=label, font=("Helvetica", 12, "bold"))
        label_obj.pack(anchor="w", padx=40)
        entry = ctk.CTkEntry(self.frame, placeholder_text=placeholder, height=40)
        entry.pack(pady=(0, 15), padx=40, fill="x")
        return entry

    def proses_validasi(self):
        # Implementasi Regex Sesuai Permintaan Anda
        patterns = {
            "Nama Lengkap": (
                self.input_nama.get(),
                r"^([a-zA-Z\s]+)$",
                "Hanya menerima huruf dan spasi.",
            ),
            "Email": (
                self.input_email.get(),
                r"^[a-zA-Z0-9_\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z\.]{2,6}$",
                "Format email salah (contoh: user@domain.com).",
            ),
            "NISN": (
                self.input_nisn.get(),
                r"^([0-9]{10})$",
                "Harus tepat 10 digit angka.",
            ),
            "Nomor Telepon": (
                self.input_telp.get(),
                r"^(\+62|0)[0-9]{9,12}$",
                "Diawali +62 atau 0, diikuti 9-12 digit angka.",
            ),
            "Tanggal Lahir": (
                self.input_tgl.get(),
                r"^(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-([0-9]{4})$",
                "Format harus DD-MM-YYYY.",
            ),
        }

        # Iterasi Pengecekan (Logika Finite State Automata)
        for field, (value, pattern, error_msg) in patterns.items():
            if not re.match(pattern, value):
                messagebox.showerror(
                    "Validasi Gagal", f"Kesalahan pada {field}:\n{error_msg}"
                )
                return

        messagebox.showinfo(
            "Berhasil", "Data Terverifikasi!\nSemua input masuk ke 'Accepting State'."
        )


if __name__ == "__main__":
    app = AppPendaftaran()
    app.mainloop()
