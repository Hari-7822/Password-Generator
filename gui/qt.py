import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QSpinBox, QTextEdit

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Password Generator")

        self.length_label = QLabel("Enter the Length of the Password:", self)

        self.length_spinbox = QSpinBox(self)
        self.length_spinbox.setRange(1, 75)
        self.length_spinbox.setValue(8)

        self.generate_button = QPushButton("Generate Password", self)
        self.generate_button.clicked.connect(self.generate_password)

        self.password_display = QTextEdit(self)
        self.password_display.setReadOnly(True)

        layout = QVBoxLayout()
        layout.addWidget(self.length_label)
        layout.addWidget(self.length_spinbox)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.password_display)

        self.setLayout(layout)

    def generate_password(self):
        upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+']

        passkey = upper + lower + numbers + symbols
        length = self.length_spinbox.value()

        password = random.sample(passkey, length)

        self.password_display.setText("".join(password))


def main():
    app = QApplication(sys.argv)
    generator = PasswordGenerator()
    generator.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
