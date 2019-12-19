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
from ui_forms import *
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

conn = sqlite3.connect('regtab.db')
c = conn.cursor()

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def add_user(name, age, login, passw, sex):
    c.execute("INSERT INTO user (login, passwors, name, age, sex) VALUES ('%s','%s','%s','%s','%s')" % (
        login, passw, name, age, sex))
    conn.commit()


# Главное окно
class MainWindow(MainWindowUI):
    def __init__(self):
        super().__init__()
        self.entbtn.clicked.connect(self.ent_func)
        self.regbtn.clicked.connect(self.reg_func)

    def ent_func(self):
        self.EntForm = EntForm()
        self.EntForm.show()
        self.close()

    def reg_func(self):
        self.RegForm = RegForm()
        self.RegForm.show()
        self.close()


# Вход
class EntForm(EntFormUI):
    def __init__(self):
        super().__init__()
        self.btn.clicked.connect(self.btnClicked)

    def btnClicked(self):
        if self.password.text() == '' or self.login.text() == '':
            QMessageBox.question(self, 'Оповищение', "Заполните все поля!", QMessageBox.Ok)
        else:
            res = c.execute('SELECT * FROM user WHERE login = "{}"'.format(self.login.text())).fetchone()
            if len(res) == 0:
                QMessageBox.question(self, 'Оповищение',
                                     "Нет такого пользователя", QMessageBox.Ok)
            elif res[2] != self.password.text():
                QMessageBox.question(self, 'Оповищение',
                                     "Неправильный пароль", QMessageBox.Ok)

            else:
                self.new_form = MainMenu(self.login.text(), self.password.text())
                self.new_form.show()
                self.close()

class RegForm(RegFormUI):
    def __init__(self):
        super().__init__()
        self.btn.clicked.connect(self.btnClicked)
        self.femalebtn.clicked.connect(self.femalebtnClicked)
        self.malebtn.clicked.connect(self.malebtnClicked)

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
            res = c.execute('SELECT * FROM user WHERE login = "{}"'.format(self.login.text())).fetchone()
            if res:
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

class MainMenu(MainMenuUI):
    def __init__(self, *args):
        super().__init__()
        self.args = list(args)
        self.btn3.clicked.connect(self.btn3Clicked)
        self.btn1.clicked.connect(self.btn1Clicked)
        self.btn2.clicked.connect(self.btn2Clicked)

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

class Warm(WarmUI):
    def __init__(self, *args):
        self.args = list(args)
        super().__init__(*self.args)
        self.btn.clicked.connect(self.btnClicked)

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


class Ex(ExUI):
    def __init__(self, *args):
        self.args = list(args)
        super().__init__(*self.args)
        self.btn.clicked.connect(self.btnClicked)
        self.nbtn.clicked.connect(self.nbtnClicked)

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

class Final(FinalUI):
    def __init__(self, *args):
        self.args = list(args)
        super().__init__(*self.args)
        self.initUI()
        self.btn.clicked.connect(self.btnClicked)
        self.nbtn.clicked.connect(self.nbtnClicked)

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


class Table(TableUI):
    def __init__(self, *args):
        self.args = list(args)
        super().__init__(*self.args)
        self.inform = []
        self.btn.clicked.connect(self.ret)

    def ret(self):
        self.new_form = MainMenu(self.args[0], self.args[1])
        self.new_form.show()
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = MainWindow()
    prog.show()
    sys.exit(app.exec())
