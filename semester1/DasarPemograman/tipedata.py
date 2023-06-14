
#   Tipedata
#   Program ini menunjukkan cara untuk mendefinisikan
#   tipe data baru.

#   Definisi tipe data baru
class Titik:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Titik(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Titik(x, y)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return Titik(x, y)

    def __truediv__(self, other):
        x = self.x / other.x
        y = self.y / other.y
        return Titik(x, y)

def main():
    # Membuat objek dari kelas Titik
    p1 = Titik(10, 20)
    p2 = Titik(30, 40)

    # Menampilkan objek
    print("p1 =", p1)
    print("")
    print("p2 =", p2)
    print("")
    print("p1 + p2 =", p1 + p2)
    print("")
    print("p1 - p2 =", p1 - p2)
    print("")
    print("p1 * p2 =", p1 * p2)
    print("")
    print("p1 / p2 =", p1 / p2)
    print("")




#    Mohamad Prihartono
#    12220015
#    Teknik Informatika
#    Universitas Nusa Mandiri Margonda
#    Thurtday, 22 September 2022
#    10:00 AM




