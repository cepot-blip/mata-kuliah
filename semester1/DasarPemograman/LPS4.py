#    Mohamad Prihartono
#    12220015
#    Teknik Informatika
#    Universitas Nusa Mandiri Margonda
#    Thurtday, 03 September 2022
#    Latihan Pertemuan 4

print("=====================================")
print("Penjualan Tiket Pesawat")
print("=====================================")

# Input Data
nama = input("Masukkan Nama Pembeli : ")
no_hp = input("Masukkan No HP : ")
tujuan = input("Masukkan Tujuan [ Jakarta/Surabaya/Medan ] : ")
kelas = input("Masukkan Kelas [ Ekonomi/Bisnis/First ] : ")
jumlah = int(input("Masukkan Jumlah Tiket : "))

print("=====================================")
print("Jumlah Tiket Pesawat")
print("=====================================")
print("Tiket Pesawat Jakarta : Rp. 1.000.000")
print("Tiket Pesawat Surabaya : Rp. 1.500.000")
print("Tiket Pesawat Medan : Rp. 2.000.000")
print("=====================================")
print("Tiket Pesawat Ekonomi : Rp. 1.000.000")
print("Tiket Pesawat Bisnis : Rp. 2.000.000")
print("Tiket Pesawat First : Rp. 3.000.000")
print("=====================================")

# Input Data
if tujuan == "Jakarta":
    harga = 1000000
elif tujuan == "Surabaya":
    harga = 1500000
elif tujuan == "Medan":
    harga = 2000000

# Input Data
if kelas == "Ekonomi":
    harga = 1000000
elif kelas == "Bisnis":
    harga = 2000000
elif kelas == "First":
    harga = 3000000

# Proses
total = harga * jumlah

# Proses potongan harga
if jumlah >= 5:
    potongan = total * 0.1
    total = total - potongan
    potongan = 0

# Output
print("=====================================")
print("Nama Pembeli : ", nama)
print("No HP : ", no_hp)
print("Tujuan : ", tujuan)
print("Kelas : ", kelas)
print("Jumlah Tiket : ", jumlah)
print("Total Harga : Rp. ", total)
print("=====================================")