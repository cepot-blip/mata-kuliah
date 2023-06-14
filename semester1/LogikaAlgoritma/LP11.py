# TEKNIK PENCARIAN TUNGGAL

# def linear_search(list, target):
#     posisi=[]

#     for i in range (len(list)):
#         if target == list[i]:
#             posisi.append(i+1)
    
#     if len(posisi)>0:
#         print("List", target, "Sebanyak", len(posisi), "ditemukan pada posisi :", posisi)
#     else:
#         print("List", target, "tidak ditemukan")

# list = [1, 4, 5, 6, 8, 4, 9]
# print("List :", list)
# target = int(input("Masukkan angka yang dicari : "))
# linear_search(list, target)


# TEKNIK PENCARIAN BINARY
# def binary_serch (list, target):
#     first = 0
#     last = len(list)-1
#     found = False
#     posisi = []

#     while first <= last and not found:
#         midpoint = (first + last)//2
#         if list[midpoint] == target:
#             found = True
#             posisi.append(midpoint+1)
#         elif target < list[midpoint]:
#             last = midpoint-1
#         else:
#             first = midpoint+1

#     if found:
#         print("List not found!")


# list = [1, 2, 4, 7, 10, 14, 23, 35, 47]
# target = int(input("Masukkan angka yang dicari : "))
# binary_serch(list, target)


# TEKNIK PENCARIAN STRAIT MAX MIN
def strait_max_min(a, n):
    max = a[0]
    min = a[0]
    for i in range(1, n):
        if a[i] > max:
            max = a[i]
        else:
            p=p+1
            print("Proses ke :", p)
            if a[i] < min:
                min = a[i]
                print("=====================================")
                print("Nilai Max :", max)
