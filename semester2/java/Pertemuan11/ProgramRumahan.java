package Pertemuan11;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.HashMap;
import java.util.Map;

public class ProgramRumahan extends JFrame implements ActionListener {
    private JLabel titleLabel;
    private JLabel lokasiLabel;
    private JLabel hargaDasarLabel;
    private JLabel fasilitasLabel;
    private JLabel pembayaranLabel;
    private JLabel totalLabel;
    private JCheckBox jogingTrackCheckBox;
    private JCheckBox swimmingPoolCheckBox;
    private JCheckBox gymnasiumCheckBox;
    private JRadioButton bcaRadioButton;
    private JRadioButton otherBankRadioButton;
    private JComboBox<String> lokasiComboBox;
    private JTextField hargaDasarTextField;
    private JTextField totalTextField;
    private JButton hitungButton;
    private JButton bersihButton;
    private JButton keluarButton;

    private Map<String, Integer> hargaDasarMap;

    private static final String[] lokasiOptions = {
            "PILIH",
            "DEPOK",
            "CITAYAM",
            "BOGOR",
            "JAKARTA",
            "TANGERANG",
            "BEKASI",
            "BANDUNG",
            "SEMARANG",
            "SURABAYA",
            "YOGYAKARTA",
            "MALANG",
            "DENPASAR",
    };

    public ProgramRumahan() {
        setTitle("DEVELOPER PERUMAHAN PT RUMAH MURAH MERIAH");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridBagLayout());
        setPreferredSize(new Dimension(700, 600));

        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(10, 10, 10, 10);

        titleLabel = new JLabel("DATA RUMAH");
        titleLabel.setFont(new Font("Arial", Font.BOLD, 16));
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.gridwidth = 2;
        add(titleLabel, gbc);

        lokasiLabel = new JLabel("Lokasi");
        gbc.gridx = 0;
        gbc.gridy = 1;
        gbc.gridwidth = 1;
        add(lokasiLabel, gbc);

        lokasiComboBox = new JComboBox<>(lokasiOptions);
        gbc.gridx = 1;
        gbc.gridy = 1;
        gbc.gridwidth = 1;
        add(lokasiComboBox, gbc);

        hargaDasarLabel = new JLabel("Harga Dasar");
        gbc.gridx = 0;
        gbc.gridy = 2;
        gbc.gridwidth = 1;
        add(hargaDasarLabel, gbc);

        hargaDasarTextField = new JTextField();
        hargaDasarTextField.setPreferredSize(new Dimension(200, 30));
        gbc.gridx = 1;
        gbc.gridy = 2;
        gbc.gridwidth = 1;
        add(hargaDasarTextField, gbc);

        fasilitasLabel = new JLabel("Fasilitas Rumah");
        gbc.gridx = 0;
        gbc.gridy = 3;
        gbc.gridwidth = 2;
        add(fasilitasLabel, gbc);

        jogingTrackCheckBox = new JCheckBox("Joging Track - Rp. 100,000.00");
        gbc.gridx = 0;
        gbc.gridy = 4;
        gbc.gridwidth = 2;
        add(jogingTrackCheckBox, gbc);

        swimmingPoolCheckBox = new JCheckBox("Swimming Pool - Rp. 200,000.00");
        gbc.gridx = 0;
        gbc.gridy = 5;
        gbc.gridwidth = 2;
        add(swimmingPoolCheckBox, gbc);

        gymnasiumCheckBox = new JCheckBox("Gymnasium - Rp. 300,000.00");
        gbc.gridx = 0;
        gbc.gridy = 6;
        gbc.gridwidth = 2;
        add(gymnasiumCheckBox, gbc);

        pembayaranLabel = new JLabel("Metode Pembayaran");
        gbc.gridx = 0;
        gbc.gridy = 7;
        gbc.gridwidth = 2;
        add(pembayaranLabel, gbc);

        bcaRadioButton = new JRadioButton("BCA");
        gbc.gridx = 0;
        gbc.gridy = 8;
        gbc.gridwidth = 1;
        add(bcaRadioButton, gbc);

        otherBankRadioButton = new JRadioButton("Other Bank");
        gbc.gridx = 1;
        gbc.gridy = 8;
        gbc.gridwidth = 1;
        add(otherBankRadioButton, gbc);

        totalLabel = new JLabel("Total Harga");
        gbc.gridx = 0;
        gbc.gridy = 9;
        gbc.gridwidth = 1;
        add(totalLabel, gbc);

        totalTextField = new JTextField();
        totalTextField.setEditable(false);
        totalTextField.setPreferredSize(new Dimension(200, 30));
        gbc.gridx = 1;
        gbc.gridy = 9;
        gbc.gridwidth = 1;
        add(totalTextField, gbc);

