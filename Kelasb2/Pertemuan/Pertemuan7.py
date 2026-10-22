
# def sapa():
#     return "Hallo Ridho"

# teks_sapaan = sapa()
# print(teks_sapaan)

#fungsi tanpa parameter
# def hitung():
#     return 5 * 3

# print(hitung())

# ==========================================

# #fungsi dengan parameter
# def persegi(sisi): #/ini parameter
#     hasil = sisi*sisi
#     return sisi

# print(5)#/ini argumen

# def sapa(nama):
#     return f"haloo {nama}"

# print(sapa())

# ==========================================

# #prosedur
# def menu():
#     print("1. Create")
#     print("2. Read")
#     print("3. Update")
#     print("4. Delete")

#     pilihan = input("pilihan Menu")

#     #if pilihan = 

# ===========================================

#Membuat variabel global
# nama = "Larry"
# prodi = "Informatika"
#Membuat variabel lokal
# def data1():
    
#     nama = "Alfi"
#     prodi = "Kedokteran Lanjut"

#     print("Nama:", nama)
#     print("Prodi:", prodi)

# def data2():
    
#     nama = "Alfi"
#     prodi = "Kedokteran Lanjut"

#     print("Nama:", nama)
#     print("Prodi:", prodi)

# data2()

# ========================================
#fungsi rekursif
# def sapa():
#     print("Hallo Ridho")
#     sapa()


# sapa()

# =======================================
# def faktorial(n):
# 	#Base Case: Kondisi fungsi berhenti
# 	if n == 0 or n == 1:
# 		return 1
# 	#Rekursive Case: Fungsi memanggil dirinya sendiri
# 	else:
# 		return n * faktorial(n - 1)
# #Memanggil fungsi
# hasil_faktorial = faktorial(4)
# print(f"Hasil dari 4! {hasil_faktorial}")

# ==============================================

#Fungsi untuk mengedit data
# buku = []

# def lihat_buku():
# 	for indeks, judul in enumerate(buku):
# 		print(f"{indeks}. {judul}")

# def edit_buku():
# 	lihat_buku()
# 	indeks = int(input("Masukkan ID Buku: "))
# 	if indeks < 0 or indeks >= len(buku):
# 		print("ID tidak valid")
# 	else:
# 		buku_baru = input("Judul baru: ")
# 		buku[indeks] = buku_baru
# 		print("Buku berhasil diupdate!")

# ===============================================

# try
# SyntaxError: expected ':'
# except jenisError:
# kode yang dijalankan error

# try:
#     umur = int(input('masukan angka : '))
#     print(umur)#input 'cinta APD'
# except ValueError:
#     print("variabel umur harus berupa angka")
# else:
#     print(f'angka yang kamu input : {umur}')

# ======================================================

# # finally
# try:
#     umur = int(input('masukan angka : '))
#     print(umur)#input 'cinta APD'
# except ValueError:
#     print("variabel umur harus berupa angka")
# else:
#     print(f'angka yang kamu input : {umur}')
# finally:
#     print('blok try selesai')

# ============================================================

# raise
# try:
# 	usn = input('Username yang diinginkan : ')
# 	if len(usn) < 5:
# 		raise ValueError('Nama Minimal Memiliki 5 karakter')
# except ValueError as error:
# 	print(error)