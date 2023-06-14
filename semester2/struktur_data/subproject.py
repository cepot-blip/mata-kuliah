# Implementasi dengan menggunakan Array

class Obat:
    def __init__(self, title, pembuat):
        self.title = title
        self.pembuat = pembuat


class ObatstoreArray:
    def __init__(self):
        self.obats = []

    def add_obat(self, title, pembuat):
        obat = Obat(title, pembuat)
        self.obats.append(obat)

    def find_obat(self, title):
        for obat in self.obats:
            if obat.title == title:
                return obat
        return None

    def remove_obat(self, title):
        for obat in self.obats:
            if obat.title == title:
                self.obats.remove(obat)
                return True
        return False

    def display_obats(self):
        if not self.obats:
            print("Tidak ada obat yang tersedia.")
        else:
            print("Daftar Obat:")
            for obat in self.obats:
                print("Judul:", obat.title)
                print("Pembuat:", obat.pembuat)
                print()


# Implementasi dengan menggunakan Linked List

class Node:
    def __init__(self, title, pembuat):
        self.title = title
        self.pembuat = pembuat
        self.next = None


class ObatstoreLinkedList:
    def __init__(self):
        self.head = None

    def add_obat(self, title, pembuat):
        obat = Node(title, pembuat)
        if not self.head:
            self.head = obat
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = obat

    def find_obat(self, title):
        current = self.head
        while current:
            if current.title == title:
                return current
            current = current.next
        return None

    def remove_obat(self, title):
        if not self.head:
            return False

        if self.head.title == title:
            self.head = self.head.next
            return True

        prev = self.head
        current = self.head.next
        while current:
            if current.title == title:
                prev.next = current.next
                return True
            prev = current
            current = current.next

        return False

    def display_obats(self):
        if not self.head:
            print("Tidak ada obat yang tersedia.")
        else:
            current = self.head
            print("Daftar Obat:")
            while current:
                print("Judul:", current.title)
                print("Pembuat:", current.pembuat)
                print()
                current = current.next


# Program Utama

def main():
    print("+------------------------------------+")
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    print("+------------------------------------+")

    print("Selamat datang, {} ({})!".format(nama, nim))
    while True:
        print("\nMenu Utama:")
        print("1. Gunakan Program Array")
        print("2. Gunakan Program Linked List")
        print("3. Keluar")

        choice = int(input("Masukkan pilihan (1-3): "))

        if choice == 1:
            obatstore = ObatstoreArray()
            while True:
                print("\nProgram Array - Penjualan Obat")
                print("1. Tambah Obat")
                print("2. Cari Obat")
                print("3. Hapus Obat")
                print("4. Tampilkan Daftar Obat")
                print("5. Kembali ke Menu Utama")

                option = int(input("Masukkan pilihan (1-5): "))

                if option == 1:
                    title = input("Masukkan judul obat: ")
                    pembuat = input("Masukkan nama pembuat: ")
                    obatstore.add_obat(title, pembuat)
                    print("Obat telah ditambahkan.")
                elif option == 2:
                    title = input("Masukkan judul obat yang ingin dicari: ")
                    obat = obatstore.find_obat(title)
                    if obat:
                        print("Obat ditemukan:")
                        print("Judul:", obat.title)
                        print("Pembuat:", obat.pembuat)
                    else:
                        print("Obat tidak ditemukan.")
                elif option == 3:
                    title = input("Masukkan judul obat yang ingin dihapus: ")
                    removed = obatstore.remove_obat(title)
                    if removed:
                        print("Obat telah dihapus.")
                    else:
                        print("Obat tidak ditemukan.")
                elif option == 4:
                    obatstore.display_obats()
                elif option == 5:
                    break
                else:
                    print("Pilihan tidak valid. Silakan pilih kembali.")

        elif choice == 2:
            obatstore = ObatstoreLinkedList()
            while True:
                print("\nProgram Linked List - Penjualan Obat")
                print("1. Tambah Obat")
                print("2. Cari Obat")
                print("3. Hapus Obat")
                print("4. Tampilkan Daftar Obat")
                print("5. Kembali ke Menu Utama")

                option = int(input("Masukkan pilihan (1-5): "))

                if option == 1:
                    title = input("Masukkan judul obat: ")
                    pembuat = input("Masukkan nama pembuat: ")
                    obatstore.add_obat(title, pembuat)
                    print("Obat telah ditambahkan.")
                elif option == 2:
                    title = input("Masukkan judul obat yang ingin dicari: ")
                    obat = obatstore.find_obat(title)
                    if obat:
                        print("Obat ditemukan:")
                        print("Judul:", obat.title)
                        print("Pembuat:", obat.pembuat)
                    else:
                        print("Obat tidak ditemukan.")
                elif option == 3:
                    title = input("Masukkan judul obat yang ingin dihapus: ")
                    removed = obatstore.remove_obat(title)
                    if removed:
                        print("Obat telah dihapus.")
                    else:
                        print("Obat tidak ditemukan.")
                elif option == 4:
                    obatstore.display_obats()
                elif option == 5:
                    break
                else:
                    print("Pilihan tidak valid. Silakan pilih kembali.")

        elif choice == 3:
            print("Terima kasih telah menggunakan program.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih kembali.")


if __name__ == "__main__":
    main()
