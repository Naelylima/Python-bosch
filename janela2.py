import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit

class Janela2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 500
        self.altura = 600

        self.botao9 = QPushButton(self)
        self.botao9.move(356, 395)
        self.botao9.resize(100, 100)
        self.botao9.setFlat(False)

        self.show()
        self.carregar_janela_nova()
        self.hide()




    def carregar_janela_nova(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.show()

stylesheet = """
        Janela2 {
            background-color: white;
        }

    """


