
#       OUTPUT PERTAMA MENGGUNAKAN PERULANGAN WHILE
z=0  #  DEKLARASI VARIALBE Z
while z >= 0: #     PERULANGAN INFINITE
    z=int(input("Masukkan Jumlah Anak : ")) #   INPUT JUMLAH ANAK
    if z< 1 or z > 100: #   JUMLAH ANAK HARUS 1-100
        print("Jumlah Yang Anda Masukkan")
        continue #  KEMBALI KE AWAL PERULANGAN
    else : #    JIKA JUMLAH ANAK 1-100
        print("\t   ====================================================")
        print("\t               Tek kotek kotek kotek..")
        print("\t   ----------------------------------------------------")
        while z>1: #    PERULANGAN JUMLAH ANAK
            print("\t  | Anak Ayam Turunlah",z,"Mati Satu Tinggalah ",z-1, "|") #  OUTPUT
            z=z-1 #     DEKRIMEN JUMLAH ANAK
        if z==1:
            print("\t  | Anak Ayam Turunlah",z,"Mati Satu Tinggalah Biyangnya.")  #    OUTPUT
            print("\t   ====================================================")
            break #     KELUAR DARI PERULANGAN


#       OUTPUT KEDUA MENGGUNAKAN PERULANGAN FOR
z=0     #  DEKLARASI VARIALBE Z
for z in  range(0,100): #      PERULANGAN INFINITE
    z=int(input("Masukkan Jumlah Anak : ")) #   INPUT JUMLAH ANAK
    if z < 1 or z >100: #   JUMLAH ANAK HARUS 1-100
        print("\tJumlah Yang Anda Masukkan") #   OUTPUT
        continue #  KEMBALI KE AWAL PERULANGAN
    else : #    JIKA JUMLAH ANAK 1-100
        print("\t   ====================================================")
        print("\t               Tek kotek kotek kotek..")
        print("\t   ----------------------------------------------------")
        while z>1: #    PERULANGAN JUMLAH ANAK
            print("\t  | Anak Ayam Turunlah",z,"Mati Satu Tinggalah",z-1,"|") #  OUTPUT
            z=z-1 #     DEKRIMEN JUMLAH ANAK
        if z==1:
            print("\t  | Anak Ayam Turunlah",z,"Mati Satu Tinggal Biyangnya.") #    OUTPUT
            print("\t   ====================================================")
            break #     KELUAR DARI PERULANGAN

