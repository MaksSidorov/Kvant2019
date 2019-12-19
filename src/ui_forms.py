import sys
import sqlite3
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import datetime

conn = sqlite3.connect('regtab.db')
c = conn.cursor()


# Форма главного окна
class MainWindowUI(QMainWindow):
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
        self.entbtn = QPushButton('', self)
        self.entbtn.resize(720, 100)
        self.entbtn.move(600, 590)
        self.entbtn.setIcon(QIcon('images/other/singWinbtn.jpg'))
        self.entbtn.setIconSize(QSize(720, 110))
        self.regbtn = QPushButton('', self)
        self.regbtn.resize(720, 100)
        self.regbtn.move(600, 710)
        self.regbtn.setIcon(QIcon('images/other/regbtn.jpg'))
        self.regbtn.setIconSize(QSize(720, 110))


# Форма для входа
class EntFormUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1920, 980)
        self.setWindowTitle('Психоэмоциональный тренажер')
        oImage = QImage("images/other/singWin.jpg")
        sImage = oImage.scaled(QSize(1920, 980))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)
        font = QtGui.QFont("Times", 15, QtGui.QFont.Bold)
        self.login = QLineEdit(self)
        self.login.setStyleSheet("QLineEdit { background-color : rgb(191,209,231); color : yellow; }")
        self.login.move(910, 255)
        self.login.resize(630, 60)
        self.login.setFont(font)
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet("QLineEdit { background-color : rgb(191,209,231); color : yellow; }")
        self.password.move(910, 395)
        self.password.resize(630, 60)
        self.password.setFont(font)
        self.btn = QPushButton("", self)
        self.btn.resize(850, 120)
        self.btn.move(670, 645)
        self.btn.setIcon(QIcon('images/other/singWinbtn.jpg'))
        self.btn.setIconSize(QSize(850, 140))


class RegFormUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1920, 980)
        self.setWindowTitle('Психоэмоциональный тренажер')
        oImage = QImage("images/other/regwinimg.jpg")
        sImage = oImage.scaled(QSize(1920, 980))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)
        self.btn = QPushButton("", self)
        self.btn.setIcon(QIcon('images/other/regbtn.jpg'))
        self.btn.setIconSize(QSize(950, 120))
        self.btn.move(650, 828)
        self.btn.resize(850, 110)
        self.name = QLineEdit(self)
        self.name.setStyleSheet("QLineEdit { background-color : rgb(191,209,231); color : yellow; }")
        self.name.move(900, 242)
        self.name.resize(630, 60)
        font = QtGui.QFont("Times", 15, QtGui.QFont.Bold)
        self.name.setFont(font)
        self.age = QLineEdit(self)
        self.age.setStyleSheet("QLineEdit { background-color : rgb(191,209,231); color : yellow; }")
        self.age.move(900, 340)
        self.age.resize(630, 60)
        self.age.setFont(font)
        self.login = QLineEdit(self)
        self.login.setStyleSheet("QLineEdit { background-color : rgb(191,209,231); color : yellow; }")
        self.login.move(900, 437)
        self.login.resize(630, 60)
        self.login.setFont(font)
        self.password = QLineEdit(self)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setStyleSheet("QLineEdit { background-color : rgb(191,209,231); color : yellow; }")
        self.password.move(900, 547)
        self.password.resize(630, 60)
        self.password.setFont(font)
        self.malebtn = QPushButton("", self)
        self.femalebtn = QPushButton("", self)
        self.femalebtn.resize(155, 155)
        self.malebtn.resize(155, 155)
        self.femalebtn.move(1230, 640)
        self.malebtn.move(1020, 640)
        self.female = False
        self.male = False
        self.femalebtn.setIcon(QIcon('images/other/female.jpg'))
        self.femalebtn.setIconSize(QSize(155, 155))
        self.malebtn.setIcon(QIcon('images/other/male.jpg'))
        self.malebtn.setIconSize(QSize(155, 155))


# Меню
class MainMenuUI(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.args = list(args)
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1920, 980)
        oImage = QImage("images/other/Win1.0.jpg")
        sImage = oImage.scaled(QSize(1920, 980))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)
        self.btn1 = QPushButton("", self)
        self.btn1.resize(480, 130)
        self.btn1.move(690, 260)
        self.btn1.setIcon(QIcon('images/other/Win1btn1.jpg'))
        self.btn1.setIconSize(QSize(480, 160))
        self.btn2 = QPushButton("", self)
        self.btn2.resize(750, 130)
        self.btn2.move(690, 480)
        self.btn2.setIcon(QIcon('images/other/Win1btn2.jpg'))
        self.btn2.setIconSize(QSize(755, 200))
        self.btn3 = QPushButton("", self)
        self.btn3.resize(800, 130)
        self.btn3.move(690, 690)
        self.btn3.setIcon(QIcon('images/other/Win1btn3.jpg'))
        self.btn3.setIconSize(QSize(800, 160))


class WarmUI(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.args = list(args)
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1920, 980)
        oImage = QImage('images/warm/Raz' + str(self.args[2]) + '.jpg')
        sImage = oImage.scaled(QSize(1920, 980))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)
        self.btn = QPushButton("", self)
        self.btn.move(1700, 800)
        self.btn.resize(200, 200)
        self.btn.setIcon(QIcon('images/other/warmbtn.jpg'))
        self.btn.setIconSize(QSize(230, 230))


