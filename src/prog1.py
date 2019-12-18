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

conn = sqlite3.connect('regtab.db')
c = conn.cursor()


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






if __name__ == '__main__':
    app = QApplication(sys.argv)
    prog = MainWindow()
    prog.show()
    sys.exit(app.exec())
