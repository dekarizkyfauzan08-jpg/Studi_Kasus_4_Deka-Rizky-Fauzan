# Nama : Deka Rizky Fauzan
# Nim : 2609116052
# Kelas : B

buku = {
	"judul": "Seporsi Mie Ayam Sebelum Mati",
	"penulis": "Brian Khrisna",
	"tahun_terbit": 2025,
}


def tampilkan_data():
	"""Menampilkan seluruh data buku."""
	print("\nData Buku")
	print("-" * 20)
	if not buku:
		print("Data buku kosong.")
	else:
		for kunci, nilai in buku.items():
			print(f"{kunci}: {nilai}")


while True:
	print("\n=== Menu Pengelolaan Buku ===")
	print("1. Tampilkan data buku")
	print("2. Tambahkan data penerbit")
	print("3. Ubah data penulis")
	print("4. Hapus data penerbit")
	print("5. Tampilkan data setelah perubahan")
	print("6. Keluar")

	pilihan = input("Pilih menu (1-6): ").strip()

	if pilihan == "1":
		tampilkan_data()
	elif pilihan == "2":
		penerbit = input("Masukkan nama penerbit: ").strip()
		if penerbit:
			buku["penerbit"] = penerbit
			print("Data penerbit berhasil ditambahkan.")
		else:
			print("Nama penerbit tidak boleh kosong.")
	elif pilihan == "3":
		penulis_baru = input("Masukkan nama penulis baru: ").strip()
		if penulis_baru:
			buku["penulis"] = penulis_baru
			print("Data penulis berhasil diubah.")
		else:
			print("Nama penulis tidak boleh kosong.")
	elif pilihan == "4":
		if "penerbit" in buku:
			buku.pop("penerbit")
			print("Data penerbit berhasil dihapus.")
		else:
			print("Data penerbit belum tersedia.")
	elif pilihan == "5":
		tampilkan_data()
	elif pilihan == "6":
		print("Program selesai.")
		break
	else:
		print("Pilihan tidak valid. Silakan pilih menu 1-6.")
