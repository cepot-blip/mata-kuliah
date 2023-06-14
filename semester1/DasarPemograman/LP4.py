#    Mohamad Prihartono
#    12220015
#    Teknik Informatika
#    Universitas Nusa Mandiri Margonda
#    Thurtday, 03 September 2022
#    Latihan Pertemuan 4

print("=====================================")
print("Pendaftaran Mahasiswa Baru")
print("=====================================")

# Input Data
nis = int(input("Masukkan NIS : "))
nama = input("Masukkan Nama Mahasiswa: ")
jurusan = input("Masukkan Jurusan [ TI/SI/Management/DataScience ] : ")

print("=====================================")
print("Data biaya pendaftaran")
print("=====================================")
print("Biaya Pendaftaran TI : Rp. 50.000.000")
print("Biaya Pendaftaran SI : Rp. 40.000.000")
print("Biaya Pendaftaran Management : Rp. 30.000.000")
print("Biaya Pendaftaran DataScience : Rp. 20.000.000")
print("=====================================")

#   Input Data
if jurusan == "TI":
    print("Biaya Pendaftaran Anda : Rp. 50.000.000")
    harga = 50000000
elif jurusan == "SI":
    print("Biaya Pendaftaran Anda : Rp. 40.000.000")
    harga = 40000000
elif jurusan == "Management":
    print("Biaya Pendaftaran Anda : Rp. 30.000.000")
    harga = 30000000
elif jurusan == "DataScience":
    print("Biaya Pendaftaran Anda : Rp. 20.000.000")
    harga = 20000000
else:
    print("Jurusan yang anda masukkan salah")
    harga = 0

print("=====================================")
print("Data Mahasiswa")

#   Output Data
if jurusan == "TI":
    jurusan = "Teknik Informatika"
elif jurusan == "SI":
    jurusan = "Sistem Informasi"
elif jurusan == "Management":
    jurusan = "Management"
elif jurusan == "DataScience":
    jurusan = "DataScience"
else:
    jurusan = "Jurusan tidak ada"

#   Output Data
print("=====================================")
print("NIS : ", nis)
print("Nama : ", nama)
print("Jurusan : ", jurusan)
print("Biaya Pendaftaran : Rp. ", harga)
print("=====================================")

