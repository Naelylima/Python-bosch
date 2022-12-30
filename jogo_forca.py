import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QMovie


class Forca(QMainWindow):
    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 500

        self.movie = QMovie('forca.gif')
        self.gif = QLabel(self)
        self.gif.resize(800, 500)
        self.gif.setMovie(self.movie)
        self.gif.setScaledContents(True)
        self.movie.start()

        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)



if __name__ == "__main__":
    aplicacao = QApplication(sys.argv)
    j = Forca()
    j.show()
    sys.exit(aplicacao.exec())
