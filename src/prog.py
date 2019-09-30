import sys
import sqlite3
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore    import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from classes import *


# Главное окно, с которого пользователь может войти или зарегестрироваться
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setGeometry(0, 0, 1920, 980)
        self.setWindowTitle('Психоэмоциональный тренажер')
        oImage = QImage('images/other/thefirstwin.jpg')
        sImage = oImage.scaled(QSize(1920, 980))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)
        btn1 = QPushButton('', self)
        btn1.resize(720, 100)
        btn1.move(600, 590)
        btn1.clicked.connect(self.entbtn)
        btn1.setIcon(QIcon('images/other/singWinbtn.jpg'))
        btn1.setIconSize(QSize(720, 110))
        btn2 = QPushButton('', self)
        btn2.resize(720, 100)
        btn2.move(600, 710)
        btn2.clicked.connect(self.regbtn)
        btn2.setIcon(QIcon('images/other/regbtn.jpg'))
        btn2.setIconSize(QSize(720, 110))

    def entbtn(self):
        self.EntForm = EntForm()
        self.EntForm.show()
        self.close()

    def regbtn(self):
        self.RegForm = RegForm()
        self.RegForm.show()
        self.close()





if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = MainWindow()
    prog.show()
    sys.exit(app.exec())
