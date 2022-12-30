import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QMovie


class Velha(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 500

        self.movie = QMovie('velha.gif')
        self.gif = QLabel(self)
        self.gif.resize(800, 500)
        self.gif.setMovie(self.movie)
        self.gif.setScaledContents(True)
        self.movie.start()

        self.botao1 = QPushButton(self)
        self.botao1.move(170, 140)  # distancia da esquerda- topo
        self.botao1.resize(90, 90)  # largura - altura
        self.botao1.setFlat(True)
        # self.botao1.clicked.connect(lambda: self.jogadas(1))

        self.botao2 = QPushButton(self)
        self.botao2.move(170, 260)
        self.botao2.resize(90, 90)
        self.botao2.setFlat(True)
        # # self.botao2.clicked.connect(lambda: self.jogadas(2))
        #
        self.botao3 = QPushButton(self)
        self.botao3.move(170, 375)
        self.botao3.resize(90, 90)
        self.botao3.setFlat(True)
        # # self.botao3.clicked.connect(lambda: self.jogadas(3))
        #
        self.botao4 = QPushButton(self)
        self.botao4.move(280, 140)
        self.botao4.resize(90, 90)
        self.botao4.setFlat(True)
        # # self.botao4.clicked.connect(lambda: self.jogadas(4))
        #

        self.botao5 = QPushButton(self)
        self.botao5.move(280, 260)
        self.botao5.resize(90, 90)
        self.botao5.setFlat(True)
        # # self.botao5.clicked.connect(lambda: self.jogadas(6))

        self.botao6 = QPushButton(self)
        self.botao6.move(280, 375)
        self.botao6.resize(90, 90)
        self.botao6.setFlat(True)
        # # self.botao6.clicked.connect(lambda: self.jogadas(5))

        self.botao7 = QPushButton(self)
        self.botao7.move(392, 140)
        self.botao7.resize(90, 90)
        self.botao7.setFlat(True)
        # # self.botao7.clicked.connect(lambda: self.jogadas(7))
        #
        self.botao8 = QPushButton(self)
        self.botao8.move(392, 260)
        self.botao8.resize(90, 90)
        self.botao8.setFlat(True)
        # # self.botao8.clicked.connect(lambda: self.jogadas(8))
        #
        self.botao9 = QPushButton(self)
        self.botao9.move(392, 375)
        self.botao9.resize(90, 90)
        self.botao9.setFlat(True)
        # # self.botao9.clicked.connect(lambda: self.jogadas(9))

        self.botao_reset = QPushButton(self)
        self.botao_reset.move(10, 450)
        self.botao_reset.resize(100, 40)
        self.botao_reset.setFlat(True)

        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)


if __name__ == "__main__":
    aplicacao = QApplication(sys.argv)
    j = Velha()
    sys.exit(aplicacao.exec())