        hitungButton = new JButton("Hitung");
        hitungButton.addActionListener(this);
        gbc.gridx = 0;
        gbc.gridy = 10;
        gbc.gridwidth = 1;
        add(hitungButton, gbc);

        bersihButton = new JButton("Bersih");
        bersihButton.addActionListener(this);
        gbc.gridx = 1;
        gbc.gridy = 10;
        gbc.gridwidth = 1;
        add(bersihButton, gbc);

        keluarButton = new JButton("Keluar");
        keluarButton.addActionListener(this);
        gbc.gridx = 0;
        gbc.gridy = 11;
        gbc.gridwidth = 2;
        add(keluarButton, gbc);

        pack();
        setLocationRelativeTo(null);
        setVisible(true);

        hargaDasarMap = new HashMap<>();
        hargaDasarMap.put("DEPOK", 100000000);
        hargaDasarMap.put("CITAYAM", 95000000);
        hargaDasarMap.put("BOGOR", 120000000);
        hargaDasarMap.put("JAKARTA", 150000000);
        hargaDasarMap.put("TANGERANG", 100000000);
        hargaDasarMap.put("BEKASI", 90000000);
        hargaDasarMap.put("BANDUNG", 110000000);
        hargaDasarMap.put("SEMARANG", 80000000);
        hargaDasarMap.put("SURABAYA", 130000000);
        hargaDasarMap.put("YOGYAKARTA", 95000000);
        hargaDasarMap.put("MALANG", 115000000);
        hargaDasarMap.put("DENPASAR", 140000000);

        lokasiComboBox.addActionListener(this);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(ProgramRumahan::new);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == hitungButton) {
            int totalHarga = Integer.parseInt(hargaDasarTextField.getText());

            if (jogingTrackCheckBox.isSelected()) {
                totalHarga += 100000;
            }
            if (swimmingPoolCheckBox.isSelected()) {
                totalHarga += 200000;
            }
            if (gymnasiumCheckBox.isSelected()) {
                totalHarga += 300000;
            }

            totalTextField.setText(String.valueOf(totalHarga));

            // Popup detail pembayaran
            String fasilitas = getSelectedFasilitas();
            String metodePembayaran = getSelectedMetodePembayaran();
            String detailPembayaran = "Detail Pembayaran\n\n" +
                    "Fasilitas: " + fasilitas + "\n" +
                    "Metode Pembayaran: " + metodePembayaran + "\n" +
                    "Total Harga: Rp " + totalHarga;

            JOptionPane.showMessageDialog(this, detailPembayaran, "Detail Pembayaran", JOptionPane.INFORMATION_MESSAGE);

        } else if (e.getSource() == bersihButton) {
            lokasiComboBox.setSelectedIndex(0);
            hargaDasarTextField.setText("");
            jogingTrackCheckBox.setSelected(false);
            swimmingPoolCheckBox.setSelected(false);
            gymnasiumCheckBox.setSelected(false);
            bcaRadioButton.setSelected(true);
            totalTextField.setText("");
        } else if (e.getSource() == keluarButton) {

            int confirm = JOptionPane.showConfirmDialog(this, "Apakah Anda yakin ingin keluar?", "Konfirmasi Keluar",
                    JOptionPane.YES_NO_OPTION);
            if (confirm == JOptionPane.YES_OPTION) {
                System.exit(0);
            }
        } else if (e.getSource() == lokasiComboBox) {
            String selectedLokasi = (String) lokasiComboBox.getSelectedItem();
            if (selectedLokasi != null) {
                int hargaDasar = hargaDasarMap.getOrDefault(selectedLokasi, 0);
                hargaDasarTextField.setText(String.valueOf(hargaDasar));
            }
        }
    }

    private String getSelectedFasilitas() {
        StringBuilder fasilitas = new StringBuilder();
        if (jogingTrackCheckBox.isSelected()) {
            fasilitas.append("Joging Track, ");
        }
        if (swimmingPoolCheckBox.isSelected()) {
            fasilitas.append("Swimming Pool, ");
        }
        if (gymnasiumCheckBox.isSelected()) {
            fasilitas.append("Gymnasium, ");
        }
        if (fasilitas.length() > 0) {
            fasilitas.deleteCharAt(fasilitas.length() - 2);
        }
        return fasilitas.toString();
    }

    private String getSelectedMetodePembayaran() {
        if (bcaRadioButton.isSelected()) {
            return "BCA";
        } else if (otherBankRadioButton.isSelected()) {
            return "Other Bank";
        }
        return "";
    }
}
