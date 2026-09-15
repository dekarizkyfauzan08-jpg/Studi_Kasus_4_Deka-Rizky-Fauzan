# Studi_Kasus_4_Deka-Rizky-Fauzan
Penjelasan Program

-Dictionary

Dictionary digunakan untuk menyimpan data buku dalam bentuk pasangan key dan value.

Contoh:

Key: judul
Value: Seporsi Mie Ayam Sebelum Mati

Dengan dictionary, data dapat lebih mudah ditambah, diubah, maupun dihapus.

<img width="528" height="145" alt="image" src="https://github.com/user-attachments/assets/f42c5da6-cd65-454a-82bf-2597a38de4fc" />


-Fungsi Tampilkan Data

Program menggunakan fungsi tampilkan_data() untuk menampilkan isi dictionary buku.

def tampilkan_data():

Pada fungsi ini digunakan:

for kunci, nilai in buku.items():

items() digunakan untuk mengambil key dan value secara bersamaan, kemudian ditampilkan menggunakan perulangan.

<img width="585" height="250" alt="image" src="https://github.com/user-attachments/assets/c88ace73-1c55-42c5-ad5c-00f6f2a07b6a" />


-Perulangan Menu

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

<img width="625" height="233" alt="image" src="https://github.com/user-attachments/assets/3dd59c4a-e95c-4c79-a7e6-e32390308d89" />


Fitur Program
-Menampilkan Data Buku

Pada menu pertama, program akan menampilkan semua data buku yang tersimpan di dalam dictionary.

Contoh:

judul: Seporsi Mie Ayam Sebelum Mati
penulis: Brian Khrisna
tahun_terbit: 2025

<img width="268" height="51" alt="image" src="https://github.com/user-attachments/assets/e985bbda-a5a4-45a1-b254-306c36ad8419" />


-Menambahkan Data Penerbit

Menu kedua digunakan untuk menambahkan data baru ke dictionary.

Kode yang digunakan:

buku["penerbit"] = penerbit

Data penerbit akan ditambahkan sebagai key baru pada dictionary.

<img width="582" height="158" alt="image" src="https://github.com/user-attachments/assets/2b39e378-30e4-451b-b5b5-1a431fb65e6f" />


-Mengubah Data Penulis

Menu ketiga digunakan untuk mengganti data penulis.

Kode yang digunakan:

buku["penulis"] = penulis_baru

Nilai dari key penulis akan berubah sesuai input pengguna.

<img width="707" height="166" alt="image" src="https://github.com/user-attachments/assets/8adc6cbe-fcb9-407b-abfc-55a96b2cec17" />


-Menghapus Data Penerbit

Menu keempat digunakan untuk menghapus data penerbit.

Kode yang digunakan:

buku.pop("penerbit")

Sebelum menghapus, program mengecek apakah data penerbit tersedia menggunakan:

if "penerbit" in buku:

<img width="591" height="172" alt="image" src="https://github.com/user-attachments/assets/5f19fafd-28a1-4020-aefc-77bdad675dfd" />

-Menampilkan Data Setelah Perubahan

Menu kelima digunakan untuk melihat data buku setelah dilakukan perubahan, baik penambahan, pengubahan, maupun penghapusan data.

<img width="641" height="175" alt="image" src="https://github.com/user-attachments/assets/5939e8ce-f838-4a99-8f07-7f0e7af0bd83" />


-Keluar Program

Menu keenam digunakan untuk menghentikan program.

Kode:

break

break berfungsi untuk menghentikan perulangan while.

<img width="672" height="136" alt="image" src="https://github.com/user-attachments/assets/367e22af-bf13-4c38-b4f0-50204210ddbf" />


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

<img width="387" height="187" alt="image" src="https://github.com/user-attachments/assets/5eacc29e-a7a9-4457-a7ac-1663f8e31a4e" />





<img width="477" height="857" alt="Cuplikan layar 2026-09-15 215050" src="https://github.com/user-attachments/assets/14015dae-5447-4408-9ac9-baa297bed04d" />







<img width="426" height="777" alt="image" src="https://github.com/user-attachments/assets/6847cd9c-07ec-4ed0-83b6-699be1604947" />


<img width="395" height="547" alt="image" src="https://github.com/user-attachments/assets/16ee87be-ee6d-45b2-9b3f-ad81b531f9ba" />


<img width="392" height="208" alt="image" src="https://github.com/user-attachments/assets/d17f6b79-dccd-4222-8945-6564e66fa715" />



Kesimpulan
Program ini dapat digunakan untuk mengelola data buku sederhana menggunakan dictionary Python.
Melalui menu yang tersedia, pengguna dapat melihat, menambahkan, mengubah, dan menghapus data buku dengan mudah.
