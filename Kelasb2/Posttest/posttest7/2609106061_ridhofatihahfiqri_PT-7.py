# Fungsi tanpa parameter mengembalikan judul program
def judul_program():
    return "==Clash Of Clans=="


# Fungsi tanpa parameter menampilkan menu utama dan mengembalikan pilihan
def menu_utama():
    print()
    print("==Pilihan Menu==")
    print()
    print("1. Login")
    print("2. Buat akun")
    print("3. Papan skor")
    print("4. Keluar")
    return input("Pilih menu: ").strip()


# Fungsi dengan parameter menangani input angka agar program tidak error
def input_angka(pesan):
    while True:
        try:
            angka = int(input(pesan))
            return angka
        except ValueError:
            print("Input harus berupa angka. Silakan coba lagi.")


# Fungsi dengan parameter dan rekursi menghitung total trophy semua akun
def hitung_trophy_rekursif(daftar_username, indeks=0):
    if indeks >= len(daftar_username):
        return 0

    username_data = daftar_username[indeks]

    if username_data in akun:
        trophy = akun[username_data]["trophy"]
    else:
        trophy = 0

    return trophy + hitung_trophy_rekursif(
        daftar_username, indeks + 1
    )

# Prosedur 1 menampilkan profil dan resource pemain
def tampilkan_profil(username, pemain):
    print()
    print("Username:", username)
    print("Gold:", pemain["gold"])
    print("Elixir:", pemain["elixir"])
    print("Gems:", pemain["gems"])
    print("Trophy:", pemain["trophy"])
    print("Layout:", pemain["layout"])


# Prosedur 2 menampilkan papan skor
def tampilkan_papan_skor():
    papan_skor = []
    for username_data in akun:
        trophy_data = akun[username_data]["trophy"]
        papan_skor.append([username_data, trophy_data])

    papan_skor.sort(key=lambda data: data[1], reverse=True)
    print()
    print("==Papan peringkat==")
    for i in range(len(papan_skor)):
        print(i + 1, papan_skor[i][0], "-", papan_skor[i][1], "Trophy")

    # Pemanggilan fungsi rekursif agar total trophy dapat dihitung.
    daftar_username = list(akun.keys())
    print("Total trophy semua akun:", hitung_trophy_rekursif(daftar_username))


# Judul program
Judul = "==Clash Of Clans==" 

# data pemain
akun = {
     "ridho": {
            "password": "123",
            "gold": 1000,
            "elixir": 5000,
            "gems": 100,
            "trophy": 1200,
            "layout": "Desa Utama"
        },
        "miku": {
            "password": "456",
            "gold": 2000,
            "elixir": 4000,
            "gems": 150,
            "trophy": 1500,
            "layout": "Desa Perang"
        }
}

# bangunan pemain
bangunan = {
    "ridho": [
        {"nama": "Cannon", "level": 2},
        {"nama": "Gold Mine", "level": 3}
    ],
    "miku": [
        {"nama": "Archer Tower", "level": 2}
    ]
}

# pasukan pemain
pasukan = {
    "ridho": [
        {"nama": "Barbarian", "jumlah": 10, "level": 1}
    ],
    "miku": [
        {"nama": "Archer", "jumlah": 20, "level": 2}
    ]
}

# Clan
clan = {
    "Warrior": {
        "pemimpin": "ridho",
        "anggota": ["ridho", "miku"]
    }
}

# Objek desa
objek_desa = {
    "ridho": ["Pohon", "Batu"],
    "miku": ["Pohon"]
}

# riwatat chat
riwayat_chat = {
    "ridho": ["Halo semua"],
    "miku": ["Siap menyerang"]
}


while True:
    print(judul_program())
    menu = menu_utama()

# Login
    if menu == "1":
        username = input("Username: ").strip()
        password = input("Password: ").strip()
#! ini berfungsi memeriksa apakah password atau username benar atau tidak dan juga memeriksa apakah akun tersebut sudah ada atau belum
        if username not in akun or akun[username]["password"] != password:
            print("Login gagal")
            continue

        pemain = akun[username]
        print("Selamat datang,", username)

