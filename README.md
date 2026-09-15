# Studi_Kasus_4_Deka-Rizky-Fauzan
1. Inisialisasi Data Produk

Program diawali dengan membuat sebuah dictionary bernama produk yang digunakan untuk menyimpan informasi produk. Data awal yang disimpan berupa nama produk, harga, dan jumlah stok. Penggunaan dictionary memudahkan program dalam mengakses dan mengubah data berdasarkan kunci seperti nama, harga, dan stok.

2. Perulangan Menu Utama

Bagian while True digunakan agar program dapat berjalan secara terus-menerus sampai pengguna memilih menu keluar. Di dalam perulangan ini terdapat tampilan menu yang memberikan beberapa pilihan kepada pengguna, yaitu melihat data produk, menambahkan kategori, mengubah harga, menghapus kategori, dan keluar dari program.

3. Input Pilihan Pengguna

Variabel pilihan digunakan untuk menerima masukan dari pengguna berdasarkan menu yang tersedia. Nilai input tersebut kemudian digunakan sebagai kondisi untuk menentukan proses yang akan dijalankan menggunakan percabangan if-elif-else.

4. Menampilkan Data Produk

Pada pilihan menu pertama, program akan menampilkan seluruh data yang terdapat dalam dictionary produk. Perulangan for digunakan untuk membaca setiap pasangan kunci dan nilai pada data produk, kemudian menampilkannya ke layar.

5. Menambahkan Kategori Produk

Pada pilihan kedua, program memberikan fitur untuk menambahkan data baru berupa kategori produk. Data kategori dimasukkan oleh pengguna melalui input() dan kemudian disimpan ke dalam dictionary produk dengan kunci baru bernama kategori.

6. Mengubah Harga Produk

Pada pilihan ketiga, pengguna dapat mengganti harga produk yang sudah ada dengan harga baru. Program menggunakan try-except untuk menangani kemungkinan kesalahan jika pengguna memasukkan nilai yang bukan angka, sehingga program tetap dapat berjalan tanpa berhenti secara tiba-tiba.

7. Menghapus Kategori Produk

Pada pilihan keempat, program akan memeriksa apakah data kategori tersedia di dalam dictionary. Jika kategori ditemukan, data tersebut akan dihapus menggunakan fungsi pop(). Jika kategori belum ada, program akan menampilkan pesan bahwa data kategori belum tersedia.

8. Keluar dari Program

Pada pilihan kelima, program akan menampilkan kembali seluruh data produk setelah dilakukan perubahan. Setelah itu, perintah break digunakan untuk menghentikan perulangan sehingga program dapat selesai dijalankan.

9. Kondisi Pilihan Tidak Valid

Bagian terakhir digunakan untuk menangani input pengguna yang tidak sesuai dengan pilihan menu yang tersedia. Jika pengguna memasukkan angka selain 1 sampai 5, program akan memberikan pesan bahwa pilihan menu tidak valid.

-OUTPUT PROGRAM-

1.Tampilan Menu Awal

<img width="395" height="171" alt="image" src="https://github.com/user-attachments/assets/9f5fc039-3d66-4497-a14d-9abe97f4d6e5" />


Screenshot ini menunjukkan bahwa program berhasil berjalan dan menu utama dapat ditampilkan.

2.Menampilkan Data Produk
   
<img width="337" height="317" alt="image" src="https://github.com/user-attachments/assets/08f8287e-d453-4814-80c2-d38137ebef19" />

Screenshot ini menunjukkan fitur membaca dan menampilkan data dari dictionary berhasil dijalankan.

3.Menambahkan Kategori

<img width="410" height="226" alt="image" src="https://github.com/user-attachments/assets/998e9b51-5b8b-425c-b886-bef0e561115e" />


Screenshot ini menunjukkan program dapat menambahkan data baru ke dalam dictionary.

4. Mengubah Harga

<img width="356" height="218" alt="image" src="https://github.com/user-attachments/assets/32b30eac-78ea-4265-9d3c-86f819e73155" />


Screenshot ini menunjukkan fitur perubahan data produk berhasil dilakukan.

5. Menghapus Kategori dan Keluar Program

<img width="400" height="506" alt="image" src="https://github.com/user-attachments/assets/d5061504-cb4d-4b3a-b3cb-058e76657233" />


Screenshot ini menunjukkan bahwa data dapat dihapus dan program dapat berhenti dengan baik.
