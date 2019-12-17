import sys
import sqlite3
from PyQt5 import QtGui, QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import time
import numpy as np
import cv2
import dlib
from keras.models import load_model
from functions import *
import datetime

# Функции для основной части, которые фиксируют движения
osnova = [func1, func2, [func3_2, func3_1], [func4_1, func4_2], [func5_1, func5_2]]
# загружаем нейронную сеть
model = load_model('model.h5')
# detector определяет координаты лица на изображении
detector = dlib.get_frontal_face_detector()
# predictor отмечает лицевые орентиры на обрезанном изображении лица
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# База данных с зарегистрированными пользователями
conn = sqlite3.connect('regtab.db')
c = conn.cursor()

# Список с количеством мыполнений упражнений, в начале заполняется 0
TABLE_DATA = []


face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Функция заносит пользователя в базу и создает таблицу по статистике упражнений
def add_user(name, age, login, passw, sex):
    c.execute("INSERT INTO user (login, passwors, name, age, sex) VALUES ('%s','%s','%s','%s','%s')" % (
        login, passw, name, age, sex))
    conn.commit()

# Форма для входа
class EntForm(QWidget):
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
        btn = QPushButton("", self)
        btn.resize(850, 120)
        btn.move(670, 645)
        btn.setIcon(QIcon('images/other/singWinbtn.jpg'))
        btn.setIconSize(QSize(850, 140))
        btn.clicked.connect(self.btnClicked)

    def btnClicked(self):
        if self.password.text() == '' or self.login.text() == '':
            QMessageBox.question(self, 'Оповищение', "Заполните все поля!", QMessageBox.Ok)
        else:
            c.execute('SELECT * FROM user')
            row = c.fetchone()
            logins = ''
            passw = ''
            while row is not None:
                if row[1] == self.login.text():
                    logins = row[1]
                    passw = row[2]
                row = c.fetchone()
            if logins == '':
                QMessageBox.question(self, 'Оповищение',
                                     "Нет такого пользователя", QMessageBox.Ok)
            elif passw != self.password.text():
                QMessageBox.question(self, 'Оповищение',
                                     "Неправильный пароль", QMessageBox.Ok)

            else:
                self.new_form = MainMenu(self.login.text(), self.password.text())
                self.new_form.show()
                self.close()


# Форма для регистрации пользователей
class RegForm(QWidget):
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
        btn = QPushButton("", self)
        btn.setIcon(QIcon('images/other/regbtn.jpg'))
        btn.setIconSize(QSize(950, 120))
        btn.move(650, 828)
        btn.resize(850, 110)
        btn.clicked.connect(self.btnClicked)
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
        self.femalebtn.clicked.connect(self.femalebtnClicked)
        self.malebtn.clicked.connect(self.malebtnClicked)
        self.femalebtn.setIcon(QIcon('images/other/female.jpg'))
        self.femalebtn.setIconSize(QSize(155, 155))
        self.malebtn.setIcon(QIcon('images/other/male.jpg'))
        self.malebtn.setIconSize(QSize(155, 155))

    def femalebtnClicked(self):
        self.female = True
        self.male = False
        self.malebtn.setIcon(QIcon('images/other/male.jpg'))
        self.malebtn.setIconSize(QSize(155, 155))
        self.femalebtn.setIcon(QIcon('images/other/female2.jpg'))
        self.femalebtn.setIconSize(QSize(155, 155))

    def malebtnClicked(self):
        self.male = True
        self.female = False
        self.femalebtn.setIcon(QIcon('images/other/female.jpg'))
        self.femalebtn.setIconSize(QSize(155, 155))
        self.malebtn.setIcon(QIcon('images/other/male2.jpg'))
        self.malebtn.setIconSize(QSize(155, 155))

    def btnClicked(self):
        if self.name.text() == '' or self.password.text() == '' or self.age.text() == '' or self.login.text() == '' or (
                self.female == self.male):
            QMessageBox.question(self, 'Оповищение', "Заполните все поля!", QMessageBox.Ok)
        else:
            c.execute('SELECT * FROM user')
            row = c.fetchone()
            logins = []
            while row is not None:
                logins.append(row[1])
                row = c.fetchone()
            if self.login.text() in logins:
                QMessageBox.question(self, 'Оповищение',
                                     "Этот логин уже занят! Выберете другой или войдите!", QMessageBox.Ok)
            else:
                sex = ''
                if self.female:
                    sex = 'female'
                else:
                    sex = 'male'
                add_user(self.name.text(), int(self.age.text()), self.login.text(), self.password.text(),
                         sex)
                self.new_form = EntForm()
                self.new_form.show()
                self.close()

