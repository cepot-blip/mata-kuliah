
# print("Universitas Nusa Mandiri Margonda")
# print("Data Mahasiswa")
# print("=====================================")
# print("Nama\t: Jhony dev")
# print("NIM\t: 201910370311000")
# print("Jurusan\t: Teknik Informatika")
# print("=====================================")
# print("Nilai Uts\t: 80")
# print("Nilai Uas\t: 90")
# print("Nilai Tugas\t: 100")
# print("Rata-rata\t:", (80+90+100)/3)
# print("=====================================")
# print("Keterangan\t: Lulus(Bersyarat)")
# print("=====================================")


# count = 0

# while(count < 8):
#     print(count, "is less than 8")
#     count = count + 1
# else:
#     print(count, "is not less than 8")


# bilangan = 0 
# pilihan = "Yes"


# while (pilihan == "Yes" or pilihan == "yes"):
#     bilangan = int(input("Masukkan Bilangan : "))
#     if bilangan % 2 == 0:
#         print("Bilangan Genap")
#     else:
#         print("Bilangan Ganjil")
#     pilihan = input("Apakah Anda Ingin Mengulang ? (Yes/No) : ")
#     if (pilihan == "No" or pilihan == "no"):
#         print("Terima Kasih")
#         break
#     else:
#         continue
# x=0
# while x<9:
#     print(x)
#     x+=1


import pandas as pd

listNim =[]
listNama =[]
listNilaiUts =[]
listNilaiUas =[]
listTotal =[]

ulang = 3
for i in range(ulang):
    print("Data ke - ", i+1)
    listNim.append(input("Masukkan NIM : "))
    listNama.append(input("Masukkan Nama : "))
    listNilaiUts.append(input("Masukkan Nilai UTS : "))
    listNilaiUas.append(input("Masukkan Nilai UAS : "))
    listTotal.append((int(listNilaiUts[i])+int(listNilaiUas[i]))/2)


data = {
    'NIM' : listNim,
    'Nama' : listNama,
    'Nilai UTS' : listNilaiUts,
    'Nilai UAS' : listNilaiUas,
    'Total' : listTotal,
    'Rata-rata' : listTotal
}

df = pd.DataFrame(data)

print('===============  DAFTRA NILAI MAHASISWA  ===============')
print(df)
print('=======================================================')