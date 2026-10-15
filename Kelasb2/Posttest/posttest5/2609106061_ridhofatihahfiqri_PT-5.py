#Sistem manajemen state & resource
Judul = "Clash of Clan Multiuser" #biar kelihatan keren aja sebenarnya buat namanya gini 

#data pemain
# [username , password, gold, elixir, gems, trophy, layout]

akun = [
    ["ridho", "123", 1000, 5000, 100, 1200, "Desa Utama"],
    ["miku", "456", 2000, 4000, 150, 1500, "Desa Perang"]
]

#data bangunan : [username, nama, level]
bangunan = [
    ["ridho", "Cannon", 2],
    ["ridho", "Gold Mine", 3],
    ["miku", "Archer Tower", 2]
]

#data pasukan: [username, nama, jumlah, level]
pasukan = [
    ["ridho", "Barbarian", 10, 1],
    ["miku", "Archer", 20, 2]
]

#data clan: [nama clan, pemimpin, anggota]
clan = [
    ["Warrior", "ridho", ["ridho", "miku"]]
]

#data objek desa: [username, nama objek]
objek_desa = [
    ["ridho", "Pohon"],
    ["ridho", "Batu"],
    ["miku", "Pohon"]
]

#data chat: [username, pesan]
riwayat_chat = [
    ["ridho", "Halo semua"],
    ["miku", "Siap menyerang"]
]

