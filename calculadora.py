import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class Calculadora(QMainWindow):

    def __init__ (self):
        super().__init__()
        self.setGeometry(100,100,210,285)
        self.setWindowTitle('Calculadora')
        #...
        self.show()

def main():
    app = QApplication([])
    window = Calculadora()
    sys.exit(app.exec_())

## MAIN ##
if __name__ == '__main__':
    main()