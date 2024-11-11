import tkinter as tk
from tkinter import ttk

def hasil_prediksi():
    try:
        nilai = []
        for entry in entries:
            nilai.append(float(entry.get()))  # Mengubah input menjadi float
            
        # Setelah nilai berhasil diambil, tampilkan hasil prediksi
        hasil_label.config(text="Prediksi: Teknologi Informasi", fg="blue")
        
    except ValueError:
        # Jika ada input yang bukan angka, tampilkan pesan kesalahan
        hasil_label.config(text="Error: Pastikan semua input adalah angka.", fg="red")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="light blue")  # Mengubah warna background utama

judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16), bg="light blue")
judul_label.pack(pady=10)

#mengatur bagian mapel.
entries = []
for i in range(1, 11):  # Menggunakan range untuk membuat label "Mata Pelajaran 1" hingga "Mata Pelajaran 10"
    frame = tk.Frame(root, bg="light blue") 
    frame.pack(pady=5, padx=10, anchor="w")
    label = tk.Label(frame, text=f"Mata Pelajaran {i}", width=35, anchor="w", bg="light blue")
    label.pack(side="left")
    entry = tk.Entry(frame, width=10)
    entry.pack(side="right")
    entries.append(entry)
#menampilkan tombol
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.pack(pady=20)
#menambahkan kolom isi
hasil_label = tk.Label(root, text="", font=("Arial", 14), fg="blue", bg="light blue")
hasil_label.pack(pady=10)
#menampilkan
root.mainloop()