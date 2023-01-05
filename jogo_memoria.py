import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer



class Memoria(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 500


        self.movie = QMovie('memoria1.gif')
        self.gif = QLabel(self)
        self.gif.resize(800, 500)
        self.gif.setMovie(self.movie)
        self.gif.setScaledContents(True)
        self.movie.start()

        self.timer = QTimer()
        self.timer.timeout.connect(self.timeout)

        self.chute = ''
        self.chute2 = ''
        self.click = 1
        self.teste = ''
        self.teste2 = ''
        self.pontos = 0

        self.botao1 = QPushButton(self)
        self.botao1.move(310, 65)
        self.botao1.resize(75, 75)
        self.botao1.setFlat(True)
        self.botao1.clicked.connect(lambda: self.jogadas(1))

        self.botao2 = QPushButton(self)
        self.botao2.move(425, 63)
        self.botao2.resize(75, 75)
        self.botao2.setFlat(True)
        self.botao2.clicked.connect(lambda: self.jogadas(2))

        self.botao3 = QPushButton(self)
        self.botao3.move(550, 63)
        self.botao3.resize(75, 75)
        self.botao3.setFlat(True)
        self.botao3.clicked.connect(lambda: self.jogadas(3))

        self.botao4 = QPushButton(self)
        self.botao4.move(670, 63)
        self.botao4.resize(75, 75)
        self.botao4.setFlat(True)
        self.botao4.clicked.connect(lambda: self.jogadas(4))

        self.botao5 = QPushButton(self)
        self.botao5.move(308, 200)
        self.botao5.resize(75, 75)
        self.botao5.setFlat(True)
        self.botao5.clicked.connect(lambda: self.jogadas(5))

        self.botao6 = QPushButton(self)
        self.botao6.move(425, 200)
        self.botao6.resize(75, 75)
        self.botao6.setFlat(True)
        self.botao6.clicked.connect(lambda: self.jogadas(6))

        self.botao7 = QPushButton(self)
        self.botao7.move(550, 200)
        self.botao7.resize(75, 75)
        self.botao7.setFlat(True)
        self.botao7.clicked.connect(lambda: self.jogadas(7))

        self.botao8 = QPushButton(self)
        self.botao8.move(670, 200)
        self.botao8.resize(75, 75)
        self.botao8.setFlat(True)
        self.botao8.clicked.connect(lambda: self.jogadas(8))

        self.botao9 = QPushButton(self)
        self.botao9.move(308, 335)
        self.botao9.resize(75, 75)
        self.botao9.setFlat(True)
        self.botao9.clicked.connect(lambda: self.jogadas(9))

        self.botao10 = QPushButton(self)
        self.botao10.move(425, 335)
        self.botao10.resize(75, 75)
        self.botao10.setFlat(True)
        self.botao10.clicked.connect(lambda: self.jogadas(10))

        self.botao11 = QPushButton(self)
        self.botao11.move(550, 335)
        self.botao11.resize(75, 75)
        self.botao11.setFlat(True)
        self.botao11.clicked.connect(lambda: self.jogadas(11))

        self.botao12 = QPushButton(self)
        self.botao12.move(670, 335)
        self.botao12.resize(75, 75)
        self.botao12.setFlat(True)
        self.botao12.clicked.connect(lambda: self.jogadas(12))


        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)


    def chamar_botao1(self):
        self.botao1.setStyleSheet('border-image: url(gato.png)')

    def chamar_botao2(self):
        self.botao2.setStyleSheet('border-image: url(gato (1).png)')

    def chamar_botao3(self):
        self.botao3.setStyleSheet('border-image: url(mouse.png)')

    def chamar_botao4(self):
        self.botao4.setStyleSheet('border-image: url(peixe.png)')

    def chamar_botao5(self):
        self.botao5.setStyleSheet('border-image: url(papagaio.png)')

    def chamar_botao6(self):
        self.botao6.setStyleSheet('border-image: url(porco.png)')

    def chamar_botao7(self):
        self.botao7.setStyleSheet('border-image: url(peixe.png)')

    def chamar_botao8(self):
        self.botao8.setStyleSheet('border-image: url(gato.png)')

    def chamar_botao9(self):
        self.botao9.setStyleSheet('border-image: url(gato (1).png)')

    def chamar_botao10(self):
        self.botao10.setStyleSheet('border-image: url(mouse.png)')

    def chamar_botao11(self):
        self.botao11.setStyleSheet('border-image: url(papagaio.png)')

    def chamar_botao12(self):
        self.botao12.setStyleSheet('border-image: url(porco.png)')

    def jogadas(self, vez):
        if self.click == 1:
            match vez:
                case 1:
                    self.chamar_botao1()
                    self.chute = 'gato'
                    self.teste = self.botao1
                    self.click = 2
                case 2:
                    self.chamar_botao2()
                    self.chute = 'gato1'
                    self.teste = self.botao2
                    self.click = 2
                case 3:
                    self.chamar_botao3()
                    self.chute = 'mouse'
                    self.teste = self.botao3
                    self.click = 2
                case 4:
                    self.chamar_botao4()
                    self.chute = 'peixe'
                    self.teste = self.botao4
                    self.click = 2
                case 5:
                    self.chamar_botao5()
                    self.chute = 'papagaio'
                    self.teste = self.botao5
                    self.click = 2
                case 6:
                    self.chamar_botao6()
                    self.chute = 'porco'
                    self.teste = self.botao6
                    self.click = 2
                case 7:
                    self.chamar_botao7()
                    self.chute = 'peixe'
                    self.teste = self.botao7
                    self.click = 2
                case 8:
                    self.chamar_botao8()
                    self.chute = 'gato'
                    self.teste = self.botao8
                    self.click = 2
                case 9:
                    self.chamar_botao9()
                    self.chute = 'gato1'
                    self.teste = self.botao9
                    self.click = 2
                case 10:
                    self.chamar_botao10()
                    self.chute = 'mouse'
                    self.teste = self.botao10
                    self.click = 2
                case 11:
                    self.chamar_botao11()
                    self.chute = 'papagaio'
                    self.teste = self.botao11
                    self.click = 2
                case 12:
                    self.chamar_botao12()
                    self.chute = 'porco'
                    self.teste = self.botao12
                    self.click = 2

        elif self.click == 2:
            match vez:
                case 1:
                    self.chamar_botao1()
                    self.chute2 = 'gato'
                    self.teste2 = self.botao1
                    self.verificar_vitoria()
                    self.click = 1
                case 2:
                    self.chamar_botao2()
                    self.chute2 = 'gato1'
                    self.teste2 = self.botao2
                    self.verificar_vitoria()
                    self.click = 1
                case 3:
                    self.chamar_botao3()
                    self.chute2 = 'mouse'
                    self.teste2 = self.botao3
                    self.verificar_vitoria()
                    self.click = 1
                case 4:
                    self.chamar_botao4()
                    self.chute2 = 'peixe'
                    self.teste2 = self.botao4
                    self.verificar_vitoria()
                    self.click = 1
                case 5:
                    self.chamar_botao5()
                    self.chute2 = 'papagaio'
                    self.teste2 = self.botao5
                    self.verificar_vitoria()
                    self.click = 1
                case 6:
                    self.chamar_botao6()
                    self.chute2 = 'porco'
                    self.teste2 = self.botao6
                    self.verificar_vitoria()
                    self.click = 1
                case 7:
                    self.chamar_botao7()
                    self.chute2 = 'peixe'
                    self.teste2 = self.botao7
                    self.verificar_vitoria()
                    self.click = 1
                case 8:
                    self.chamar_botao8()
                    self.chute2 = 'gato'
                    self.teste2 = self.botao8
                    self.verificar_vitoria()
                    self.click = 1
                case 9:
                    self.chamar_botao9()
                    self.chute2 = 'gato1'
                    self.teste2 = self.botao9
                    self.verificar_vitoria()
                    self.click = 1
                case 10:
                    self.chamar_botao10()
                    self.chute2 = 'mouse'
                    self.teste2 = self.botao10
                    self.verificar_vitoria()
                    self.click = 1
                case 11:
                    self.chamar_botao11()
                    self.chute2 = 'papagaio'
                    self.teste2 = self.botao11
                    self.verificar_vitoria()
                    self.click = 1
                case 12:
                    self.chamar_botao12()
                    self.chute2 = 'porco'
                    self.teste2 = self.botao12
                    self.verificar_vitoria()
                    self.click = 1



    def verificar_vitoria(self):
        if self.chute == self.chute2:
            print('ganhou')
            if self.teste == self.botao1 or self.teste == self.botao2 or self.teste == self.botao3 or self.teste == self.botao4 or self.teste == self.botao5 or self.teste == self.botao6 or self.teste == self.botao7 or self.teste == self.botao8 or self.teste == self.botao9 or self.teste == self.botao10 or self.teste == self.botao11 or self.teste == self.botao12 and self.teste2 == self.botao1 or self.teste2 == self.botao2 or self.teste2 == self.botao3 or self.teste2 == self.botao4 or self.teste2 == self.botao5 or self.teste2 == self.botao6 or self.teste2 == self.botao7 or self.teste2 == self.botao8 or self.teste2 == self.botao9 or self.teste2 == self.botao10 or self.teste2 == self.botao11 or self.teste2 == self.botao12:
                self.teste.setEnabled(False)
                self.teste2.setEnabled(False)

                self.teste = ''
                self.teste2 = ''
                self.chute = ''
                self.chute2 = ''
                self.click = 1
                self.pontos += 1
                self.timer.stop()
                print(self.pontos)
                if self.pontos == 6:
                    print('obaa')

        else:
            print('perdeu')

            if self.timer.isActive() == False:
                self.timer.start(400)


    def timeout(self):
        if self.teste == self.botao1 or self.teste == self.botao2 or self.teste == self.botao3 or self.teste == self.botao4 or self.teste == self.botao5 or self.teste == self.botao6 or self.teste == self.botao7 or self.teste == self.botao8 or self.teste == self.botao9 or self.teste == self.botao10 or self.teste == self.botao11 or self.teste == self.botao12 and self.teste2 == self.botao1 or self.teste2 == self.botao2 or self.teste2 == self.botao3 or self.teste2 == self.botao4 or self.teste2 == self.botao5 or self.teste2 == self.botao6 or self.teste2 == self.botao7 or self.teste2 == self.botao8 or self.teste2 == self.botao9 or self.teste2 == self.botao10 or self.teste2 == self.botao11 or self.teste2 == self.botao12 :
            self.teste.setStyleSheet('border-image: url('')')
            self.teste2.setStyleSheet('border-image: url('')')

            self.chute = ''
            self.chute2 = ''

            self.teste = ''
            self.teste2 = ''

            self.click = 1
            self.timer.stop()


if __name__ == "__main__":
    aplicacao = QApplication(sys.argv)
    j = Memoria()
    # aplicacao.setStyleSheet()
    # j.show()
    sys.exit(aplicacao.exec())
