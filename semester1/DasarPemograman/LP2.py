print("=====================================")
print("Selamat Datang di Program Sederhana")
print("Universitas Nusa Mandiri Margonda")


print("=====================================")
print("Nama             \t: Mohamad Prihartono")
print("NIM              \t: 12220015")
print("Jurusan          \t: Teknik Informatika")
print("Latihan Pertemuan\t: 2")

#       Menu Program Sederhana
print("=====================================")
print("Silahkan Pilih Menu")
print("=====================================")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("=====================================")

#       Input menu dari user
pilihan = int(input("Masukkan Pilihan Anda : "))


#       Penjumlahan dasar
if pilihan == 1:
            print("=====================================")
            print("Anda Memilih Penjumlahan")
            print("=====================================")
            a = int(input("Masukkan Bilangan Pertama : "))
            b = int(input("Masukkan Bilangan Kedua : "))
            print("Hasil Penjumlahan dari", a, "+", b, "adalah =", a+b)

#       Pengurangan dasar
elif pilihan == 2:
            print("=====================================")
            print("Anda Memilih Pengurangan")
            print("=====================================")
            a = int(input("Masukkan Bilangan Pertama : "))
            b = int(input("Masukkan Bilangan Kedua : "))
            print("Hasil Pengurangan dari", a, "-", b, "adalah = ", a-b)

#       Perkalian dasar
elif pilihan == 3:
            print("=====================================")
            print("Anda Memilih Perkalian")
            print("=====================================")
            a = int(input("Masukkan Bilangan Pertama : "))
            b = int(input("Masukkan Bilangan Kedua : "))
            print("Hasil Perkalian dari", a, "*", b, "adalah =", a*b)

#       Pembagian dasar
elif pilihan == 4:
            print("=====================================")
            print("Anda Memilih Pembagian")
            print("=====================================")
            a = int(input("Masukkan Bilangan Pertama : "))
            b = int(input("Masukkan Bilangan Kedua : "))
            print("Hasil Pembagian dari", a, "/", b, "adalah =", a/b)

#       Jika pilihan tidak ada
else:
    print("=======================================================================")
    print("Pilihan Anda Tidak Tersedia Silahkan masukan angka sesuai yang tersedia")
    print("=======================================================================")

print("=============================================")
print("Terima Kasih Telah Menggunakan Program Ini :)")
print("=============================================")


#    Mohamad Prihartono
#    12220015
#    Teknik Informatika
#    Universitas Nusa Mandiri Margonda
#    2022