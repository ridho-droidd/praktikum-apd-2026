# Materi Pertemuan 4 di bawah ini --->

game = ["Genshin", 7.0, True]#game adalah list yang berisi string, float, dan boolean
for i in game: #for loop akan berjalan sebanyak jumlah elemen dalam list game
    print(i)

for i in range(1, 3):# Mengontrol baris dalam tabel perkalian
    for j in range(1, 4):# Mengontrol kolom dalam tabel perkalian
        print(f'{i} x {j} = {i * j}')
    print('') #biar ada jarak tiap iterasi

for i in range(1, 4):
    print("1 = ", i)

jawab = "ya"
hitung = 0

while jawab == "ya":#while loop akan terus berjalan selama jawab = "ya"
    hitung += 1#hitung akan bertambah 1 setiap kali perulangan
    jawab = input("Ulang lagi tidak? ")#jawab akan diisi input dari user, jika jawab = "ya" maka perulangan akan terus berjalan, jika jawab = "tidak" maka perulangan akan berhenti

print(f"Total Perulangan : {hitung}")#print total perulangan yang dilakukan

for i in range(10):#for loop akan berjalan sebanyak 10 kali
    if i == 5:#jika i = 5 maka perulangan akan berhenti
        break#break akan menghentikan perulangan
    print(i)

angka_benar = 7

while True:#while loop akan terus berjalan selama kondisi True
    print("== game tebak angka ==")

    angka_input = int(input("Masukkan angka (1-10): "))#angka_input akan diisi input dari user

    if not angka_input.digit():#jika angka_input bukan digit maka perulangan akan dilanjutkan ke iterasi berikutnya
        print("Input harus berupa angka")
        continue#continue akan melanjutkan perulangan ke iterasi berikutnya

    if angka_benar == angka_input:#jika angka_benar = angka_input maka perulangan akan berhenti
       print("angka yang anda masukkan benar")
       break
    else:
        print("angka anda masih salah")

for i in range(10):#for loop akan berjalan sebanyak 10 kali
    if i % 2 == 0:#jika i habis dibagi 2 maka perulangan akan dilanjutkan ke iterasi berikutnya
        continue#continue akan melanjutkan perulangan ke iterasi berikutnya
    print(i)

uang_awal = int(input("Masukkan jumlah uang awal: "))#uang_awal akan diisi input dari user

while uang_awal > 0:
    uang_pengeluaran = int(input("Masukkan jumlah uang yang dikeluarkan: "))
    uang_awal -= uang_pengeluaran
    print(f"Sisa uang: {uang_awal}")

print("Miskin, uang habis")