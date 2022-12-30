import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QMovie
from tela2 import jogo_velha
from tela3 import jogo_forca
from tela4 import jogo_joken
from tela5 import jogo_memoria


class Janela(QMainWindow):  # Herança
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 500

        self.movie = QMovie('principal.gif')
        self.gif = QLabel(self)
        self.gif.resize(800, 500)
        self.gif.setMovie(self.movie)
        self.gif.setScaledContents(True)
        self.movie.start()

        self.botao_velha = QPushButton(self)
        self.botao_velha.move(243, 250)
        self.botao_velha.resize(100, 30)
        self.botao_velha.setFlat(True)
        self.botao_velha.clicked.connect(self.chamar_velha)

        self.botao_forca = QPushButton(self)
        self.botao_forca.move(243, 310)
        self.botao_forca.resize(100, 30)
        self.botao_forca.setFlat(True)
        self.botao_forca.clicked.connect(self.chamar_forca)

        self.botao_joken = QPushButton(self)
        self.botao_joken.move(450, 250)
        self.botao_joken.resize(100, 30)
        self.botao_joken.setFlat(True)
        self.botao_joken.clicked.connect(self.chamar_joken)


        self.botao_memoria = QPushButton(self)
        self.botao_memoria.move(455, 310)
        self.botao_memoria.resize(100, 30)
        self.botao_memoria.setFlat(True)
        self.botao_memoria.clicked.connect(self.chamar_memoria)


        self.carregar_janela()

    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.show()

    def chamar_velha(self):
        velha.show()

    def chamar_forca(self):
        forca.show()

    def chamar_joken(self):
        joken.show()

    def chamar_memoria(self):
        memoria.show()

if __name__ == "__main__":
    aplicacao = QApplication(sys.argv)
    j = Janela()
    velha = jogo_velha.Velha()
    forca = jogo_forca.Forca()
    joken = jogo_joken.Joken()
    memoria = jogo_memoria.Memoria()
    sys.exit(aplicacao.exec())
