#       proses dan output secara berulang dengan memanfaatkan fungsi matriks/list
banyak_input = int(input("Masukkan banyaknya input: "))
list_nim = []
list_uts = []
list_uas = []
list_total = []
ulang = 0
rata = 0
for i in range(banyak_input):
    print("=====================================")
    print("Data ke - ", i+1)
    nim = input("Masukkan NIM: ")
    uts = int(input("Masukkan nilai UTS: "))
    uas = int(input("Masukkan nilai UAS: "))
    print("=====================================")
    total = uts + uas
    list_nim.append(nim)
    list_uts.append(uts)
    list_uas.append(uas)
    list_total.append(total)
    rata = rata + total
    if i == ulang:
        for j in range(ulang):
            print(list_nim[j], list_uts[j], list_uas[j], list_total[j])
        ulang = ulang + 1
print("NIM  \t\tUTS   \t\tUAS   \t\tTotal")
for j in range(banyak_input):
    print(list_nim[j], list_uts[j], list_uas[j], list_total[j])
print("Rata-rata nilai total adalah", rata/banyak_input)
print("=====================================")