# dictionary terkait
        bangunan.setdefault(username, [])
        pasukan.setdefault(username, [])
        objek_desa.setdefault(username, [])
        riwayat_chat.setdefault(username, [])

        while True:
            print()
            print("==MENU PEMAIN==")
            print("1. Profil dan inventori")
            print("2. Membangun bangunan")
            print("3. Melatih pasukan")
            print("4. Upgrade bangunan")
            print("5. Upgrade pasukan")
            print("6. Mengubah resource")
            print("7. Mengubah Trophy")
            print("8. Mengubah layout desa")
            print("9. Menghilangkan pohon/batu")
            print("10. Membuat clan")
            print("11. Melihat clan")
            print("12. Menghapus clan")
            print("13. Chat clan")
            print("14. Menghapus riwayat chat")
            print("15. Logout")

            aksi = input("Pilih menu: ").strip()

# Read
            if aksi == "1":
                tampilkan_profil(username, pemain)

                print("Bangunan:")

                if bangunan[username]:
                    for data in bangunan[username]:
                        print(data["nama"], "- Level", data["level"])
                else:
                    print("Belum ada bangunan.")

                print("Pasukan:")
                if pasukan[username]:
                    for data in pasukan[username]:
                        print(
                            data["nama"],
                            "- Jumlah:", data["jumlah"],
                            "- Level:", data["level"]
                        )
                else:
                    print("Belum ada pasukan.")

                print("Objek desa:", objek_desa[username])

#Create Bangunan
            elif aksi == "2":
                nama = input("Pilih Cannon, Gold Mine, Archer Tower: ").strip()
                if not nama:
                    print("Nama bangunan tidak boleh kosong.")
                    continue
                bangunan[username].append({"nama": nama, "level": 1})
                print("Bangunan berhasil dibuat.")

#Create Pasukan
            elif aksi == "3":
                print("Pilih pasukan: Barbarian, Archer")
                nama = input("Nama pasukan: ").strip()

                jumlah_input = input("Jumlah pasukan: ").strip()

                if jumlah_input.isdigit():
                    jumlah = int(jumlah_input)

                    if jumlah <= 0:
                        print("Jumlah pasukan harus lebih dari 0.")
                        continue
                else:
                    print("Jumlah harus berupa angka.")
                    continue

                pasukan[username].append({
                    "nama": nama,
                    "jumlah": jumlah,
                    "level": 1
                })

                print("Pasukan berhasil dilatih.")

# Update bangunan
            elif aksi == "4":
                daftar = bangunan[username]

                if not daftar:
                    print("Kamu belum memiliki bangunan.")
                    continue

                print("Daftar bangunan:")
                for data in daftar:
                    print(data["nama"], "- Level", data["level"])

                nomor = input("Masukkan nama bangunan yang ingin di-upgrade: ").strip()

                ditemukan = False

                for data in daftar:
                    if data["nama"].lower() == nomor.lower():
                        data["level"] += 1
                        print("Bangunan berhasil di-upgrade.")
                        ditemukan = True
                        break

                if not ditemukan:
                    print("Bangunan tidak ditemukan.")

# Update Pasukan
            elif aksi == "5":
                daftar = pasukan[username]

                if not daftar:
                    print("Kamu belum memiliki pasukan")
                    continue

                print("Daftar pasukan:")
                for data in daftar:
                    print(data["nama"], "- Level", data["level"])

                nama = input("Nama pasukan yang di upgrade cuy: ")

                ditemukan = False

                for data in daftar:
                    if data["nama"].lower() == nama.lower():
                        data["level"] += 1
                        print("Pasukan berhasil diupgrade.")
                        ditemukan = True
                        break

                if not ditemukan:
                    print("Pasukan yang mana nih?.")

