print("======== TOKO MAINAN ANAK =========")
print("===================================")
print("List Kode Maianin")
print("===================================")
print("1. A001")
print("2. A002")
print("3. A003")
print("4. A004")
print("5. A005")
print("===================================")

# Input
nama = input("Masukkan nama pembeli : ")
kode_mainan = input("Masukkan kode mainan : ")
jumlah_beli = int(input("Masukkan jumlah beli : "))
harga = 0

# Proses
if kode_mainan == "A001":
    harga = 20000
elif kode_mainan == "A002":
    harga = 25000
elif kode_mainan == "A003":
    harga = 30000
elif kode_mainan == "A004":
    harga = 35000
elif kode_mainan == "A005":
    harga = 40000
else:
    print("Kode mainan tidak ada")

total_harga = harga * jumlah_beli



print("===================================")
print("Daftar Harga Mainan")
print("===================================")
print("1. Boneka Barbie Rp. 100.000")
print("2. Boneka Hello Kitty Rp. 80.000")
print("3. Boneka Doraemon Rp. 70.000")
print("4. Boneka Mickey Mouse Rp. 60.000")
print("5. Boneka Anak-anak Rp. 50.000")
print("===================================")
pilihan = int(input("Masukkan pilihan : "))
jumlah = int(input("Masukkan jumlah : "))
print("===================================")

# Proses
if pilihan == 1:
    harga = 100000
    total = harga * jumlah
    print("Total harga : Rp.", total)
elif pilihan == 2:
    harga = 80000
    total = harga * jumlah
    print("Total harga : Rp.", total)
elif pilihan == 3:
    harga = 70000
    total = harga * jumlah
    print("Total harga : Rp.", total)
elif pilihan == 4:
    harga = 60000
    total = harga * jumlah
    print("Total harga : Rp.", total)
elif pilihan == 5:
    harga = 50000
    total = harga * jumlah
    print("Total harga : Rp.", total)
else:
    print("Pilihan tidak tersedia")

# Output
print("===================================")
print("Nama Pembeli : ", nama)
print("Kode Mainan : ", kode_mainan)
print("Jumlah Beli : ", jumlah_beli)
print("Total Harga : Rp.", total)
print("===================================")

# Proses
if kode_mainan == "A001":
    harga = 100000
    total = harga * jumlah_beli
    print("Total harga : Rp.", total)
elif kode_mainan == "A002":
    harga = 80000
    total = harga * jumlah_beli
    print("Total harga : Rp.", total)
elif kode_mainan == "A003":
    harga = 70000
    total = harga * jumlah_beli
    print("Total harga : Rp.", total)
elif kode_mainan == "A004":
    harga = 60000
    total = harga * jumlah_beli
    print("Total harga : Rp.", total)
elif kode_mainan == "A005":
    harga = 50000
    total = harga * jumlah_beli
    print("Total harga : Rp.", total)
else:
    print("Kode mainan tidak tersedia")


