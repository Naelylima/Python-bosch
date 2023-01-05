import random
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QMovie
# from PyQt5.QtWidgets import QLineEdit


class Forca(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 500

        self.movie = QMovie('forcaTeste.gif')
        self.gif = QLabel(self)
        self.gif.resize(800, 500)
        self.gif.setMovie(self.movie)
        self.gif.setScaledContents(True)
        self.movie.start()

        self.mostrar_palavra = QLabel(self)
        self.mostrar_palavra.setText('')
        self.mostrar_palavra.move(300, 220)
        self.mostrar_palavra.setStyleSheet('QLabel {font:arial;font-size:30px;color:"dark pink";background: "pink"}')
        self.mostrar_palavra.resize(200, 20)

        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.move(250, 400)
        self.caixa_texto.resize(300, 25)

        self.botao_leitura = QPushButton(self)
        self.botao_leitura.move(560, 388)
        self.botao_leitura.resize(33, 30)
        self.botao_leitura.setFlat(True)
        self.botao_leitura.clicked.connect(self.leitura)

        self.botao_reset = QPushButton(self)
        self.botao_reset.move(695, 15)
        self.botao_reset.resize(90, 40)
        self.botao_reset.setFlat(True)

        self.botao_iniciar = QPushButton("iniciar",self)
        self.botao_iniciar.move(695, 55)
        self.botao_iniciar.resize(90, 40)
        self.botao_iniciar.setFlat(False)
        self.botao_iniciar.clicked.connect(self.jogo_forca)

        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)

    def leitura(self):
        texto = self.caixa_texto.text()
        self.letra = texto
        print(self.letra)
        self.caixa_texto.setText("")
        # self.chutes.setText(texto)

    def jogo_forca(self):
        self.chances = 6
        self.palavras_lista = ["BOSCH", "ETS", "JOVEM", "SMART", "PYTHON"]
        self.dicas = ["Empresa", "Setor aprendiz", "Aprendiz", "Curso dentro da BOSCH", "Linguagem de programação"]

        self.palavra_aleatoria = random.choice(self.palavras_lista)
        self.palavra_certa = []

        for i in range(len(self.palavra_aleatoria)):
            self.palavra_certa.append(('-'))
        self.erros = []
        teste = ("-  " * len(self.palavra_aleatoria))
        self.mostrar_palavra.setText(teste)

        while True:
            for j in range(len(self.palavras_lista)):
                if self.palavra_aleatoria == self.palavras_lista[j]:
                    print(f"\nA dica é: {self.dicas[j]}")

            # self.letra.upper().replace(" ", "")


if __name__ == "__main__":
    aplicacao = QApplication(sys.argv)
    j = Forca()
    j.show()
    sys.exit(aplicacao.exec())