class ExUI(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.args = list(args)
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1920, 980)
        oImage = QImage("images/Ex/" + str(self.args[2]) + ".jpg")
        sImage = oImage.scaled(QSize(1920, 980))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)
        self.dimensions = (900, 585)
        scene = QGraphicsScene(self)
        pixmap = QPixmap(*self.dimensions)
        self.pixmapItem = scene.addPixmap(pixmap)
        self.btn = QPushButton("Начать", self)
        self.btn.move(1400, 920)
        self.btn.resize(200, 50)
        self.nbtn = QPushButton("След", self)
        self.nbtn.move(1700, 920)
        self.nbtn.resize(200, 50)
        self.nbtn.setEnabled(False)

        view = QGraphicsView(self)
        view.setScene(scene)
        view.resize(910, 595)
        view.move(110, 335)
        if self.args[2] < 2:
            self.num1 = QLabel('0    ', self)
            self.num1.setFont(QtGui.QFont('SansSerif', 25))
            pal = self.num1.palette()
            pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("yellow"))
            self.num1.setPalette(pal)
            self.num1.move(400, 250)
            self.flag1 = True
            self.c1 = 0
        else:
            self.num1 = QLabel('0    ', self)
            self.num2 = QLabel('0    ', self)
            self.label1 = QLabel('Левый', self)
            self.label2 = QLabel('Правый', self)
            self.label1.move(400, 200)
            self.label2.move(550, 200)
            self.label1.setFont(QtGui.QFont('SansSerif', 25))
            self.label2.setFont(QtGui.QFont('SansSerif', 25))
            self.num1.setFont(QtGui.QFont('SansSerif', 25))
            pal = self.num1.palette()
            pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("yellow"))
            self.num1.setPalette(pal)
            self.num2.setFont(QtGui.QFont('SansSerif', 25))
            pal = self.num2.palette()
            pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("yellow"))
            self.num2.setPalette(pal)
            self.num1.move(400, 250)
            self.num2.move(550, 250)
            self.flag1 = True
            self.c1 = 0
            self.flag2 = True
            self.c2 = 0


class FinalUI(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.args = list(args)
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1920, 980)
        oImage = QImage("images/Final/" + str(self.args[2]) + ".jpg")
        sImage = oImage.scaled(QSize(1920, 980))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)
        self.dimensions = (900, 585)
        scene = QGraphicsScene(self)
        pixmap = QPixmap(*self.dimensions)
        self.pixmapItem = scene.addPixmap(pixmap)
        self.btn = QPushButton("Начать", self)
        self.btn.move(1700, 720)
        self.btn.resize(200, 75)
        self.nbtn = QPushButton("След", self)
        self.nbtn.move(1700, 820)
        self.nbtn.resize(200, 75)
        self.nbtn.setEnabled(False)

        view = QGraphicsView(self)
        view.setScene(scene)
        view.resize(910, 595)
        view.move(400, 335)


class TableUI(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.args = list(args)
        self.inform = []
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1920, 980)
        oImage = QImage("images/other/table.jpg")
        sImage = oImage.scaled(QSize(1920, 980))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)
        c.execute(
            "INSERT INTO inf (login, dataa, o1, o2, o3, o4, o5, o6, o7, o8, happy, angry, sad, fear, surprised, disgust) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (
            self.args[0], datetime.date.today(), *self.args[3]))
        conn.commit()
        c.execute('SELECT * FROM inf WHERE login = "{}"'.format(self.args[0]))
        row = c.fetchone()
        while row is not None:
            self.inform.append(list(row)[2:])
            row = c.fetchone()
        self.tableWidget = QTableWidget(self)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setRowCount(len(self.inform))
        self.tableWidget.setColumnCount(15)
        self.tableWidget.move(50, 100)
        self.tableWidget.resize(1800, 800)
        self.tableWidget.setHorizontalHeaderLabels(
            ('дата', 'Упражнение № 1', 'Упражнение № 2', 'Упражнение № 3(Левый глаз)', 'Упражнение № 3(Правый глаз)',
             'Упражнение № 4(Левая сторона)', 'Упражнение № 4(Правая сторона)', 'Упражнение № 5(Левая сторона)',
             'Упражнение № 5(Правая сторона)', 'злость', 'отвращение', 'страх', 'радость', 'грусть', 'удивление')
        )
        self.tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        for x in range(len(self.inform)):
            for y in range(len(self.inform[0])):
                if y == 0:
                    cellinfo = QTableWidgetItem(str(self.inform[x][y]))
                    cellinfo.setFlags(
                        Qt.ItemIsSelectable | Qt.ItemIsEnabled
                    )
                    self.tableWidget.setItem(x, y, cellinfo)
                elif y > 8:
                    cellinfo = QTableWidgetItem(str(self.inform[x][y]) + '/1')
                    cellinfo.setFlags(
                        Qt.ItemIsSelectable | Qt.ItemIsEnabled
                    )
                    self.tableWidget.setItem(x, y, cellinfo)
                    if self.inform[x][y] == 1:
                        self.tableWidget.item(x, y).setBackground(QColor(0, 255, 0))
                    else:
                        self.tableWidget.item(x, y).setBackground(QColor(255, 255, 0))
                else:
                    cellinfo = QTableWidgetItem(str(self.inform[x][y]) + '/10')
                    cellinfo.setFlags(
                        Qt.ItemIsSelectable | Qt.ItemIsEnabled
                    )
                    self.tableWidget.setItem(x, y, cellinfo)
                    if self.inform[x][y] >= 10:
                        self.tableWidget.item(x, y).setBackground(QColor(0, 255, 0))
                    else:
                        self.tableWidget.item(x, y).setBackground(QColor(255, 255, 0))
        self.tableWidget.resizeColumnsToContents()
        self.btn = QPushButton('На главную', self)
        self.btn.move(1800, 920)
        self.btn.resize(100, 50)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = TableUI('dd', 'dd', 0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    prog.show()
    sys.exit(app.exec())
