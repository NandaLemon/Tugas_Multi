import sqlite3
from tkinter import Tk, Label, Entry, Button

# Fungsi untuk membuat tabel jika belum ada
def create_table():
    conn = sqlite3.connect('c:nilai_siswa.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS nilai_siswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama_siswa TEXT,
            biologi INTEGER,
            fisika INTEGER,
            inggris INTEGER,
            prediksi_fakultas TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Fungsi untuk memasukkan data ke tabel
def insert_data(nama_siswa, biologi, fisika, inggris, prediksi_fakultas):
    conn = sqlite3.connect('nilai_siswa.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama_siswa, biologi, fisika, inggris, prediksi_fakultas))

    conn.commit()
    conn.close()

# Fungsi untuk menangani klik tombol submit
def submit_nilai():
    nama_siswa = entry_nama.get()
    biologi = int(entry_biologi.get())
    fisika = int(entry_fisika.get())
    inggris = int(entry_inggris.get())

    # Menentukan prediksi fakultas berdasarkan nilai tertinggi
    max_nilai = max(biologi, fisika, inggris)
    if max_nilai == biologi:
        prediksi_fakultas = 'Kedokteran'
    elif max_nilai == fisika:
        prediksi_fakultas = 'Teknik'
    else:
        prediksi_fakultas = 'Bahasa'

    insert_data(nama_siswa, biologi, fisika, inggris, prediksi_fakultas)
    label_hasil.config(text=f'Nilai {nama_siswa} berhasil disubmit. Prediksi Fakultas: {prediksi_fakultas}')

# Membuat tabel jika belum ada
create_table()

# Membuat antarmuka pengguna menggunakan Tkinter
root = Tk()
root.title('Input Nilai Siswa')

label_nama = Label(root, text='Nama Siswa:')
label_nama.grid(row=0, column=0)

entry_nama = Entry(root)
entry_nama.grid(row=0, column=1)

label_biologi = Label(root, text='Nilai Biologi:')
label_biologi.grid(row=1, column=0)

entry_biologi = Entry(root)
entry_biologi.grid(row=1, column=1)

label_fisika = Label(root, text='Nilai Fisika:')
label_fisika.grid(row=2, column=0)

entry_fisika = Entry(root)
entry_fisika.grid(row=2, column=1)

label_inggris = Label(root, text='Nilai Inggris:')
label_inggris.grid(row=3, column=0)

entry_inggris = Entry(root)
entry_inggris.grid(row=3, column=1)

button_submit = Button(root, text='Submit Nilai', command=submit_nilai)
button_submit.grid(row=4, column=0, columnspan=2)

label_hasil = Label(root, text='')
label_hasil.grid(row=5, column=0, columnspan=2)

root.mainloop()
