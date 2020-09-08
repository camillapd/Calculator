import sys
from PyQt5.QtWidgets import QAction, QApplication, QLineEdit, QMainWindow, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore

class Calculadora(QMainWindow):

    def __init__ (self):
        super().__init__()
        self.setGeometry(100,100,210,285)
        self.setWindowTitle('Calculadora')
        self.setWindowIcon(QIcon('assets/calculator.png'))
        self.textoInterface()
        self.criarMenu()       
        #...
        self.show()

    def textoInterface(self):
    
        self.numeros_texto = QLineEdit(self)
        self.numeros_texto.move(10,30)
        self.numeros_texto.resize(190,50)
        self.numeros_texto.setMaxLength(20)
        self.numeros_texto.setAlignment(QtCore.Qt.AlignRight)
        self.numeros_texto.setText("0")
    
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
        QMessageBox.about(self, "Sobre Calculadora", "github/cammievolsci")


    

def main():
    app = QApplication([])
    window = Calculadora()
    sys.exit(app.exec_())

## MAIN ##
if __name__ == '__main__':
    main()