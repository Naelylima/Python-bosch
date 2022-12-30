import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QMovie


class Joken(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 500

        self.movie = QMovie('joken.gif')
        self.gif = QLabel(self)
        self.gif.resize(800, 500)
        self.gif.setMovie(self.movie)
        self.gif.setScaledContents(True)
        self.movie.start()

        self.botao_pedra = QPushButton(self)
        self.botao_pedra.move(20, 35)
        self.botao_pedra.resize(100, 100)
        self.botao_pedra.setFlat(True)

        self.botao_papel = QPushButton(self)
        self.botao_papel.move(20, 170)
        self.botao_papel.resize(100, 120)
        self.botao_papel.setFlat(True)

        self.botao_tesoura = QPushButton(self)
        self.botao_tesoura.move(20, 320)
        self.botao_tesoura.resize(100, 100)
        self.botao_tesoura.setFlat(True)

        self.botao_reset = QPushButton(self)
        self.botao_reset.move(680, 15)
        self.botao_reset.resize(100, 40)
        self.botao_reset.setFlat(True)

        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
if __name__ == "__main__":
    aplicacao = QApplication(sys.argv)
    j = Joken()
    j.show()
    sys.exit(aplicacao.exec())