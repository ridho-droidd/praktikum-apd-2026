#Login system
username = "ridhofatihahfiqri"
password = "2609106061"

maks_login = 3
login_terakhir = 0

while login_terakhir < maks_login:
    username_input = input("Masukkan username: ").lower().strip()
    password_input = input("Masukkan password: ").lower().strip()

    if username_input == username and password_input == password:
        print("Login berhasil")
        break
    else:
        print("Username atau password salah")
        login_terakhir += 1

    if login_terakhir == maks_login:
        print("Anda telah melebihi batas percobaan login")

while login_terakhir < maks_login:
    print ("silahkan pilih jenis paket:")
    print ("1. Paket Reguler, 1 porsi")
    print ("2. Paket anak, 1 porsi")
    print ("3. Paket keluarga, 4 porsi")
    print ("4. Keluar dari program")

    pilihan = input("Masukkan pilihan Anda (1-4): ")

    if pilihan == "4":
        print("Program selesai.")
        break
    elif pilihan == "1":
        jenis_paket = "Paket Reguler"
        porsi_per_paket = 1
    elif pilihan == "2":
        jenis_paket = "Paket anak"
        porsi_per_paket = 1
    elif pilihan == "3":
        jenis_paket = "Paket keluarga"
        porsi_per_paket = 4
    else:
        print("Pilihan tidak valid. Silakan pilih antara 1 hingga 4.")
        continue
    jumlah_paket = int(input("Masukkan jumlah paket yang ingin dipesan: "))

#menghitung total porsi menggunakan for
    total_porsi = 0
    for i in range(jumlah_paket):
        total_porsi = total_porsi + porsi_per_paket

#menentukan bonus
    if total_porsi >= 20:
        bonus = "5 Paket buah"
    elif total_porsi >= 10 and total_porsi < 20:
        bonus = "3 Paket susu"
    elif total_porsi >= 5 and total_porsi < 10:
        bonus = "1 Paket vitamin"
    else:
        bonus = "Tidak ada bonus"

#Jumlah penerima manfaat
    Penerima_manfaat = total_porsi 

#Menampilkan hasil
    print('')
    print(f"Jenis paket yang dipilih: {jenis_paket}")
    print(f"Jumlah paket yang dipesan: {jumlah_paket}")
    print(f"Total porsi yang diterima: {total_porsi}")
    print(f"Jumlah penerima manfaat: {Penerima_manfaat}")
    print(f"Bonus yang diterima: {bonus}")
    print('')
#keluar dari loop menampilkan hasil
    break