# Меню
class MainMenu(QWidget):
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
        btn1 = QPushButton("", self)
        btn1.resize(480, 130)
        btn1.move(690, 260)
        btn1.setIcon(QIcon('images/other/Win1btn1.jpg'))
        btn1.setIconSize(QSize(480, 160))
        btn1.clicked.connect(self.btn1Clicked)
        btn2 = QPushButton("", self)
        btn2.resize(750, 130)
        btn2.move(690, 480)
        btn2.setIcon(QIcon('images/other/Win1btn2.jpg'))
        btn2.setIconSize(QSize(755, 200))
        btn2.clicked.connect(self.btn2Clicked)
        btn3 = QPushButton("", self)
        btn3.resize(800, 130)
        btn3.move(690, 690)
        btn3.setIcon(QIcon('images/other/Win1btn3.jpg'))
        btn3.setIconSize(QSize(800, 160))
        btn3.clicked.connect(self.btn3Clicked)

    def btn1Clicked(self):
        self.new_form = Warm(*self.args, 1)
        self.new_form.show()
        self.close()

    def btn2Clicked(self):
        self.new_form = Ex(*self.args, 0, [])
        self.new_form.show()
        self.close()

    def btn3Clicked(self):
        self.new_form = Final(self.args[0], self.args[1], 0, self.args[3])
        self.new_form.show()
        self.close()

# Окно разминки
class Warm(QWidget):
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
        btn = QPushButton("", self)
        btn.move(1700, 800)
        btn.resize(200, 200)
        btn.clicked.connect(self.btnClicked)
        btn.setIcon(QIcon('images/other/warmbtn.jpg'))
        btn.setIconSize(QSize(230, 230))

    def btnClicked(self):
        if self.args[2] == 9:
            self.new_form = MainMenu(*self.args[:2])
            oImage = QImage("images/other/Win1.1.jpg")
            sImage = oImage.scaled(QSize(1920, 980))  # resize Image to widgets size
            palette = QPalette()
            palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
            self.new_form.setPalette(palette)
            self.new_form.show()
            self.close()
        else:
            self.args[2] += 1
            oImage = QImage('images/Warm/Raz' + str(self.args[2]) + '.jpg')
            sImage = oImage.scaled(QSize(1920, 980))  # resize Image to widgets size
            palette = QPalette()
            palette.setBrush(10, QBrush(sImage))
            self.setPalette(palette)

