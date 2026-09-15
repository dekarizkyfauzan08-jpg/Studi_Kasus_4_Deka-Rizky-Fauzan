# Studi_Kasus_4_Deka-Rizky-Fauzan
Penjelasan Program
1. Dictionary

Dictionary digunakan untuk menyimpan data buku dalam bentuk pasangan key dan value.

Contoh:

Key: judul
Value: Seporsi Mie Ayam Sebelum Mati

Dengan dictionary, data dapat lebih mudah ditambah, diubah, maupun dihapus.

2. Fungsi Tampilkan Data

Program menggunakan fungsi tampilkan_data() untuk menampilkan isi dictionary buku.

def tampilkan_data():

Pada fungsi ini digunakan:

for kunci, nilai in buku.items():

items() digunakan untuk mengambil key dan value secara bersamaan, kemudian ditampilkan menggunakan perulangan.

3. Perulangan Menu

Program menggunakan:

while True:

Perulangan ini membuat menu dapat dijalankan berulang kali sampai pengguna memilih menu keluar.

Menu yang tersedia:

Tampilkan data buku
Tambahkan data penerbit
Ubah data penulis
Hapus data penerbit
Tampilkan data setelah perubahan
Keluar
Fitur Program
1. Menampilkan Data Buku

Pada menu pertama, program akan menampilkan semua data buku yang tersimpan di dalam dictionary.

Contoh:

judul: Seporsi Mie Ayam Sebelum Mati
penulis: Brian Khrisna
tahun_terbit: 2025
2. Menambahkan Data Penerbit

Menu kedua digunakan untuk menambahkan data baru ke dictionary.

Kode yang digunakan:

buku["penerbit"] = penerbit

Data penerbit akan ditambahkan sebagai key baru pada dictionary.

3. Mengubah Data Penulis

Menu ketiga digunakan untuk mengganti data penulis.

Kode yang digunakan:

buku["penulis"] = penulis_baru

Nilai dari key penulis akan berubah sesuai input pengguna.

4. Menghapus Data Penerbit

Menu keempat digunakan untuk menghapus data penerbit.

Kode yang digunakan:

buku.pop("penerbit")

Sebelum menghapus, program mengecek apakah data penerbit tersedia menggunakan:

if "penerbit" in buku:
5. Menampilkan Data Setelah Perubahan

Menu kelima digunakan untuk melihat data buku setelah dilakukan perubahan, baik penambahan, pengubahan, maupun penghapusan data.

6. Keluar Program

Menu keenam digunakan untuk menghentikan program.

Kode:

break

break berfungsi untuk menghentikan perulangan while.

Konsep Python yang Digunakan

Beberapa konsep Python yang diterapkan dalam program ini:

Dictionary untuk menyimpan data.
Perulangan while untuk menjalankan menu secara berulang.
Perulangan for untuk membaca isi dictionary.
Percabangan if-elif-else untuk memilih menu.
Fungsi untuk membuat kode lebih terstruktur.
items() untuk mengambil key dan value.
pop() untuk menghapus data pada dictionary.
Screenshot Hasil Program

Tambahkan screenshot hasil menjalankan program di bawah ini:

(Masukkan gambar hasil output program di sini)

Kesimpulan

Program ini dapat digunakan untuk mengelola data buku sederhana menggunakan dictionary Python.
Melalui menu yang tersedia, pengguna dapat melihat, menambahkan, mengubah, dan menghapus data buku dengan mudah.
