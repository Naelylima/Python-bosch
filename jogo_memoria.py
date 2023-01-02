import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QMovie


class Memoria(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 500

        self.chute = ''
        self.chute2 = ''
        self.click = 1

        self.movie = QMovie('memoria1.gif')
        self.gif = QLabel(self)
        self.gif.resize(800, 500)
        self.gif.setMovie(self.movie)
        self.gif.setScaledContents(True)
        self.movie.start()

        self.botao1 = QPushButton(self)
        self.botao1.move(310, 65)
        self.botao1.resize(75, 75)
        self.botao1.setFlat(False)
        self.botao1.clicked.connect(self.chamar_botao1)

        self.botao2 = QPushButton(self)
        self.botao2.move(425, 63)
        self.botao2.resize(75, 75)
        self.botao2.setFlat(False)
        self.botao2.clicked.connect(self.chamar_botao2)

        self.botao3 = QPushButton(self)
        self.botao3.move(550, 63)
        self.botao3.resize(75, 75)
        self.botao3.setFlat(False)
        self.botao3.clicked.connect(self.chamar_botao3)

        self.botao4 = QPushButton(self)
        self.botao4.move(670, 63)
        self.botao4.resize(75, 75)
        self.botao4.setFlat(False)
        self.botao4.clicked.connect(self.chamar_botao4)

        self.botao5 = QPushButton(self)
        self.botao5.move(308, 200)
        self.botao5.resize(75, 75)
        self.botao5.setFlat(False)
        self.botao5.clicked.connect(self.chamar_botao5)

        self.botao6 = QPushButton(self)
        self.botao6.move(425, 200)
        self.botao6.resize(75, 75)
        self.botao6.setFlat(False)
        self.botao6.clicked.connect(self.chamar_botao6)

        self.botao7 = QPushButton(self)
        self.botao7.move(550, 200)
        self.botao7.resize(75, 75)
        self.botao7.setFlat(False)
        self.botao7.clicked.connect(self.chamar_botao7)

        self.botao8 = QPushButton(self)
        self.botao8.move(670, 200)
        self.botao8.resize(75, 75)
        self.botao8.setFlat(False)
        self.botao8.clicked.connect(self.chamar_botao8)

        self.botao9 = QPushButton(self)
        self.botao9.move(308, 335)
        self.botao9.resize(75, 75)
        self.botao9.setFlat(False)
        self.botao9.clicked.connect(self.chamar_botao9)

        self.botao10 = QPushButton(self)
        self.botao10.move(425, 335)
        self.botao10.resize(75, 75)
        self.botao10.setFlat(False)
        self.botao10.clicked.connect(self.chamar_botao10)

        self.botao11 = QPushButton(self)
        self.botao11.move(550, 335)
        self.botao11.resize(75, 75)
        self.botao11.setFlat(False)
        self.botao11.clicked.connect(self.chamar_botao11)

        self.botao12 = QPushButton(self)
        self.botao12.move(670, 335)
        self.botao12.resize(75, 75)
        self.botao12.setFlat(False)
        self.botao12.clicked.connect(self.chamar_botao12)


        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
