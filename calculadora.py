import sys
from PyQt5.QtWidgets import QAction, QApplication, QGridLayout, QLineEdit, QMainWindow, QMessageBox, QPushButton
from PyQt5.QtGui import QDoubleValidator, QIcon
from PyQt5 import QtCore

class Calculadora(QMainWindow):

    def __init__ (self):
        super().__init__()
        self.setGeometry(100,100,210,285)
        self.setWindowTitle('Calculadora')
        self.setWindowIcon(QIcon('assets/calculator.png'))
        self.textoInterface()
        self.criarMenu()      
        self.criarBotoes() 
        #...
        self.show()

    def textoInterface(self):
        
        self.so_double = QDoubleValidator()      
        self.numeros_texto = QLineEdit(self)
        self.numeros_texto.setValidator(self.so_double)
        self.numeros_texto.move(10,30)
        self.numeros_texto.resize(190,50)
        self.numeros_texto.setMaxLength(20)
        self.numeros_texto.setAlignment(QtCore.Qt.AlignRight)
        self.numeros_texto.setText("0")
        self.fonte = self.numeros_texto.font()
        self.fonte.setPointSize(18)
        self.numeros_texto.setFont(self.fonte)
    
    def criarMenu(self):
        
        copy_act = QAction('Copiar',self)
        copy_act.setShortcut('Ctrl+C')
        copy_act.triggered.connect(self.numeros_texto.copy)

        paste_act = QAction('Colar',self)
        paste_act.setShortcut('Ctrl+V')
        paste_act.triggered.connect(self.numeros_texto.paste)

        about_act = QAction('Sobre a Calculadora',self)
        about_act.triggered.connect(self.aboutusText)

        menu_bar = self.menuBar()       

        edit_menu = menu_bar.addMenu('Editar')
        edit_menu.addAction(copy_act)
        edit_menu.addAction(paste_act)

        help_menu = menu_bar.addMenu('Ajuda')
        help_menu.addAction(about_act)

    def aboutusText(self):
        QMessageBox.about(self, "Sobre Calculadora", "github/camillapd")

    def criarBotoes(self):

        comma_button = QPushButton(",")
        #comma_button.triggered.connect

        plus_button = QPushButton("+")
        #plus_button.triggered.connect

        minus_button = QPushButton("-")
        #minus_button.triggered.connect       

        divison_button = QPushButton("/")
        #division_button.triggered.connect

        multiply_button = QPushButton("*")
        #multiply_button.triggered.connect

        equals_button = QPushButton("=")
        #equals_button.triggered.connect

        sqrt_button = QPushButton("√")
        #sqrt_button.triggered.connect

        power_button = QPushButton("x²")
        #power_button.triggered.connect

        half_button = QPushButton("1/2")
        #half_button.triggered.connect

        plusminus_button = QPushButton("±")
        #plusminus_button.triggered.connect

        backspace_button = QPushButton("←")
        #backspace_button.triggered.connect

        clear_button = QPushButton("C")
        #clear_button.triggered.connect

        #for i in range(0,9):
         #   digit_button[i] = QPushButton(i)


        button_grid = QGridLayout()
        button_grid.setContentsMargins(5, 5, 5, 5)
        button_grid.addWidget(clear_button,10,10,5,5)


def main():
    app = QApplication([])
    window = Calculadora()
    sys.exit(app.exec_())

## MAIN ##
if __name__ == '__main__':
    main()