class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)

    def size(self):
        return len(self.items)


def display_data():
    print("+------------------------------------+")
    print("\t     Data Kelompok")
    print("+------------------------------------+")
    nim1 = input("Masukan NIM Anggota 1       : ")
    nama1 = input("Masukan Nama Anggota 1      : ")
    print()
    nim2 = input("Masukan NIM Anggota 2       : ")
    nama2 = input("Masukan Nama Anggota 2      : ")
    print("+------------------------------------+")
    print("\t     Selamat Datang!")
    print("+------------------------------------+")
    print('"{}" ({})!'.format(nama1, nim1))
    print('"{}" ({})!'.format(nama2, nim2))
    print("+------------------------------------+")
    print()


def stack_program():
    stack = Stack()

    while True:
        print("Program dengan Stack")
        print("1. Push (Tambah Data)")
        print("2. Pop (Hapus Data)")
        print("3. Peek (Lihat Data Teratas)")
        print("4. Ukuran Stack")
        print("5. Kembali ke Menu Utama")
        choice = int(input("Masukkan pilihan (1-5): "))

        if choice == 1:
            print("=============================================")
            item = input("Masukkan data yang ingin ditambahkan: ")
            print("=============================================")

            stack.push(item)
            print('Data "{}" telah ditambahkan ke dalam stack.'.format(item))
            print("=============================================")

        elif choice == 2:
            if not stack.is_empty():
                item = stack.pop()
                print("=============================================")
                print('Data "{}" telah dihapus dari stack.'.format(item))
                print("=============================================")
            else:
                print("Stack kosong.")
                print("=============================================")
        elif choice == 3:
            if not stack.is_empty():
                item = stack.peek()
                print("=============================================")
                print('Data teratas dalam stack adalah: "{}"'.format(item))
                print("=============================================")
            else:
                print("Stack kosong.")
                print("=============================================")
        elif choice == 4:
            print("=============================================")
            print("Ukuran stack saat ini:", stack.size())
            print("=============================================")
        elif choice == 5:
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang sesuai!")


def queue_program():
    queue = Queue()

    while True:
        print("+------------------------------------+")
        print("\tProgram dengan Queue")
        print("+------------------------------------+")
        print("1. Enqueue (Tambah Data)")
        print("2. Dequeue (Hapus Data)")
        print("3. Ukuran Queue")
        print("4. Kembali ke Menu Utama")
        choice = int(input("Masukkan pilihan (1-4): "))

        if choice == 1:
            print("=============================================")
            item = input("Masukkan data yang ingin ditambahkan: ")
            print("=============================================")

            queue.enqueue(item)
            print('Data "{}" telah ditambahkan ke dalam queue.'.format(item))
            print("=============================================")
        elif choice == 2:
            if not queue.is_empty():
                print("=============================================")
                item = queue.dequeue()
                print("=============================================")
                print('Data "{}" telah dihapus dari queue.'.format(item))
                print("=============================================")
            else:
                print("Queue kosong.")
                print("=============================================")
        elif choice == 3:
            print("=============================================")
            print("Ukuran queue saat ini:", queue.size())
            print("=============================================")
        elif choice == 4:
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang sesuai.")


def main():
    while True:
        print("+------------------------------------+")
        print("\tProgram Struktur Data")
        print("+------------------------------------+")
        print("1. Masukan Nama Kelompok")
        print("2. Gunakan Stack")
        print("3. Gunakan Queue")
        print("4. Keluar")
        choice = int(input("Masukkan pilihan (1-4): "))

        if choice == 1:
            display_data()
        elif choice == 2:
            stack_program()
        elif choice == 3:
            queue_program()
        elif choice == 4:
            print("+------------------------------------+")
            print("\t     Terima Kasih!")
            print("+------------------------------------+")
            print("Terima kasih telah menggunakan program ini.")
            print("Semoga program ini bermanfaat bagi Anda.")
            print("Sampai jumpa lagi!")
            print("+------------------------------------+")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang sesuai!")


if __name__ == '__main__':
    main()
