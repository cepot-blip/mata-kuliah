package Pertemuan11;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;

public class PenjualanBarang extends JFrame implements ActionListener {
    private JComboBox<String> cmbKode;
    private JTextField txtNama, txtHarga, txtJumlah, txtJumlahBeli, txtTotalBayar, txtUangBayar, txtUangKembali;
    private JButton btnBersih, btnKeluar, btnDaftarBarang;
    private ArrayList<Barang> daftarBarang;

    public PenjualanBarang() {
        // Inisialisasi daftar barang
        daftarBarang = new ArrayList<>();

        // Membuat JFrame
        setTitle("PT TOSRBA VAN JAVA - Penjualan Barang");
        setSize(400, 300);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout());

        // Panel utama
        JPanel panel = new JPanel();
        panel.setLayout(new GridLayout(9, 2, 10, 10));
        panel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        // Membuat label dan input fields
        JLabel lblTitle = new JLabel("Penjualan Barang");
        lblTitle.setFont(new Font("Arial", Font.BOLD, 14));
        JLabel lblKode = new JLabel("Kode Barang");
        JLabel lblNama = new JLabel("Nama Barang");
        JLabel lblHarga = new JLabel("Harga Barang");
        JLabel lblJumlah = new JLabel("Jumlah Barang");
        JLabel lblJumlahBeli = new JLabel("Jumlah Beli");
        JLabel lblTotalBayar = new JLabel("Total Bayar");
        JLabel lblUangBayar = new JLabel("Uang Bayar");
        JLabel lblUangKembali = new JLabel("Uang Kembali");

        cmbKode = new JComboBox<>();
        txtNama = new JTextField();
        txtHarga = new JTextField();
        txtJumlah = new JTextField();
        txtJumlahBeli = new JTextField();
        txtTotalBayar = new JTextField();
        txtUangBayar = new JTextField();
        txtUangKembali = new JTextField();
        txtTotalBayar.setEditable(false);
        txtUangKembali.setEditable(false);

        // Menambahkan action listener ke combobox dan textfield jumlah beli
        cmbKode.addActionListener(this);
        txtJumlahBeli.addActionListener(this);

        // Membuat button
        btnBersih = new JButton("Bersih");
        btnKeluar = new JButton("Keluar");
        btnDaftarBarang = new JButton("Daftar Barang");

        // Menambahkan action listener ke button
        btnBersih.addActionListener(this);
        btnKeluar.addActionListener(this);
        btnDaftarBarang.addActionListener(this);

        // Menambahkan komponen ke panel
        panel.add(lblKode);
        panel.add(cmbKode);
        panel.add(lblNama);
        panel.add(txtNama);
        panel.add(lblHarga);
        panel.add(txtHarga);
        panel.add(lblJumlah);
        panel.add(txtJumlah);
        panel.add(lblJumlahBeli);
        panel.add(txtJumlahBeli);
        panel.add(lblTotalBayar);
        panel.add(txtTotalBayar);
        panel.add(lblUangBayar);
        panel.add(txtUangBayar);
        panel.add(lblUangKembali);
        panel.add(txtUangKembali);

        panel.add(btnBersih);
        panel.add(btnKeluar);
        panel.add(btnDaftarBarang);

