import sys
import random
from PySide6 import QtCore, QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        
        #textbox for length
        self.length = QtWidgets.QLineEdit(self)
        self.length.move(20, 20)
        self.length.resize(280, 40)
        
        #checkbox for vars
        self.letters = QtWidgets.QCheckBox('Letters', self)
        self.letters.move(300, 50)

        self.num = QtWidgets.QCheckBox('Numbers', self)
        self.num.move(300, 80)

        self.symbols = QtWidgets.QCheckBox('Symbols', self)
        self.symbols.move(300, 110)
        

        #button
        self.btn = QtWidgets.QPushButton('Generate Password', self)
        self.btn.move(250, 150)

    @QtCore.Slot()
    def random(self):
        print('Hello')


if __name__ == '__main__':
    
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())