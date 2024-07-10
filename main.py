import sys
from random import randint

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QMainWindow,
    QLabel,
    QWidget
)


class Label(QLabel):
    clicked = pyqtSignal()
    clicked2 = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__()
        QLabel.__init__(self, parent=parent)

    def mousePressEvent(self, e):
        self.clicked.emit()

    def mouseReleaseEvent(self, e):
        self.clicked2.emit()


class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Hello World % d" % randint(0, 100))
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setGeometry(1500, 500, 301, 300)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.window1 = AnotherWindow()
        self.window2 = AnotherWindow()
        #self.setGeometry(1481, 857, 301, 172)
        
        self.setGeometry(1000, 400, 1000, 700)

        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        self.Sweet = QtWidgets.QWidget(self)
        self.Sweet.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.Sweet)
        self.label.setGeometry(450, 455, 301, 172)
        #self.label.setAlignment(Qt.AlignVCenter | Qt.AlignBottom)
        #self.label.setGeometry((1920 - wid - 450), (1080 - hig - 50), 301, 172)
        #self.label.setGeometry(QtCore.QRect(0, 0, 301, 172))
        self.label.setObjectName("label")

        self.setCentralWidget(self.Sweet)

        self.movie = QMovie("media/sweetiebot_anim.gif")
        self.label.setMovie(self.movie)
        self.movie.start()


        self.btn_1 = Label(parent=self.label)
        self.btn_1.setGeometry(10, 10, 150, 100)

        self.btn_2 = Label(parent=self.label)
        self.btn_2.setGeometry(100, 100, 150, 100)

        self.btn_close = Label(parent=self.label)
        self.btn_close.setGeometry(200, 20, 40, 40)
        self.pixmap = QPixmap('media/123.svg')
        self.btn_close.setPixmap(self.pixmap)

        self.dialog = QLabel(parent=self.Sweet)
        self.dialog.setGeometry(100, 350, 400, 400)
        self.dialog.setPixmap(QPixmap('media/window_dial2.svg'))
        self.dialog.hide()

        self.btn_close.clicked.connect(self.close)
        #self.btn_2.clicked.connect(self.toggle_window2)
        self.btn_2.clicked.connect(self.dial1)
        self.btn_1.clicked.connect(self.pet_anim)
        self.btn_1.clicked2.connect(self.set_normal)
    
    def dialog_bar(self):
        
        self.dialog.show()


    def pet_anim(self):
        self.movie = QMovie("media/sweetiebot_anim2.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

    def set_normal(self):
        self.movie = QMovie("media/sweetiebot_anim.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

    def toggle_window2(self):
        if self.window2.isVisible():
            self.window2.hide()

        else:
            self.window2.show()

    def dial1(self):
        if self.dialog.isVisible():
            self.dialog.hide()

        else:
            self.dialog.show()




app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
