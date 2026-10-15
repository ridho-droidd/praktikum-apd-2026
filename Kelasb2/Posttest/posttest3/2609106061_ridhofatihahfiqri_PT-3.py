username = input("Masukkan username: ").lower().strip()
password = input("Masukkan password: ").lower().strip()

if username == "ridhofatihahfiqri":
    if password == "61":
        print("Login berhasil")
        print("1.misi standard (bonus 2%), 2.sulit (bonus 5%), 3.kritis (bonus 8%), 4.penyelematan bumi (bonus 12%):")
        Pemilihan_misi = input("Masukkan level misi (1-4): ").lower().strip()

        if Pemilihan_misi == "1":
            reward = 1000
            bonus = 0.02
            reward_total = reward + (reward * bonus)
            print("Reward total:", reward_total)
        elif Pemilihan_misi == "2":
            reward = 1000
            bonus = 0.05
            reward_total = reward + (reward * bonus)
            print("Reward total:", reward_total)
        elif Pemilihan_misi == "3":
            reward = 1000
            bonus = 0.08
            reward_total = reward + (reward * bonus)
            print("Reward total:", reward_total)
        elif Pemilihan_misi == "4":
            reward = 1000
            bonus = 0.12
            reward_total = reward + (reward * bonus)
            print("Reward total:", reward_total)
        else:
            print("Pilihan level misi tidak valid. Silakan pilih level misi yang tersedia.")
    else:
        print("Password salah. Silakan coba lagi.")
else:
    print("Username tidak ditemukan. Silakan coba lagi.")

