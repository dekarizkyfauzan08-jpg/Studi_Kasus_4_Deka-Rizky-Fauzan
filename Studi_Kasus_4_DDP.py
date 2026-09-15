# Nama : Deka Rizky Fauzan
# Nim : 2609116052
# Kelas : B

produk = {
	"nama": "Aerox",
	"harga": 35000000,
	"stok": 10
}

while True:
	print("\n=== MENU PENGELOLAAN DATA PRODUK ===")
	print("1. Tampilkan data produk")
	print("2. Tambah kategori")
	print("3. Ubah harga")
	print("4. Hapus kategori")
	print("5. Keluar")

	pilihan = input("Pilih menu (1-5): ")

	if pilihan == "1":
		print("\nData produk:")
		for kunci, nilai in produk.items():
			print(f"{kunci.capitalize()}: {nilai}")
	elif pilihan == "2":
		produk["kategori"] = input("Masukkan kategori produk: ")
		print("Kategori berhasil ditambahkan.")
	elif pilihan == "3":
		try:
			produk["harga"] = int(input("Masukkan harga baru: "))
			print("Harga berhasil diubah.")
		except ValueError:
			print("Harga harus berupa angka.")
	elif pilihan == "4":
		if "kategori" in produk:
			produk.pop("kategori")
			print("Kategori berhasil dihapus.")
		else:
			print("Data kategori belum tersedia.")
	elif pilihan == "5":
		print("\nData produk setelah perubahan:")
		for kunci, nilai in produk.items():
			print(f"{kunci.capitalize()}: {nilai}")
		print("Program selesai.")
		break
	else:
		print("Pilihan menu tidak valid.")