        // Menambahkan panel ke JFrame
        add(lblTitle, BorderLayout.NORTH);
        add(panel, BorderLayout.CENTER);

        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == cmbKode) {
            // Mengisi informasi barang berdasarkan kode yang dipilih
            String kodeBarang = cmbKode.getSelectedItem().toString();
            Barang barang = getBarangByKode(kodeBarang);
            if (barang != null) {
                txtNama.setText(barang.getNama());
                txtHarga.setText(String.valueOf(barang.getHarga()));
                txtJumlah.setText(String.valueOf(barang.getJumlah()));
            }
        } else if (e.getSource() == txtJumlahBeli) {
            // Menghitung total bayar berdasarkan jumlah beli
            double harga = Double.parseDouble(txtHarga.getText());
            int jumlahBeli = Integer.parseInt(txtJumlahBeli.getText());
            double totalBayar = harga * jumlahBeli;
            txtTotalBayar.setText(String.valueOf(totalBayar));
        } else if (e.getSource() == btnDaftarBarang) {
            // Membuka form Daftar Barang
            new FormDaftarBarang(this);
        } else if (e.getSource() == btnBersih) {
            // Mengosongkan input fields
            cmbKode.setSelectedIndex(0);
            txtNama.setText("");
            txtHarga.setText("");
            txtJumlah.setText("");
            txtJumlahBeli.setText("");
            txtTotalBayar.setText("");
            txtUangBayar.setText("");
            txtUangKembali.setText("");
        } else if (e.getSource() == btnKeluar) {
            // Keluar dari program
            dispose();
        }
    }

    private Barang getBarangByKode(String kode) {
        for (Barang barang : daftarBarang) {
            if (barang.getKode().equals(kode)) {
                return barang;
            }
        }
        return null;
    }

    public void tambahBarang(Barang barang) {
        daftarBarang.add(barang);
        cmbKode.addItem(barang.getKode());
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new PenjualanBarang());
    }

    public static class FormDaftarBarang extends JFrame implements ActionListener {
        private JTextField txtKode, txtNama, txtHarga, txtJumlah;
        private JButton btnSimpan, btnBatal;
        private PenjualanBarang penjualanBarang;

        public FormDaftarBarang(PenjualanBarang penjualanBarang) {
            this.penjualanBarang = penjualanBarang;

            setTitle("Form Daftar Barang");
            setSize(300, 200);
            setDefaultCloseOperation(DISPOSE_ON_CLOSE);
            setLocationRelativeTo(null);
            setLayout(new BorderLayout());

            JPanel panel = new JPanel();
            panel.setLayout(new GridLayout(5, 2, 10, 10));
            panel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

            JLabel lblTitle = new JLabel("Form Daftar Barang");
            lblTitle.setFont(new Font("Arial", Font.BOLD, 14));
            JLabel lblKode = new JLabel("Kode Barang");
            JLabel lblNama = new JLabel("Nama Barang");
            JLabel lblHarga = new JLabel("Harga Barang");
            JLabel lblJumlah = new JLabel("Jumlah Barang");

            txtKode = new JTextField();
            txtNama = new JTextField();
            txtHarga = new JTextField();
            txtJumlah = new JTextField();

            btnSimpan = new JButton("Simpan");
            btnBatal = new JButton("Batal");

            btnSimpan.addActionListener(this);
            btnBatal.addActionListener(this);

            panel.add(lblKode);
            panel.add(txtKode);
            panel.add(lblNama);
            panel.add(txtNama);
            panel.add(lblHarga);
            panel.add(txtHarga);
            panel.add(lblJumlah);
            panel.add(txtJumlah);
            panel.add(btnSimpan);
            panel.add(btnBatal);

            add(lblTitle, BorderLayout.NORTH);
            add(panel, BorderLayout.CENTER);

            setVisible(true);
        }

        @Override
        public void actionPerformed(ActionEvent e) {
            if (e.getSource() == btnSimpan) {
                // Membuat objek Barang berdasarkan inputan
                String kode = txtKode.getText();
                String nama = txtNama.getText();
                double harga = Double.parseDouble(txtHarga.getText());
                int jumlah = Integer.parseInt(txtJumlah.getText());
                Barang barang = new Barang(kode, nama, harga, jumlah);

                // Menambahkan barang ke form penjualan barang
                penjualanBarang.tambahBarang(barang);

                // Menutup form daftar barang
                dispose();
            } else if (e.getSource() == btnBatal) {
                // Menutup form daftar barang
                dispose();
            }
        }
    }

    public static class Barang {
        private String kode;
        private String nama;
        private double harga;
        private int jumlah;

        public Barang(String kode, String nama, double harga, int jumlah) {
            this.kode = kode;
            this.nama = nama;
            this.harga = harga;
            this.jumlah = jumlah;
        }

        public String getKode() {
            return kode;
        }

        public String getNama() {
            return nama;
        }

        public double getHarga() {
            return harga;
        }

        public int getJumlah() {
            return jumlah;
        }
    }
}
