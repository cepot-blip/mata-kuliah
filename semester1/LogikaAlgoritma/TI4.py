print("=========================================")
print("Menentukan Grade Kelulusan Mahasiswa")
print("=========================================")

# Input
nim = int(input("Masukkan NIM Mahasiswa: "))
nama = input("Masukkan Nama Mahasiswa: ")
uts = int(input("Masukkan Nilai UTS Mahasiswa: "))
uas = int(input("Masukkan Nilai UAS Mahasiswa: "))
tugas = int(input("Masukkan Nilai Tugas Mahasiswa: "))
absensi = int(input("Masukkan Nilai Absensi Mahasiswa: "))
matakuliah = input("Masukkan Mata Kuliah: ")

# Proses
nilai_akhir = (uts * 0.25) + (uas * 0.30) + (tugas * 0.25) + (absensi * 0.2)

if nilai_akhir >= 80:
    grade = "A"
elif nilai_akhir >= 70:
    grade = "B"
elif nilai_akhir >= 60:
    grade = "C"
elif nilai_akhir >= 50:
    grade = "D"
else:
    grade = "E"

# Output
print("=========================================")
print("NIM Mahasiswa: ", nim)
print("Nama Mahasiswa: ", nama)
print("Nilai UTS Mahasiswa: ", uts)
print("Nilai UAS Mahasiswa: ", uas)
print("Nilai Tugas Mahasiswa: ", tugas)
print("Nilai Absensi Mahasiswa: ", absensi)
print("Mata Kuliah: ", matakuliah)
print("Nilai Akhir: ", nilai_akhir)
print("Grade: ", grade)
print("=========================================")
