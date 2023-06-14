class Stack:
    def __init__(self):
        self.items = []                     # Inisialisasi stack dengan list kosong

    def is_empty(self):
        return len(self.items) == 0         # Cek apakah stack kosong

    def push(self, item):
        self.items.append(item)             # Tambahkan item ke dalam stack

    def pop(self):
        if not self.is_empty():
            return self.items.pop()         # Hapus dan kembalikan item teratas dari stack

    def peek(self):
        if not self.is_empty():
            return self.items[-1]           # Ambil item teratas dari stack

    def size(self):
        return len(self.items)              # Kembalikan ukuran stack


class Queue:
    def __init__(self):
        self.items = []                     # Inisialisasi queue dengan list kosong

    def is_empty(self):
        return len(self.items) == 0         # Cek apakah queue kosong

    def enqueue(self, item):
        self.items.append(item)             # Tambahkan item ke dalam queue

    def dequeue(self):
        if not self.is_empty():
            # Hapus dan kembalikan item pertama dari queue
            return self.items.pop(0)

    def size(self):
        return len(self.items)              # Kembalikan ukuran queue


def stack_program():
    stack = Stack()

    while True:
        print("+------------------------------------+")
        print("\tProgram dengan Stack")
        print("+------------------------------------+")
        print("1. Push (Tambah Data)")
        print("2. Pop (Hapus Data)")
        print("3. Peek (Lihat Data Teratas)")
        print("4. Ukuran Stack")
        print("5. Kembali ke Menu Utama")
        choice = int(input("Masukkan pilihan (1-5): "))

        if choice == 1:
            print("**************************************")
            item = input("Masukkan data yang ingin ditambahkan: ")
            print("**************************************")

            stack.push(item)
            print("Data", item, "telah ditambahkan ke dalam stack.")
            print("**************************************")

        elif choice == 2:
            if not stack.is_empty():
                item = stack.pop()
                print("**************************************")
                print("Data", item, "telah dihapus dari stack.")
                print("**************************************")

            else:
                print("Stack kosong.")

        elif choice == 3:
            if not stack.is_empty():
                item = stack.peek()
                print("**************************************")
                print("Data teratas dalam stack adalah:", item)
                print("**************************************")

            else:
                print("Stack kosong.")
        elif choice == 4:
            print("**************************************")
            print("Ukuran stack saat ini:", stack.size())
            print("**************************************")

        elif choice == 5:
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang sesuai.")


def queue_program():
    queue = Queue()

    while True:
        print("+------------------------------------+")
        print("Program dengan Queue")
        print("+------------------------------------+")
        print("1. Enqueue (Tambah Data)")
        print("2. Dequeue (Hapus Data)")
        print("3. Ukuran Queue")
        print("4. Kembali ke Menu Utama")
        choice = int(input("Masukkan pilihan (1-4): "))

        if choice == 1:
            print("**************************************")
            item = input("Masukkan data yang ingin ditambahkan: ")
            print("**************************************")

            queue.enqueue(item)
            print("Data", item, "telah ditambahkan ke dalam queue.")
            print("**************************************")

        elif choice == 2:
            if not queue.is_empty():
                item = queue.dequeue()
                print("**************************************")
                print("Data", item, "telah dihapus dari queue.")
                print("**************************************")
            else:
                print("Queue kosong.")
        elif choice == 3:
            print("**************************************")
            print("Ukuran queue saat ini:", queue.size())
            print("**************************************")
        elif choice == 4:
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang sesuai.")


def main():
    while True:
        print("+------------------------------------+")
        print("\tProgram Struktur Data")
        print("+------------------------------------+")
        print("\t     Kelompok 2")
        print("-------------------------------------")
        print("1. 12220014 Anggoro Bayu Prasetyo")
        print("2. 12220015 Mohamad Prihartono")
        print("+------------------------------------+")
        print("1. Gunakan Program Stack")
        print("2. Gunakan Program Queue")
        print("3. Keluar")
        choice = int(input("Masukkan pilihan (1-3): "))

        if choice == 1:
            stack_program()
        elif choice == 2:
            queue_program()
        elif choice == 3:
            print("***********************************************************")
            print("Terima kasih telah menggunakan program ini. Sampai jumpa :)")
            print("***********************************************************")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan pilihan yang sesuai.")


if __name__ == '__main__':
    main()
