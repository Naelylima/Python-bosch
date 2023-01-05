import random
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5 import QtGui
from PyQt5.QtGui import QMovie


class Joken(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 500

        self.ponto_usuario = 0
        self.ponto_computador = 0
        self.opcao_computador = ''
        self.opcao_usuario = ''
        self.resultado = ''

        self.movie = QMovie('joken.gif')
        self.gif = QLabel(self)
        self.gif.resize(800, 500)
        self.gif.setMovie(self.movie)
        self.gif.setScaledContents(True)
        self.movie.start()

        self.computador = QLabel(self)
        self.computador.setText(f"{self.ponto_computador}")
        self.computador.move(255, -15)
        self.computador.setStyleSheet('QLabel {font:a;font-size:25px;color:"white"}')
        self.computador.resize(600, 100)

        self.jogador = QLabel(self)
        self.jogador.setText(f"{self.ponto_usuario}")
        self.jogador.move(650, -15)
        self.jogador.setStyleSheet('QLabel {font:a;font-size:25px;color:"white"}')
        self.jogador.resize(600, 100)

        self.imagem = QLabel(self)
        self.imagem.move(190, 200)
        self.imagem.resize(100, 100)
        self.imagem.setScaledContents(True)

        self.imagemDireita = QLabel(self)
        self.imagemDireita.move(500, 200)
        self.imagemDireita.resize(100, 100)
        self.imagemDireita.setScaledContents(True)

        self.botao_pedra = QPushButton(self)
        self.botao_pedra.move(20, 35)
        self.botao_pedra.resize(100, 100)
        self.botao_pedra.setFlat(True)
        self.botao_pedra.clicked.connect(self.botao_pedraF)
        self.botao_pedra.clicked.connect(self.sorteador)

        self.botao_papel = QPushButton(self)
        self.botao_papel.move(20, 170)
        self.botao_papel.resize(100, 120)
        self.botao_papel.setFlat(True)
        self.botao_papel.clicked.connect(self.botao_papelF)
        self.botao_papel.clicked.connect(self.sorteador)

        self.botao_tesoura = QPushButton(self)
        self.botao_tesoura.move(20, 320)
        self.botao_tesoura.resize(100, 100)
        self.botao_tesoura.setFlat(True)
        self.botao_tesoura.clicked.connect(self.botao_tesouraF)
        self.botao_tesoura.clicked.connect(self.sorteador)

        self.botao_reset = QPushButton(self)
        self.botao_reset.move(680, 15)
        self.botao_reset.resize(100, 40)
        self.botao_reset.setFlat(True)
        self.botao_reset.clicked.connect(self.reset)

        self.resultado = QLabel(self)
        self.resultado.setText("")
        self.resultado.move(310, 250)
        self.resultado.setStyleSheet('QLabel {font:bold;font-size:20px;color:"white";align-text: center;}')
        self.resultado.resize(300, 200)

        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)

    def botao_pedraF(self):
        self.imagemDireita.setPixmap(QtGui.QPixmap('pedra.png'))
        self.opcao_usuario = 'pedra'

    def botao_papelF(self):
        self.imagemDireita.setPixmap(QtGui.QPixmap('papel.png'))
        self.opcao_usuario = 'papel'
        # self.opcao_user.setText('Papel')

    def botao_tesouraF(self):
        self.imagemDireita.setPixmap(QtGui.QPixmap('tesoura.png'))
        self.opcao_usuario = 'tesoura'
        # self.opcao_user.setText('Tesoura')

    def sorteador(self):

        lista_escolha = ['pedra', 'papel', 'tesoura']
        self.opcao_computador = random.choice(lista_escolha)

        if self.opcao_computador == 'pedra':
            self.imagem.setPixmap(QtGui.QPixmap('pedra.png'))
            self.verificacao()

        elif self.opcao_computador == 'papel':
            self.imagem.setPixmap(QtGui.QPixmap('papel.png'))
            self.verificacao()
        else:
            self.imagem.setPixmap(QtGui.QPixmap('tesoura.png'))
            self.verificacao()

    def verificacao(self):
        print(f'usuario: {self.opcao_usuario}, computador:{self.opcao_computador} ')

        if self.opcao_computador == self.opcao_usuario:
            self.resultado.setText('  Deu empate')
            print('empate')

        if self.opcao_usuario == 'tesoura' and self.opcao_computador == 'papel':
            self.ponto_usuario += 1
            self.jogador.setText(f"{self.ponto_usuario}")
            self.resultado.setText('Usuario venceu!')

        elif self.opcao_usuario == 'papel' and self.opcao_computador == 'pedra':
            self.ponto_usuario += 1
            self.jogador.setText(f"{self.ponto_usuario}")
            self.resultado.setText('Usuario venceu!')

        elif self.opcao_usuario == 'pedra' and self.opcao_computador == 'tesoura':
            self.ponto_usuario += 1
            self.jogador.setText(f"{self.ponto_usuario}")
            self.resultado.setText('Usuario venceu!')

        # Computador
        elif self.opcao_computador == 'tesoura' and self.opcao_usuario == 'papel':
            self.ponto_computador += 1
            self.computador.setText(f"{self.ponto_computador}")
            self.resultado.setText('Computador  venceu!')

        elif self.opcao_computador == 'papel' and self.opcao_usuario == 'pedra':
            self.ponto_computador += 1
            self.computador.setText(f"{self.ponto_computador}")
            self.resultado.setText('Computador venceu!')

        elif self.opcao_computador == 'pedra' and self.opcao_usuario == 'tesoura':
            self.ponto_computador += 1
            self.computador.setText(f"{self.ponto_computador}")
            self.resultado.setText('Computador venceu!')

    def reset(self):
        self.resultado.setText('')
        self.ponto_usuario = 0
        self.ponto_computador = 0
        self.opcao_computador = ''
        self.opcao_usuario = ''
        self.resultado = ''
        self.computador.setText(f"{self.ponto_computador}")
        self.jogador.setText(f"{self.ponto_usuario}")
        self.imagem.setPixmap(QtGui.QPixmap(''))
        self.imagemDireita.setPixmap(QtGui.QPixmap(''))



    if __name__ == "__main__":
        aplicacao = QApplication(sys.argv)
        # j = Joken()
        # j.show()
        sys.exit(aplicacao.exec())
