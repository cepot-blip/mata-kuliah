package Pertemuan9;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class LoginPage extends JFrame implements ActionListener {
    private JLabel lblUsername, lblPassword;
    private JTextField txtUsername;
    private JPasswordField txtPassword;
    private JButton btnLogin, btnRegister;

    public LoginPage() {
        // Membuat JFrame
        setTitle("Login Page");
        setSize(300, 200);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout());
        getContentPane().setBackground(Color.WHITE);

        // Panel utama untuk mengatur posisi komponen di tengah
        JPanel panel = new JPanel();
        panel.setLayout(new GridBagLayout());
        panel.setBackground(Color.WHITE);
        panel.setBorder(BorderFactory.createEmptyBorder(10, 10, 10, 10));

        // Membuat label dan menentukan posisi
        lblUsername = new JLabel("Username");
        lblPassword = new JLabel("Password");

        // Membuat text field dengan tampilan rounded
        txtUsername = new JTextField(15);
        txtPassword = new JPasswordField(15);
        txtUsername.setBorder(BorderFactory.createBevelBorder(5));
        txtPassword.setBorder(BorderFactory.createBevelBorder(5));

        // Membuat button Login dan Register
        btnLogin = new JButton("Login");
        btnRegister = new JButton("Register");

        // Menambahkan komponen ke panel dengan pengaturan posisi
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.insets = new Insets(5, 0, 5, 0);
        panel.add(lblUsername, gbc);

        gbc.gridy = 1;
        panel.add(lblPassword, gbc);

        gbc.gridx = 1;
        gbc.gridy = 0;
        panel.add(txtUsername, gbc);

        gbc.gridy = 1;
        panel.add(txtPassword, gbc);

        gbc.gridx = 1;
        gbc.gridy = 2;
        panel.add(btnLogin, gbc);

        gbc.gridy = 3;
        panel.add(btnRegister, gbc);

        // Menambahkan panel ke JFrame
        add(panel, BorderLayout.CENTER);
    }

    public void actionPerformed(ActionEvent e) {
        // ... kode action listener lainnya ...
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            LoginPage loginPage = new LoginPage();
            loginPage.setVisible(true);
        });
    }
}
