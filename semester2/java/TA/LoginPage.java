package TA;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class LoginPage extends JFrame implements ActionListener {
    private JLabel usernameLabel;
    private JLabel passwordLabel;
    private JTextField usernameTextField;
    private JPasswordField passwordField;
    private JButton loginButton;

    public LoginPage() {
        setTitle("Login");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridBagLayout());
        setPreferredSize(new Dimension(400, 300));

        GridBagConstraints constraints = new GridBagConstraints();
        constraints.insets = new Insets(10, 10, 10, 10);

        usernameLabel = new JLabel("Username:");
        constraints.gridx = 0;
        constraints.gridy = 0;
        add(usernameLabel, constraints);

        usernameTextField = new JTextField(15);
        constraints.gridx = 1;
        constraints.gridy = 0;
        add(usernameTextField, constraints);

        passwordLabel = new JLabel("Password:");
        constraints.gridx = 0;
        constraints.gridy = 1;
        add(passwordLabel, constraints);

        passwordField = new JPasswordField(15);
        constraints.gridx = 1;
        constraints.gridy = 1;
        add(passwordField, constraints);

        loginButton = new JButton("Login");
        loginButton.addActionListener(this);
        constraints.gridx = 1;
        constraints.gridy = 2;
        add(loginButton, constraints);

        pack();
        setLocationRelativeTo(null);
        setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(LoginPage::new);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        String username = usernameTextField.getText();
        char[] passwordChars = passwordField.getPassword();
        String password = new String(passwordChars);

        // Perform authentication logic here
        if (username.equals("admin") && password.equals("password")) {
            // Redirect to the desired code
            ListMenu app = new ListMenu();
            app.run();
            dispose(); // Close the login page
        } else {
            JOptionPane.showMessageDialog(this, "Invalid username or password", "Login Failed",
                    JOptionPane.ERROR_MESSAGE);
        }
    }
}
