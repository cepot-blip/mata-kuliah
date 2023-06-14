# def menarahanoi(n,asal,tujuan,bantuan):
#     if n==1:
#         print("pindah disk 1 dari tiang",asal,"ke tiang",tujuan)
#         return
#     menarahanoi(n-1,asal,bantuan,tujuan)
#     print("pindah disk",n,"dari tiang",asal,"ke tiang",tujuan)
#     menarahanoi(n-1,bantuan,tujuan,asal)
# #drive code
# n=int(input("jumlah piringan : "))
# menarahanoi(n,'a','b','c')
# #jumlah cara
# print("Jumlah cara : ",(2**n)-1)
# #Rumus Menara Hanoi (2pangkatn - 1)
# # n=jumlah piringan


# nilai_tugas = [60, 70, 80, 90]
# print(nilai_tugas[0])
# print(nilai_tugas[1])
# print(nilai_tugas[2])
# print(nilai_tugas[3])

# nilai_tugas = [60, 70, 80, 90]
# print(nilai_tugas[-3])

# nilai_tugas = [60, 70, 80, 90]
# print("Nilai Element ke 2 dan 3 :", nilai_tugas[1:3])

# nilai_tugas = [60, 70, 80, 90]
# print(nilai_tugas[0:])

# nilai_tugas = [60, 70, 80, 90]
# print(nilai_tugas[len(nilai_tugas)-3:])

# nilai_tugas = [60, 70, 80, 90]
# nilai_tugas[0] = 65
# nilai_tugas[1] = 75
# nilai_tugas[2] = 85
# nilai_tugas[3] = 95
# print(nilai_tugas)


# nilai_tugas = [60, 70, 80, 90]
# nilai_tugas.pop(0)
# print(nilai_tugas[0:])

# nilai_tugas = [60, 70, 80, 90]
# nilai_tugas.remove(90)
# print(nilai_tugas[0:])


# penjualan=[[90, 100, 30, 45],[45, 27, 60], [20, 110, 45, 30], [98, 95, 75, 40]]

# for i in penjualan:
#     for j in i:
#         print(j, end=" ")
#     print()


# penjualan=[[90, 100, 30, 45],[45, 27, 60], [20, 110, 45, 30], [98, 95, 75, 40]]
# n = int(input("Masukkan jumlah baris : "))
# print()
# for i in range(n-1, -n, -1):
#     for j in range(abs(i), +1):
#         print("*", end=" ")
#     for j in range(n,abs(i), -1):
#         print("0", end=" ")        
#     print()

def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key


data = [9, 5, 1, 4, 3]
insertionSort(data)
print('Sorted Array in Ascending Order:')
print(data)


# Bubble sort in Python

def bubbleSort(array):
    
  # loop to access each array element
  for i in range(len(array)):

    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping elements if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)


# Quick sort in Python

# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array[i], array[j]) = (array[j], array[i])

  # swap the pivot element with the greater element specified by i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)