while True:
    print()
    print("1. Login")
    print("2. Buat akun")
    print("3. Papan skor")
    print("4. Keluar")

    menu = input("Pilih menu: ")

    if menu == "1":
        username = input("Username: ")
        password = input("Password: ")

        pemain = None

        for data in akun:
            if data[0] == username and data[1] == password:
                pemain = data
                break

        if pemain == None:
            print("Login gagal")
            continue

        print("Selamat datang,", pemain[0])

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

            aksi = input("Pilih menu: ")

            # Read: Profil Dan Inventori
            if aksi == "1":
                print()
                print("Username:", pemain[0])
                print("Gold:", pemain[2])
                print("Elixir:", pemain[3])
                print("Gems:", pemain[4])
                print("Trophy:", pemain[5])
                print("Layout:", pemain[6])

                print()
                print("Bangunan:")
                for data in bangunan:
                    if data[0] == pemain[0]:
                        print(data[1], "- Level", data[2])

                print()
                print("Pasukan:")
                for data in pasukan:
                    if data[0] == pemain[0]:
                        print(data[1], "- Jumlah:", data[2],
                              "- Level:", data[3])

            # Create: Bangunan
            elif aksi == "2":
                nama = input("pilih Canon, Gold Mine, Archer Tower: ")
                bangunan.append([pemain[0], nama, 1])
                print("Bangunan berhasil dibuat")

            # Create: Pasukan
            elif aksi == "3":
                print("Barbarian, Archer")
                nama = input("Nama pasukan: ")
                jumlah = int(input("Jumlah pasukan: "))
                pasukan.append([pemain[0], nama, jumlah, 1])
                print("Pasukan berhasil dilatih")

            # Update: Upgrade Bangunan
            elif aksi == "4":
                daftar = []

                for data in bangunan:
                    if data[0] == pemain[0]:
                        daftar.append(data)

                for i in range(len(daftar)):
                    print(i + 1, daftar[i][1],
                          "- Level", daftar[i][2])

                nomor = int(input("Tekan nomor untuk upgrade bangunan yang tersedia: "))

                if 1 <= nomor <= len(daftar):
                    daftar[nomor - 1][2] += 1
                    print("Bangunan berhasil diupgrade")
                else:
                    print("Bangunan tidak ditemukan.")

            # Update: Upgrade Pasukan
            elif aksi == "5":
                daftar = []

                for data in pasukan:
                    if data[0] == pemain[0]:
                        daftar.append(data)

                for i in range(len(daftar)):
                    print(i + 1, daftar[i][1],
                          "- Level", daftar[i][3])

                nomor = int(input("Nomor pasukan: "))

                if 1 <= nomor <= len(daftar):
                    daftar[nomor - 1][3] += 1
                    print("Pasukan berhasil diupgrade")
                else:
                    print("Pasukan tidak ditemukan.")

            # Update: Resource
            elif aksi == "6":
                print("1. Gold")
                print("2. Elixir")
                print("3. Gems")

                resource = input("Pilih resource: ")
                perubahan = int(input("Masukan nilai resource yang diubah: "))

                if resource == "1":
                    pemain[2] = max(0, pemain[2] + perubahan)
                elif resource == "2":
                    pemain[3] = max(0, pemain[3] + perubahan)
                elif resource == "3":
                    pemain[4] = max(0, pemain[4] + perubahan)
                else:
                    print("Resource tidak valid.")
                    continue

                print("Resource berhasil diperbarui")

            # Update: Trophy
            elif aksi == "7":
                perubahan = int(input("Masukan nilai trophy: "))
                pemain[5] = max(0, pemain[5] + perubahan)
                print("Trophy berhasil diperbarui")

            # Update: Layout
            elif aksi == "8":
                pemain[6] = input("Nama layout baru: ")
                print("Layout berhasil diubah")

            # Delete: Pohon/batu
            elif aksi == "9":
                daftar = []

                for data in objek_desa:
                    if data[0] == pemain[0]:
                        daftar.append(data)

                for i in range(len(daftar)):
                    print(i + 1, daftar[i][1])

                nomor = int(input("pilih Nomor pohon/batu: "))

                if 1 <= nomor <= len(daftar):
                    objek_desa.remove(daftar[nomor - 1])
                    print("Objek berhasil dihilangkan")
                else:
                    print("Objek tidak ditemukan.")

            # Create: Clan
            elif aksi == "10":
                nama = input("Nama clan: ")
                sudah_punya = False

                for data in clan:
                    if pemain[0] in data[2]:
                        sudah_punya = True

                if sudah_punya:
                    print("Kamu sudah memiliki clan.")
                else:
                    clan.append([nama, pemain[0], [pemain[0]]])
                    print("Clan berhasil dibuat")

            # Read: Clan
            elif aksi == "11":
                for data in clan:
                    print()
                    print("Clan:", data[0])
                    print("Pemimpin:", data[1])
                    print("Anggota:", data[2])

            # Delete: Bubarkan Clan
            elif aksi == "12":
                for i in range(len(clan)):
                    print(i + 1, clan[i][0],
                          "- Pemimpin:", clan[i][1])

                nomor = int(input("Nomor clan: "))

                if 1 <= nomor <= len(clan):
                    if clan[nomor - 1][1] == pemain[0]:
                        clan.pop(nomor - 1)
                        print("Clan berhasil dibubarkan")
                    else:
                        print("Hanya pemimpin yang dapat membubarkan clan.")
                else:
                    print("Clan tidak ditemukan.")

            # CREATE: Chat clan
            elif aksi == "13":
                pesan = input("Pesan: ")
                riwayat_chat.append([pemain[0], pesan])

                print()
                print("Riwayat chat")
                for data in riwayat_chat:
                    print(data[0] + ":", data[1])

            # DELETE: Riwayat chat
            elif aksi == "14":
                riwayat_chat.clear()
                print("Riwayat chat berhasil dihapus")

            # Logout
            elif aksi == "15":
                print("Logout berhasil.")
                break

            else:
                print("Pilihan tidak valid.")

    # Create: Akun baru
    elif menu == "2":
        username = input("Username baru: ")
        sudah_ada = False

        for data in akun:
            if data[0] == username:
                sudah_ada = True

        if sudah_ada:
            print("Username sudah digunakan")
        else:
            password = input("Password baru: ")
            akun.append([
                username, password, 1000, 1000, 50, 0, "Desa Utama"
            ])
            print("Akun berhasil dibuat")

    # Read: Papan leaderboard
    elif menu == "3":
        papan_skor = []

        for data in akun:
            papan_skor.append([data[0], data[5]])

        papan_skor.sort(key=lambda data: data[1], reverse=True)

        print()
        print("Papan leaderboard")
        for i in range(len(papan_skor)):
            print(i + 1, papan_skor[i][0],
                  "-", papan_skor[i][1], "Trophy")

    elif menu == "4":
        print("Close the game")
        break

    else:
        print("Pilihan tidak valid.")