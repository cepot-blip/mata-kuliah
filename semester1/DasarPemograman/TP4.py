#    Mohamad Prihartono
#    12220015
#    Teknik Informatika
#    Universitas Nusa Mandiri Margonda
#    Thurtday, 03 September 2022
#    Tugas Pertemuan 4


print("=====================================================")
print("\tTunjangan Gaji PT. DINGIN DAMAI")
print("=====================================================")

# Input Data
nama_karyawan    = input("\tMasukkan Nama Karyawan : ")
golongan_jabatan = input("\tMasukkan Golongan Jabatan [ 1/2/3 ] : ")
pendidikan       = input("\tMasukkan Pendidikan [ SMA/D3/S1/S2 ] : ")
jumlah_jam_kerja = int(input("\tMasukkan Jumlah Jam Kerja : "))
gaji_pokok = 300000

#   Input Data
if golongan_jabatan == "1":
    gaji_pokok = gaji_pokok * 0.05
elif golongan_jabatan == "2":
    gaji_pokok = gaji_pokok * 0.1
elif golongan_jabatan == "3":
    gaji_pokok = gaji_pokok * 0.15
else:
    gaji_pokok = 0

#   Proses
print("=====================================================")
print("\t   Data Tunjangan Gaji dari")
print("=====================================================")
print("\tTunjangan Golongan 1 : Rp. 15.000")
print("\tTunjangan Golongan 2 : Rp. 30.000")
print("\tTunjangan Golongan 3 : Rp. 45.000")
print("=====================================================")

print("\t   Data Tunjangan Pendidikan")
print("=====================================================")
print("\tTunjangan Pendidikan SMA : Rp. 7.500")
print("\tTunjangan Pendidikan D3  : Rp. 15.000")
print("\tTunjangan Pendidikan S1  : Rp. 60.000")
print("\tTunjangan Pendidikan S2  : Rp. 90.000")
print("=====================================================")

#   Input Data
if pendidikan == "SMA" or pendidikan == "sma":
    tunjangan_pendidikan = gaji_pokok * 0.025
elif pendidikan == "D3" or pendidikan == "d3":
    tunjangan_pendidikan = gaji_pokok * 0.05
elif pendidikan == "S1" or pendidikan == "s1":
    tunjangan_pendidikan = gaji_pokok * 0.20
elif pendidikan == "S2" or pendidikan == "s2":
    tunjangan_pendidikan = gaji_pokok * 0.30
else:
    tunjangan_pendidikan = 0

#   Input Data
if golongan_jabatan == "1":
    tunjangan_jabatan = gaji_pokok * 0.05
elif golongan_jabatan == "2":
    tunjangan_jabatan = gaji_pokok * 0.1
elif golongan_jabatan == "3":
    tunjangan_jabatan = gaji_pokok * 0.15
else:
    tunjangan_jabatan = 0

#   Input Data
if jumlah_jam_kerja < 8:
    tunjangan_jam_kerja = + 3500
else:
    tunjangan_jam_kerja = 0


#   Output Data
print("\t   Data Tunjangan Gaji")
print("=====================================================")
print("\t   Nama Karyawan     \t: ", nama_karyawan)
print("\t   Golongan Jabatan  \t: ", golongan_jabatan)
print("\t   Pendidikan        \t: ", pendidikan)
print("\t   Honor Lembur      \t: ", jumlah_jam_kerja)
print("=====================================================")
print("\t   total Gaji        \t: ", gaji_pokok + tunjangan_pendidikan + tunjangan_jabatan + tunjangan_jam_kerja, "Rupiah")
print("=====================================================")

