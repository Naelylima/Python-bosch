import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
from PyQt5 import QtGui
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import QTimer

class Janela(QMainWindow): #Herança
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = " Primeira Janela "

        botao1 = QPushButton('Ligar', self)
        botao1.move(100, 100)  # posição dentro da janela (distancia da esquerda - distancia do topo)
        botao1.resize(150, 50) # (altura - largura do botão)
        botao1.setStyleSheet('QPushButton {background-color:#46C0DC;font:bold;font-size:10px}') #PARA ESTILIZAR
        botao1.clicked.connect(self.botao1_click)

        botao2 = QPushButton('Desligado', self)
        botao2.move(300, 100)  # posição dentro da janela (distancia da esquerda - distancia do topo)
        botao2.resize(150, 50)  # (altura - largura do botão)
        botao2.setStyleSheet('QPushButton {background-color:#46C0DC;font:bold;font-size:10px}')  # PARA ESTILIZAR
        botao2.clicked.connect(self.botao2_click)

        botao_leitura = QPushButton("LEIA", self)
        botao_leitura.move(300, 410)
        botao_leitura.resize(150, 25)
        botao_leitura.clicked.connect(self.leitura)


        self.label1 = QLabel(self)
        self.label1.setText("Insira um texto")
        self.label1.move(300, 200)
        self.label1.setStyleSheet('QLabel {font:bold;font-size:20px;color:"black"}')
        self.label1.resize(300, 50)

        self.imagem = QLabel(self)
        self.imagem.move(80, 180)
        self.imagem.resize(200, 200)
        self.imagem.setScaledContents(True)

        self.imagem2 = QLabel(self)
        self.imagem2.move(80, 180)
        self.imagem2.resize(200, 200)
        self.imagem2.setScaledContents(True)

        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.move(100, 410)
        self.caixa_texto.resize(150, 25)

        self.timer = QTimer()
        self.timer.timeout.connect(self.timeout)

        self.carregar_janela()

    def carregar_janela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        # print('LIGADO')
        self.label1.setText('Ligado')
        self.label1.setStyleSheet('QLabel {font:bold;font-size:20px;color:"green"}')
        self.imagem.setPixmap(QtGui.QPixmap('sol.png'))

    def botao2_click(self):
        # print('DESLIGADO')
        self.label1.setText('Desligado')
        self.label1.setStyleSheet('QLabel {font:bold;font-size:20px;color:"red"}')
        self.imagem.setPixmap(QtGui.QPixmap('lua.png'))


    def leitura(self):
        frase = self.caixa_texto.text()
        self.label1.setText("Você digitou: "+frase)
        if self.timer.isActive() == False:
           self.timer.start(5000)

    def timeout(self):
        self.label1.setText("MUITO OBRIGADO!")

if __name__ == '__main__':
    aplicacao = QApplication(sys.argv)
    j =Janela()
    sys.exit(aplicacao.exec())

