#   Mohamad Prihartono
#   12220015
#   Teknik Informatika
#   Latihan Individu Pertemuan 3 Soal 2
#   Logika Dan Algoritma
#   2022/09/29


print("=====================================")
print("Program Menghitung Jumlah Bilangan")
print("=====================================")

a = int(input("Masukkan Bilangan Pertama : "))
b = int(input("Masukkan Bilangan Kedua   : "))
c = int(input("Masukkan Bilangan Ketiga  : "))
d = int(input("Masukkan Bilangan Keempat : "))


print("=====================================")
print("Manakah Bilangan Terbesar ?")
print("=====================================")
if a > b and a > c and a > d:
    print("Bilangan Terbesar Adalah : ", a)
elif b > a and b > c and b > d:
    print("Bilangan Terbesar Adalah : ", b)
elif c > a and c > b and c > d:
    print("Bilangan Terbesar Adalah : ", c)
elif d > a and d > b and d > c:
    print("Bilangan Terbesar Adalah : ", d)
else:
    print("Bilangan Tidak Boleh Sama")