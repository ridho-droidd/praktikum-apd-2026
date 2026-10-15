skincare_1 = 35000
skincare_2 = 42000
skincare_3 = 50000
skincare_4 = 55000
skincare_5 = 68000
skincare_6 = 70000
ongkos_kirim = 12000
total_pengeluaran = skincare_1 + skincare_2 + skincare_3 + skincare_4 + skincare_5 + skincare_6 + ongkos_kirim
print (total_pengeluaran)

banyak_data = [skincare_1, skincare_2, skincare_3, skincare_4, skincare_5, skincare_6, ongkos_kirim]
rata_rata = total_pengeluaran/len(banyak_data)
print("rata-rata nilai",rata_rata)

nim = 61
boelan = nim < rata_rata
print ("total_pengeluaran:", total_pengeluaran)
print ("rata_rata:", rata_rata)
print ("nim:", nim)
print ("boelan:", boelan)

harga_skincare = [skincare_1, skincare_2, skincare_3, skincare_4, skincare_5, skincare_6]
total_jpy = total_pengeluaran * 0.009
print ("total_jpy:", total_jpy)
print (harga_skincare[3:])
