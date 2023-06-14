

print("=========================================")
print("Penggajian Pegawai")
print("=========================================")


# Input
gaji_pokok = int(input("Masukkan Gaji Pokok: "))
jam_kerja = int(input("Masukkan Jumlah Jam Kerja: "))

# Proses
tunjangan = (20/100) * gaji_pokok
if jam_kerja > 200:
    lembur = (jam_kerja - 200) * 2000
else:
    lembur = 0

pajak = (10/100) * (gaji_pokok + tunjangan + lembur)

gaji_bersih = gaji_pokok + tunjangan + lembur - pajak


# Output
print("=========================================")
print("Gaji Pokok: ", gaji_pokok)
print("Jumlah Jam Kerja: ", jam_kerja)
print("Gaji Lembur: ", lembur)
print("Gaji Total: ", gaji_bersih)
print("=========================================")
