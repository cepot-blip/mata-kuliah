package TA;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class MasterClass {
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            TaUas app = new TaUas();
            app.run();
        });
    }
}

class TaUas extends JFrame implements ActionListener {
    private JList<String> menuMakananList;
    private JList<String> menuMinumanList;
    private JButton pesanButton;
    private JButton bayarButton;
    private JButton keluarButton;
    private JTextField uangBayarTextField;
    private JLabel totalHargaLabel;
    private JLabel kembalianLabel;
    private int totalHarga = 0;

    private String[] menuMakanan = {
            "Nasi Goreng",
            "Mie Ayam",
            "Sate Ayam",
            "Ayam Bakar",
            "Ikan Bakar",
            "Sayur Asem",
            "Soto Lamongan",
            "Nasi Uduk",
            "Rendang"
    };

    private int[] hargaMakanan = {
            15000,
            12000,
            10000,
            20000,
            25000,
            18000,
            10000,
            15000,
            30000
    };

    private String[] menuMinuman = {
            "Es Teh",
            "Es Jeruk",
            "Es Kopi",
            "Es Campur",
            "Jus Alpukat",
            "Kopi Panas",
            "Coco Huzlenut",
            "Es Teh Manis",
            "Capucion"
    };

    private int[] hargaMinuman = {
            5000,
            6000,
            7000,
            8000,
            9000,
            3000,
            8000,
            7000,
            9000
    };

    public void run() {
        setTitle("Daftar Menu");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridBagLayout());
        setPreferredSize(new Dimension(700, 600));

        GridBagConstraints constraints = new GridBagConstraints();
        constraints.insets = new Insets(15, 15, 15, 15);

        JLabel menuMakananLabel = new JLabel("Menu Makanan");
        JLabel menuMinumanLabel = new JLabel("Menu Minuman");
        JLabel uangBayarLabel = new JLabel("Uang Bayar");
        JLabel hargaMakananLabel = new JLabel();
        JLabel hargaMinumanLabel = new JLabel();
        JScrollPane menuMakananScrollPane = new JScrollPane();
        JScrollPane menuMinumanScrollPane = new JScrollPane();
        uangBayarTextField = new JTextField(10);
        pesanButton = new JButton("Pesan");
        bayarButton = new JButton("Bayar");
        keluarButton = new JButton("Keluar");
        totalHargaLabel = new JLabel("Total Harga: Rp 0");
        kembalianLabel = new JLabel("Kembalian: Rp 0");

        pesanButton.addActionListener(this);
        bayarButton.addActionListener(this);
        keluarButton.addActionListener(this);

        menuMakananList = new JList<>(menuMakanan);
        menuMakananScrollPane.setViewportView(menuMakananList);
        menuMakananScrollPane.setPreferredSize(new Dimension(160, 200));
        menuMakananList.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        menuMakananList.addListSelectionListener(e -> {
            int index = menuMakananList.getSelectedIndex();
            if (index >= 0 && index < hargaMakanan.length) {
                hargaMakananLabel.setText("Harga: Rp " + hargaMakanan[index]);
            }
        });

        menuMinumanList = new JList<>(menuMinuman);
        menuMinumanScrollPane.setViewportView(menuMinumanList);
        menuMinumanScrollPane.setPreferredSize(new Dimension(150, 200));
        menuMinumanList.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        menuMinumanList.addListSelectionListener(e -> {
            int index = menuMinumanList.getSelectedIndex();
            if (index >= 0 && index < hargaMinuman.length) {
                hargaMinumanLabel.setText("Harga: Rp " + hargaMinuman[index]);
            }
        });

        constraints.gridx = 0;
        constraints.gridy = 0;
        add(menuMakananLabel, constraints);

        constraints.gridx = 1;
        constraints.gridy = 0;
        add(hargaMakananLabel, constraints);

        constraints.gridx = 2;
        constraints.gridy = 0;
        add(menuMinumanLabel, constraints);

        constraints.gridx = 3;
        constraints.gridy = 0;
        add(hargaMinumanLabel, constraints);

        constraints.gridx = 0;
        constraints.gridy = 1;
        constraints.gridheight = 3;
        add(menuMakananScrollPane, constraints);

        constraints.gridx = 2;
        constraints.gridy = 1;
        constraints.gridheight = 3;
        add(menuMinumanScrollPane, constraints);

        constraints.gridx = 1;
        constraints.gridy = 1;
        constraints.gridheight = 1;
        add(uangBayarLabel, constraints);

        constraints.gridx = 1;
        constraints.gridy = 2;
        add(uangBayarTextField, constraints);

        constraints.gridx = 0;
        constraints.gridy = 4;
        constraints.gridwidth = 2;
        add(pesanButton, constraints);

        constraints.gridx = 2;
        constraints.gridy = 4;
        add(bayarButton, constraints);

        constraints.gridx = 3;
        constraints.gridy = 4;
        add(keluarButton, constraints);

        constraints.gridx = 0;
        constraints.gridy = 5;
        constraints.gridwidth = 4;
        add(totalHargaLabel, constraints);

        constraints.gridx = 0;
        constraints.gridy = 6;
        constraints.gridwidth = 4;
        add(kembalianLabel, constraints);

        pack();
        setLocationRelativeTo(null);
        setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == pesanButton) {
            int makananIndex = menuMakananList.getSelectedIndex();
            int minumanIndex = menuMinumanList.getSelectedIndex();

            int hargaMakananTerpilih = hargaMakanan[makananIndex];
            int hargaMinumanTerpilih = hargaMinuman[minumanIndex];

            totalHarga = hargaMakananTerpilih + hargaMinumanTerpilih;
            totalHargaLabel.setText("Total Harga: Rp " + totalHarga);

            int uangBayar = Integer.parseInt(uangBayarTextField.getText());

            int kembalian = uangBayar - totalHarga;
            kembalianLabel.setText("Kembalian: Rp " + kembalian);
        } else if (e.getSource() == bayarButton) {
            int makananIndex = menuMakananList.getSelectedIndex();
            int minumanIndex = menuMinumanList.getSelectedIndex();

            int hargaMakananTerpilih = hargaMakanan[makananIndex];
            int hargaMinumanTerpilih = hargaMinuman[minumanIndex];

            totalHarga = hargaMakananTerpilih + hargaMinumanTerpilih;
            totalHargaLabel.setText("Total Harga: Rp " + totalHarga);

            int uangBayar = Integer.parseInt(uangBayarTextField.getText());

            int kembalian = uangBayar - totalHarga;
            kembalianLabel.setText("Kembalian: Rp " + kembalian);

            String message = "Terima kasih telah melakukan pembayaran.\n\n" +
                    "Detail Pembayaran :\n" +
                    "Total Harga      : Rp " + totalHarga + "\n" +
                    "Uang Bayar       : Rp " + uangBayar + "\n" +
                    "Kembalian        : Rp " + kembalian;
            JOptionPane.showMessageDialog(this, message, "Pembayaran Berhasil", JOptionPane.INFORMATION_MESSAGE);
        } else if (e.getSource() == keluarButton) {
            int result = JOptionPane.showConfirmDialog(this, "Apakah Anda yakin ingin keluar?", "Konfirmasi Keluar",
                    JOptionPane.YES_NO_OPTION);
            if (result == JOptionPane.YES_OPTION) {
                System.exit(0);
            }
        }
    }
}
