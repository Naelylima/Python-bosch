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

        self.movie = QMovie('velhaTeste.gif')
        self.gif = QLabel(self)
        self.gif.resize(800, 500)
        self.gif.setMovie(self.movie)
        self.gif.setScaledContents(True)
        self.movie.start()

        self.jogada = 'jogador1'
        self.vencedor = ''
        self.ponto_jogador1 = 0
        self.ponto_jogador2 = 0

        self.btn1 = ''
        self.btn2 = ''
        self.btn3 = ''
        self.btn4 = ''
        self.btn5 = ''
        self.btn6 = ''
        self.btn7 = ''
        self.btn8 = ''
        self.btn9 = ''

        self.jogador1 = QLabel(self)
        self.jogador1.setText(f"{self.ponto_jogador1}")
        self.jogador1.move(195, 0)
        self.jogador1.setStyleSheet('QLabel {font:a;font-size:25px;color:"white"}')
        self.jogador1.resize(600, 100)

        self.jogador2 = QLabel(self)
        self.jogador2.setText(f"{self.ponto_jogador2}")
        self.jogador2.move(442, 0)
        self.jogador2.setStyleSheet('QLabel {font:a;font-size:25px;color:"white"}')
        self.jogador2.resize(600, 100)

        self.botao1 = QPushButton(self)
        self.botao1.move(170, 140)  # distancia da esquerda- topo
        self.botao1.resize(90, 90)  # largura - altura
        self.botao1.setFlat(True)
        self.botao1.clicked.connect(lambda: self.jogadas(1))

        self.botao2 = QPushButton(self)
        self.botao2.move(170, 260)
        self.botao2.resize(90, 90)
        self.botao2.setFlat(True)
        self.botao2.clicked.connect(lambda: self.jogadas(2))

        self.botao3 = QPushButton(self)
        self.botao3.move(170, 375)
        self.botao3.resize(90, 90)
        self.botao3.setFlat(True)
        self.botao3.clicked.connect(lambda: self.jogadas(3))

        self.botao4 = QPushButton(self)
        self.botao4.move(280, 140)
        self.botao4.resize(90, 90)
        self.botao4.setFlat(True)
        self.botao4.clicked.connect(lambda: self.jogadas(4))

        self.botao5 = QPushButton(self)
        self.botao5.move(280, 260)
        self.botao5.resize(90, 90)
        self.botao5.setFlat(True)
        self.botao5.clicked.connect(lambda: self.jogadas(5))

        self.botao6 = QPushButton(self)
        self.botao6.move(280, 375)
        self.botao6.resize(90, 90)
        self.botao6.setFlat(True)
        self.botao6.clicked.connect(lambda: self.jogadas(6))

        self.botao7 = QPushButton(self)
        self.botao7.move(392, 140)
        self.botao7.resize(90, 90)
        self.botao7.setFlat(True)
        self.botao7.clicked.connect(lambda: self.jogadas(7))

        self.botao8 = QPushButton(self)
        self.botao8.move(392, 260)
        self.botao8.resize(90, 90)
        self.botao8.setFlat(True)
        self.botao8.clicked.connect(lambda: self.jogadas(8))

        self.botao9 = QPushButton(self)
        self.botao9.move(392, 375)
        self.botao9.resize(90, 90)
        self.botao9.setFlat(True)
        self.botao9.clicked.connect(lambda: self.jogadas(9))

        self.botao_reset = QPushButton(self)
        self.botao_reset.move(10, 450)
        self.botao_reset.resize(100, 40)
        self.botao_reset.setFlat(True)

        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)

    def jogadas(self, vez):
        if self.jogada == 'jogador1':
            match vez:
                case 1:
                    self.btn1 = 'Jogador1'
                    self.botao1.setStyleSheet('border-image: url(x .png)')
                    self.botao1.setEnabled(False)
                    self.jogada = 'jogador2'
                    self.verificar_vitoria()
                case 2:
                    self.btn2 = 'Jogador1'
                    self.botao2.setStyleSheet('border-image: url(x .png)')
                    self.botao2.setEnabled(False)
                    self.jogada = 'jogador2'
                    self.verificar_vitoria()
                case 3:
                    self.btn3 = 'Jogador1'
                    self.botao3.setStyleSheet('border-image: url(x .png)')
                    self.botao3.setEnabled(False)
                    self.jogada = 'jogador2'
                    self.verificar_vitoria()
                case 4:
                    self.btn4 = 'Jogador1'
                    self.botao4.setStyleSheet('border-image: url(x .png)')
                    self.botao4.setEnabled(False)
                    self.jogada = 'jogador2'
                    self.verificar_vitoria()
                case 5:
                    self.btn5 = 'Jogador1'
                    self.botao5.setStyleSheet('border-image: url(x .png)')
                    self.botao5.setEnabled(False)
                    self.jogada = 'jogador2'
                    self.verificar_vitoria()
                case 6:
                    self.btn6 = 'Jogador1'
                    self.botao6.setStyleSheet('border-image: url(x .png)')
                    self.botao6.setEnabled(False)
                    self.jogada = 'jogador2'
                    self.verificar_vitoria()
                case 7:
                    self.btn7 = 'Jogador1'
                    self.botao7.setStyleSheet('border-image: url(x .png)')
                    self.botao7.setEnabled(False)
                    self.jogada = 'jogador2'
                    self.verificar_vitoria()
                case 8:
                    self.btn8 = 'Jogador1'
                    self.botao8.setStyleSheet('border-image: url(x .png)')
                    self.botao8.setEnabled(False)
                    self.jogada = 'jogador2'
                    self.verificar_vitoria()
                case 9:
                    self.btn9 = 'Jogador1'
                    self.botao9.setStyleSheet('border-image: url(x .png)')
                    self.botao9.setEnabled(False)
                    self.jogada = 'jogador2'
                    self.verificar_vitoria()

        elif self.jogada == 'jogador2':
            match vez:
                case 1:
                    self.btn1 = 'Jogador2'
                    self.botao1.setStyleSheet('border-image: url(circulo.png)')
                    self.botao1.setEnabled(False)
                    self.jogada = 'jogador1'
                    self.verificar_vitoria()
                case 2:
                    self.btn2 = 'Jogador2'
                    self.botao2.setStyleSheet('border-image: url(circulo.png)')
                    self.botao2.setEnabled(False)
                    self.jogada = 'jogador1'
                    self.verificar_vitoria()
                case 3:
                    self.btn3 = 'Jogador2'
                    self.botao3.setStyleSheet('border-image: url(circulo.png)')
                    self.botao3.setEnabled(False)
                    self.jogada = 'jogador1'
                    self.verificar_vitoria()
                case 4:
                    self.btn2 = 'Jogador2'
                    self.botao4.setStyleSheet('border-image: url(circulo.png)')
                    self.botao4.setEnabled(False)
                    self.jogada = 'jogador1'
                    self.verificar_vitoria()
                case 5:
                    self.btn5 = 'Jogador2'
                    self.botao5.setStyleSheet('border-image: url(circulo.png)')
                    self.botao5.setEnabled(False)
                    self.jogada = 'jogador1'
                    self.verificar_vitoria()
                case 6:
                    self.btn6 = 'Jogador2'
                    self.botao6.setStyleSheet('border-image: url(circulo.png)')
                    self.botao6.setEnabled(False)
                    self.jogada = 'jogador1'
                    self.verificar_vitoria()

                case 7:
                    self.btn7 = 'Jogador2'
                    self.botao7.setStyleSheet('border-image: url(circulo.png)')
                    self.botao7.setEnabled(False)
                    self.jogada = 'jogador1'
                    self.verificar_vitoria()

                case 8:
                    self.btn8 = 'Jogador2'
                    self.botao8.setStyleSheet('border-image: url(circulo.png)')
                    self.botao8.setEnabled(False)
                    self.jogada = 'jogador1'
                    self.verificar_vitoria()

                case 9:
                    self.btn9 = 'Jogador2'
                    self.botao9.setStyleSheet('border-image: url(circulo.png)')
                    self.botao9.setEnabled(False)
                    self.jogada = 'jogador1'
                    self.verificar_vitoria()

    def verificar_vitoria(self):
        if self.btn1 == 'Jogador1' and self.btn2 == 'Jogador1' and self.btn3 == 'Jogador1':
            print('jogador1 venceu')
            self.vencedor = 'jogador1'
            self.ponto_jogador1 += 1
            self.jogador1.setText(f"{self.ponto_jogador1}")
            self.desativar_botoes()
            # self.__init__()

        elif self.btn4 == 'Jogador1' and self.btn5 == 'Jogador1' and self.btn6 == 'Jogador1':
            print('jogador1 venceu')
            self.vencedor = 'jogador1'
            self.ponto_jogador1 += 1
            self.jogador1.setText(f"{self.ponto_jogador1}")
            self.desativar_botoes()

        elif self.btn7 == 'Jogador1' and self.btn8 == 'Jogador1' and self.btn9 == 'Jogador1':
            print('jogador1 venceu')
            self.vencedor = 'jogador1'
            self.ponto_jogador1 += 1
            self.jogador1.setText(f"{self.ponto_jogador1}")
            self.desativar_botoes()

        elif self.btn1 == 'Jogador1' and self.btn4 == 'Jogador1' and self.btn7 == 'Jogador1':
            print('jogador1 venceu')
            self.vencedor = 'jogador1'
            self.ponto_jogador1 += 1
            self.jogador1.setText(f"{self.ponto_jogador1}")
            self.desativar_botoes()

        elif self.btn2 == 'Jogador1' and self.btn5 == 'Jogador1' and self.btn8 == 'Jogador1':
            print('jogador1 venceu')
            self.vencedor = 'jogador1'
            self.ponto_jogador1 += 1
            self.jogador1.setText(f"{self.ponto_jogador1}")
            self.desativar_botoes()
        elif self.btn3 == 'Jogador1' and self.btn6 == 'Jogador1' and self.btn9 == 'Jogador1':
            print('jogador1 venceu')
            self.vencedor = 'jogador1'
            self.ponto_jogador1 += 1
            self.jogador1.setText(f"{self.ponto_jogador1}")
            self.desativar_botoes()

        elif self.btn1 == 'Jogador1' and self.btn5 == 'Jogador1' and self.btn9 == 'Jogador1':
            print('jogador1 venceu')
            self.vencedor = 'jogador1'
            self.ponto_jogador1 += 1
            self.jogador1.setText(f"{self.ponto_jogador1}")
            self.desativar_botoes()

        elif self.btn7 == 'Jogador1' and self.btn5 == 'Jogador1' and self.btn3 == 'Jogador1':
            print('jogador1 venceu')
            self.vencedor = 'jogador1'
            self.ponto_jogador1 += 1
            self.jogador1.setText(f"{self.ponto_jogador1}")
            self.desativar_botoes()

        # JOGADOR2
        elif self.btn1 == 'Jogador2' and self.btn2 == 'Jogador2' and self.btn3 == 'Jogador2':
            print('jogador2 venceu')
            self.vencedor = 'jogador2'
            self.ponto_jogador2 += 1
            self.jogador2.setText(f"{self.ponto_jogador2}")
            self.desativar_botoes()

        elif self.btn4 == 'Jogador2' and self.btn5 == 'Jogador2' and self.btn6 == 'Jogador2':
            print('jogador2 venceu')
            self.vencedor = 'jogador2'
            self.ponto_jogador2 += 1
            self.jogador2.setText(f"{self.ponto_jogador2}")
            self.desativar_botoes()

        elif self.btn7 == 'Jogador2' and self.btn8 == 'Jogador2' and self.btn9 == 'Jogador2':
            print('jogador2 venceu')
            self.vencedor = 'jogador2'
            self.ponto_jogador2 += 1
            self.jogador2.setText(f"{self.ponto_jogador2}")
            self.desativar_botoes()

        elif self.btn1 == 'Jogador2' and self.btn4 == 'Jogador2' and self.btn7 == 'Jogador2':
            print('jogador2 venceu')
            self.vencedor = 'jogador2'
            self.ponto_jogador2 += 1
            self.jogador2.setText(f"{self.ponto_jogador2}")
            self.desativar_botoes()

        elif self.btn2 == 'Jogador2' and self.btn5 == 'Jogador2' and self.btn8 == 'Jogador2':
            print('jogador2 venceu')
            self.vencedor = 'jogador2'
            self.ponto_jogador2 += 1
            self.jogador2.setText(f"{self.ponto_jogador2}")
            self.desativar_botoes()

        elif self.btn3 == 'Jogador2' and self.btn6 == 'Jogador2' and self.btn9 == 'Jogador2':
            print('jogador2 venceu')
            self.vencedor = 'jogador2'
            self.ponto_jogador2 += 1
            self.jogador2.setText(f"{self.ponto_jogador2}")
            self.desativar_botoes()

        elif self.btn1 == 'Jogador2' and self.btn5 == 'Jogador2' and self.btn9 == 'Jogador2':
            print('jogador2 venceu')
            self.vencedor = 'jogador2'
            self.ponto_jogador2 += 1
            self.jogador2.setText(f"{self.ponto_jogador2}")
            self.desativar_botoes()

        elif self.btn7 == 'Jogador2' and self.btn5 == 'Jogador2' and self.btn3 == 'Jogador2':
            print('jogador2 venceu')
            self.vencedor = 'jogador2'
            self.ponto_jogador2 += 1
            self.jogador2.setText(f"{self.ponto_jogador2}")
            self.desativar_botoes()
        else:
            if self.btn1 != '' and self.btn2 != '' and self.btn3 != '' and self.btn4 != '' and self.btn5 != '' and self.btn6 != '' and self.btn7 != '' and self.btn8 != '' and self.btn9 != '':
                print('deu velha')
                self.jogador1.setText("Deu velha!")

    def desativar_botoes(self):
        if self.vencedor == 'jogador1' or self.vencedor == 'jogador2':
            self.botao1.setEnabled(False)
            self.botao2.setEnabled(False)
            self.botao3.setEnabled(False)
            self.botao4.setEnabled(False)
            self.botao5.setEnabled(False)
            self.botao6.setEnabled(False)
            self.botao7.setEnabled(False)
            self.botao8.setEnabled(False)
            self.botao9.setEnabled(False)


**if __name__ == "__main__":
    aplicacao = QApplication(sys.argv)
    j = Velha()
    sys.exit(aplicacao.exec())**