#Update Resource
            elif aksi == "6":
                print("1. Gold")
                print("2. Elixir")
                print("3. Gems")
                pilihan = input("Pilih resource: ").strip()
                perubahan_resource = input_angka("Masukan nilai resource terbaru: ")

                if pilihan == "1":
                    pemain["gold"] = max(0, pemain["gold"] + perubahan_resource)
                elif pilihan == "2":
                    pemain["elixir"] = max(0, pemain["elixir"] + perubahan_resource)
                elif pilihan == "3":
                    pemain["gems"] = max(0, pemain["gems"] + perubahan_resource)
                else :
                    print("resource yang mana?")
                    continue

                print("Resource berhasil diperbarui")

#Update Trophy
            elif aksi == "7":
                perubahan = input_angka("Masukan nilai trophy: ")
                pemain["trophy"] = max(0, pemain["trophy"] + perubahan)
                print("Trophy berhasil diperbarui")

#Update Layout
            elif aksi == "8":
                pemain["layout"] = input("Nama layout baru: ")
                print("Layout berhasil diubah")

#Delete Objek
            elif aksi == "9":
                daftar = objek_desa[username]

                if not daftar:
                    print("Tidak ada pohon atau batu.")
                    continue

                for i in range(len(daftar)):
                    print(i + 1, daftar[i])

                nomor = input_angka("Pilih nomor pohon/batu: ")

                if 1 <= nomor <= len(daftar):
                    daftar.pop(nomor - 1)
                    print("Objek berhasil dihilangkan.")
                else:
                    print("Objek tidak ditemukan.")

#Create Clan
            elif aksi == "10":
                nama = input("Nama clan: ").strip()

                sudah_punya = False

                for data in clan.values():
                    if username in data["anggota"]:
                        sudah_punya = True

                if sudah_punya:
                    print("Kamu sudah memiliki clan.")
                elif nama in clan:
                    print("Nama clan sudah digunakan.")
                else:
                    clan[nama] = {
                        "pemimpin": username,
                        "anggota": [username]
                    }

                    print("Clan berhasil dibuat.")

#Read data clan
            elif aksi == "11":
                for nama in clan:
                    print()
                    print("Clan:", nama)
                    print("Pemimpin:", clan[nama]["pemimpin"])
                    print("Anggota:", clan[nama]["anggota"])

#Delete Clan
            elif aksi == "12":
                daftar = []

                for nama in clan:
                    daftar.append(nama)

                if not daftar:
                    print("kamu gak ada clan nih")
                    continue

                for i in range(len(daftar)):
                    print(i + 1, daftar[i],
                          "- Pemimpin:", clan[daftar[i]]["pemimpin"])

                nomor = input_angka("Nomor clan: ")

                if 1 <= nomor <= len(daftar):
                    nama = daftar[nomor - 1]

                    if clan[nama]["pemimpin"] == username:
                        clan.pop(nama)
                        print("Clan berhasil dibubarkan.")
                    else:
                        print("kamu bukan pemimpinnya")
                else:
                    print("clannya yang mana?")

#Create Chat Clan
            elif aksi == "13":
                pesan = input("Pesan: ")

                riwayat_chat[username].append (pesan)

                print()
                print("Riwayat chat")

                for nama in riwayat_chat:
                    for data in riwayat_chat[nama]:
                        print(nama + ":", data)

#Delete Riwayat Chat
            elif aksi == "14":
                riwayat_chat [username].clear()
                print("chat udah dibungkam")

#Logout
            elif aksi == "15":
                print("Logout berhasil.")
                break

            else:
                print("Pilihan tidak valid.")

#Create Akun Baru, pasti buat akun smurf
    elif menu == "2":
        username = input("Username baru: ").strip()
        sudah_ada = False

        for data in akun:
            if data == username:
                sudah_ada = True

        if sudah_ada:
            print("Username sudah digunakan.")
        else:
            password = input("Password baru: ")

            akun[username] = {
                "password": password,
                "gold": 1000,
                "elixir": 1000,
                "gems": 50,
                "trophy": 0,
                "layout": "Desa Utama"
            }

            print("Akun smurf udah dibuat.")

#Read Trophy Akun yang tersedia
    elif menu == "3":
        tampilkan_papan_skor()

#Close game
    elif menu == "4":
        print("Close the game")
        break

    else:
        print("Pilihan tidak valid.")