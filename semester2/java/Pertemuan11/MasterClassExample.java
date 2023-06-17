package Pertemuan11;

// Master class yang mengajarkan konsep dasar pemrograman
public class MasterClassExample {
    // Metode utama untuk menjalankan program
    public static void main(String[] args) {
        // Membuat objek dari kelas MasterClassExample
        MasterClassExample example = new MasterClassExample();

        // Memanggil metode dalam master class untuk mengajarkan konsep-konsep dasar
        example.learnVariables();
        example.learnLoops();
        example.learnConditionals();
        example.learnMethods();
    }

    // Metode untuk mengajarkan konsep variabel
    public void learnVariables() {
        // Deklarasi dan inisialisasi variabel
        int x = 5;
        int y = 3;
        int sum = x + y;

        // Menampilkan nilai variabel
        System.out.println("x: " + x);
        System.out.println("y: " + y);
        System.out.println("sum: " + sum);
    }

    // Metode untuk mengajarkan konsep perulangan
    public void learnLoops() {
        // Perulangan for
        for (int i = 1; i <= 5; i++) {
            System.out.println("Iteration: " + i);
        }

        // Perulangan while
        int count = 1;
        while (count <= 5) {
            System.out.println("Count: " + count);
            count++;
        }
    }

    // Metode untuk mengajarkan konsep kondisional
    public void learnConditionals() {
        int x = 10;

        // Kondisional if
        if (x > 5) {
            System.out.println("x is greater than 5");
        }

        // Kondisional if-else
        if (x % 2 == 0) {
            System.out.println("x is even");
        } else {
            System.out.println("x is odd");
        }
    }

    // Metode untuk mengajarkan konsep metode/fungsi
    public void learnMethods() {
        int result = addNumbers(2, 3);
        System.out.println("Result: " + result);
    }

    // Metode untuk menjumlahkan dua angka
    public int addNumbers(int a, int b) {
        return a + b;
    }
}
