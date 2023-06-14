

#   Pengulangan input data menggunakan for i 
ulangan = 2
print("=====================================")
print("Pengulangan input data menggunakan for i")
print("=====================================")
for  i in range (ulangan):
    print("Masukkan data ke-", i+1)
    nim = input("Masukkan NIM : ")
    uts = int(input("Masukkan Nilai UTS : "))
    uas = int(input("Masukkan Nilai UAS : "))
    print("Nim anda adalah       :", nim)
    print("Nilai uts anda adalah :", uts)
    print("Nilai uas anda adalah :", uas)
    print("-----------------------------------\n")


#   Pengulangan input data menggunakan while
ulangan = int(input("Masukan Data yang ingin di input : "))
i = 0
print("=====================================")
print("Pengulangan input data menggunakan while")
print("=====================================")
while i < ulangan:
    print("Masukkan data ke-", i+1)
    nim = input("Masukkan NIM           : ")
    uts = int(input("Masukkan Nilai UTS : "))
    uas = int(input("Masukkan Nilai UAS : "))
    print("Nim anda adalah       :", nim)
    print("Nilai uts anda adalah :", uts)
    print("Nilai uas anda adalah :", uas)
    print("-----------------------------------\n")
    i += 1