# Окно с упражнениями
class Ex(QWidget):
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
        self.btn.clicked.connect(self.btnClicked)
        self.nbtn = QPushButton("След", self)
        self.nbtn.move(1700, 920)
        self.nbtn.resize(200, 50)
        self.nbtn.clicked.connect(self.nbtnClicked)
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

    def btnClicked(self):
        self.btn.setEnabled(False)
        self.capture = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.setInterval(int(10))
        self.timer.timeout.connect(self.get_frame1)
        self.timer.start()
        self.timer1 = QTimer(self)
        self.timer1.start(20000)
        self.timer1.timeout.connect(self.osnbtn1_1)

    def osnbtn1_1(self):
        self.timer1.stop()
        self.timer.stop()
        self.nbtn.setEnabled(True)

    def nbtnClicked(self):
        if self.args[2] == 4:
            self.args[3].extend([int(self.num1.text()), int(self.num2.text())])
            self.new_form = MainMenu(*self.args)
            oImage = QImage("images/other/Win1.2.jpg")
            sImage = oImage.scaled(QSize(1920, 980))  # resize Image to widgets size
            palette = QPalette()
            palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
            self.new_form.setPalette(palette)
            self.new_form.show()
            self.close()
        else:
            if self.args[2] < 2:
                self.args[3].append(int(self.num1.text()))
            else:
                self.args[3].extend([int(self.num1.text()), int(self.num2.text())])
            self.args[2] += 1
            self.new_form = Ex(*self.args)
            self.new_form.show()
            self.close()
    # Функция, обрабатывающая изображение
    def get_frame1(self):

        _, frame = self.capture.read()
        frame = cv2.resize(frame, (900, 585))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = detector(gray)
        for face in faces:
            x1 = face.left()
            y1 = face.top()
            x2 = face.right()
            y2 = face.bottom()
            landmarks = predictor(gray, face)
            if self.args[2] < 2:
                if osnova[self.args[2]](landmarks, x2, x1, y2, y1) and self.flag1:
                    self.c1 += 1
                    self.flag1 = False
                    self.num1.setText(str(self.c1))
                elif self.flag1 == False and osnova[self.args[2]](landmarks, x2, x1, y2, y1) == False:
                    self.flag1 = True
            else:
                if osnova[self.args[2]][0](landmarks, x2, x1, y2, y1) and self.flag1:
                    self.c1 += 1
                    self.flag1 = False
                    self.num1.setText(str(self.c1))
                elif self.flag1 == False and osnova[self.args[2]][0](landmarks, x2, x1, y2, y1) == False:
                    self.flag1 = True

                if osnova[self.args[2]][1](landmarks, x2, x1, y2, y1) and self.flag2:
                    self.c2 += 1
                    self.flag2 = False
                    self.num2.setText(str(self.c2))
                elif self.flag2 == False and osnova[self.args[2]][1](landmarks, x2, x1, y2, y1) == False:
                    self.flag2 = True
        frame = cv2.flip(frame, 1)
        image = QImage(frame, *self.dimensions, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(image)
        self.pixmapItem.setPixmap(pixmap)

# Форма с финальной части
class Final(QWidget):
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
        btn = QPushButton("Начать", self)
        btn.move(1700, 720)
        btn.resize(200, 75)
        btn.clicked.connect(self.btnClicked)
        self.nbtn = QPushButton("След", self)
        self.nbtn.move(1700, 820)
        self.nbtn.resize(200, 75)
        self.nbtn.clicked.connect(self.nbtnClicked)
        self.nbtn.setEnabled(False)

        view = QGraphicsView(self)
        view.setScene(scene)
        view.resize(910, 595)
        view.move(400, 335)

    def btnClicked(self):
        self.capture = cv2.VideoCapture(0)
        self.timer = QTimer(self)
        self.timer.setInterval(int(120))
        self.timer.timeout.connect(self.get_frame1)
        self.timer.start()
        self.timer1 = QTimer(self)
        self.timer1.start(20000)
        self.timer1.timeout.connect(self.finbtn1_1)

    def finbtn1_1(self):
        self.args[3].append(0)
        self.timer1.stop()
        self.timer.stop()
        self.nbtn.setEnabled(True)

    def nbtnClicked(self):
        if self.args[2] == 5:
            self.new_form1 = Table(*self.args)
            self.new_form1.show()
            self.close()
        else:
            self.args[2] += 1
            self.new_form = Final(*self.args)
            self.new_form.show()
            self.close()
    # Функция для определения эмоции
    def get_frame1(self):
        try:
            _, frame = self.capture.read()
            frame = cv2.resize(frame, (900, 585))
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray)
            for (x, y, w, h) in faces:
                imga = gray[x:x + w, y:y + h]
                imga = cv2.resize(imga, (48, 48))
                imga = np.reshape(imga, (48, 48, 1))
                em = model.predict(np.array([imga]))
                g = 6
                m = max(em[0])
                if em[0][0] == m:
                    g = 0
                elif em[0][1] == m:
                    g = 1
                elif em[0][2] == m:
                    g = 2
                elif em[0][3] == m:
                    g = 3
                elif em[0][4] == m:
                    g = 4
                elif em[0][5] == m:
                    g = 5
                elif em[0][6] == m:
                    g = 6
                if g == self.args[2]:
                    self.timer1.stop()
                    self.timer.stop()
                    self.nbtn.setEnabled(True)
                    self.args[3].append(1)
        except Exception as err:
            print(err)

        image = QImage(frame, *self.dimensions, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(image)
        self.pixmapItem.setPixmap(pixmap)

# Таблица с финальным результатом
class Table(QWidget):
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
             'Упражнение № 5(Правая сторона)','злость', 'отвращение', 'страх', 'радость', 'грусть', 'удивление')
        )
        self.tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        for x in range(len(self.inform)):
            for y in range(len(self.inform[0])):
                if y == 0:
                    cellinfo = QTableWidgetItem(str(self.inform[x][y]))
                    cellinfo.setFlags(
                        QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                    )
                    self.tableWidget.setItem(x, y, cellinfo)
                elif y > 8:
                    cellinfo = QTableWidgetItem(str(self.inform[x][y]) + '/1')
                    cellinfo.setFlags(
                        QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                    )
                    self.tableWidget.setItem(x, y, cellinfo)
                    if self.inform[x][y] == 1:
                        self.tableWidget.item(x, y).setBackground(QColor(0, 255, 0))
                    else:
                        self.tableWidget.item(x, y).setBackground(QColor(255, 255, 0))
                else:
                    cellinfo = QTableWidgetItem(str(self.inform[x][y]) + '/10')
                    cellinfo.setFlags(
                        QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                    )
                    self.tableWidget.setItem(x, y, cellinfo)
                    if self.inform[x][y] >= 10:
                        self.tableWidget.item(x, y).setBackground(QColor(0, 255, 0))
                    else:
                        self.tableWidget.item(x, y).setBackground(QColor(255, 255, 0))
        self.tableWidget.resizeColumnsToContents()
        btn = QPushButton('На главную', self)
        btn.move(1800, 920)
        btn.resize(100, 50)
        btn.clicked.connect(self.ret)

    def ret(self):
        self.new_form = MainMenu(self.args[0], self.args[1])
        self.new_form.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Table('us', 'us', 0, [1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    ex.show()
    sys.exit(app.exec())
