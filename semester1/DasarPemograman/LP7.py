# BUAT KALKULATOR OTOMATIS

# Import library
import os


match = 0
while match == 0:
    print("Kalkulator Sederhana")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Exit")
    print("Pilih menu 1-5: ")
    menu = int(input())

def penjumlahan():
    print("Penjumlahan")
    print("Masukkan angka pertama: ")
    a = int(input())
    print("Masukkan angka kedua: ")
    b = int(input())
    print("Hasilnya adalah: ", a+b)

def pengurangan():
    print("Pengurangan")
    print("Masukkan angka pertama: ")
    a = int(input())
    print("Masukkan angka kedua: ")
    b = int(input())
    print("Hasilnya adalah: ", a-b)

def perkalian():
    print("Perkalian")
    print("Masukkan angka pertama: ")
    a = int(input())
    print("Masukkan angka kedua: ")
    b = int(input())
    print("Hasilnya adalah: ", a*b)

def pembagian():
    print("Pembagian")
    print("Masukkan angka pertama: ")
    a = int(input())
    print("Masukkan angka kedua: ")
    b = int(input())
    print("Hasilnya adalah: ", a/b)

def keluar():
    print("Keluar")
    print("Terima kasih sudah menggunakan kalkulator ini")

if menu == 1:
    penjumlahan()
elif menu == 2:
    pengurangan()
elif menu == 3:
    perkalian()
elif menu == 4:
    pembagian()
elif menu == 5:
    keluar()
    match = 1
