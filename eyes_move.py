import sys
from random import randint

import math
from PyQt5 import Qt
from PyQt5.QtCore import *
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import *
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QMovie, QIcon
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


class AnotherWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(1400, 400, 432, 517)

        self.label7 = QLabel()
        self.label7.setGeometry(0, 0, 432, 517)
        self.pixmap = QPixmap('media/window_dial.svg')
        self.label7.setPixmap(self.pixmap)

        self.label = QLabel("Hello World % d" % randint(0, 100), parent=self.label7)
        self.label.setGeometry(0, 0, 432, 517)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window2 = AnotherWindow()
        self.setGeometry(1481, 857, 301, 172)

        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        self.label = QLabel()
        self.setCentralWidget(self.label)

        self.label6 = QLabel(parent=self.label)
        self.label6.setGeometry(0, 0, 200, 200)

        self.label7 = QLabel(parent=self.label6)
        self.label7.setGeometry(35, 85, 100, 50)
        self.pixmap = QPixmap('media/bottom.png')
        self.label7.setPixmap(self.pixmap)

        self.label3 = QLabel(parent=self.label6)
        self.label3.setGeometry(0, 0, 40, 40)
        self.pixmap = QPixmap('media/eye22.svg')
        self.label3.setPixmap(self.pixmap)

        self.label4 = QLabel(parent=self.label6)
        self.label4.setGeometry(0, 0, 40, 40)
        self.pixmap = QPixmap('media/eye22.svg')
        self.label4.setPixmap(self.pixmap)

        # transform = QTransform()
        # transform.rotate(45)
        # self.label4.setPixmap(self.pixmap.transformed(transform))

        self.label5 = QLabel(parent=self.label)
        self.label5.setGeometry(0, 0, 235, 278)
        self.movie = QMovie("media/gifmaker_me(1).gif")
        self.label5.setMovie(self.movie)
        self.movie.start()

        self.label6.setMask(QBitmap('media/mask.png'))

        self.label8 = QLabel(parent=self.label)
        self.label8.setGeometry(200, 100, 100, 50)

        # self.label23 = Label(parent=self)
        # self.label23.setGeometry(10, 20, 260, 278)
        # self.pixmap = QPixmap('media/image2.png')
        # self.label23.setPixmap(self.pixmap)
        # self.label23.hide()

        # self.counter = 0

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_cursor_position)
        self.timer.start(50)

        self.animation = QPropertyAnimation(self.label, b"geometry")
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation.setStartValue(QRect(0, 0, 235, 278))
        self.animation.setEndValue(QRect(0, 120, 235, 278))

        self.animation2 = QPropertyAnimation(self.label, b"geometry")
        self.animation2.setDuration(500)
        self.animation2.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation2.setStartValue(QRect(0, 120, 235, 278))
        self.animation2.setEndValue(QRect(0, 0, 235, 278))

        self.btn_up = Label(parent=self.label)
        self.btn_up.setGeometry(10, 120, 150, 100)

        self.btn_up2 = Label(parent=self.label)
        self.btn_up2.setGeometry(10, 10, 150, 100)
        self.btn_up2.hide()

        self.btn_up.clicked.connect(self.toggle_window12)
        self.btn_up2.clicked.connect(self.toggle_w2)

    def toggle_window12(self):
        self.btn_up2.show()
        self.btn_up.hide()
        self.animation.start()
        self.timer.stop()
        self.movie.stop()

    def toggle_w2(self):
        self.btn_up.show()
        self.btn_up2.hide()
        self.animation2.start()
        self.timer.start()
        self.movie.start()

    def toggle_window2(self):
        if self.window2.isVisible():
            self.window2.hide()

        else:
            self.window2.show()

    def update_cursor_position(self):
        def draw_eye1(eye_x, eye_y):
            cursor_pos = QCursor.pos()

            mouse_x = cursor_pos.x() - 1481
            mouse_y = cursor_pos.y() - 857

            distance_x = mouse_x - eye_x
            distance_y = mouse_y - eye_y

            distance = min(math.sqrt(distance_x ** 2 + distance_y ** 2), 10)
            angle = math.atan2(distance_y, distance_x)

            pupil_x = eye_x + (math.cos(angle) * distance)
            pupil_y = eye_y + (math.sin(angle) * distance)

            # self.label.setText(f'fgggg {pupil_x}, {pupil_y}')
            self.label3.move(int(pupil_x) - 13, int(pupil_y) - 17)

        draw_eye1(50, 102)

        def draw_eye2(eye_x, eye_y):
            cursor_pos = QCursor.pos()

            mouse_x = cursor_pos.x() - 1481
            mouse_y = cursor_pos.y() - 857

            distance_x = mouse_x - eye_x
            distance_y = mouse_y - eye_y

            distance = min(math.sqrt(distance_x ** 2 + distance_y ** 2), 15)
            angle = math.atan2(distance_y, distance_x)

            pupil_x = eye_x + (math.cos(angle) * distance)
            pupil_y = eye_y + (math.sin(angle) * distance)

            self.label4.move(int(pupil_x) - 13, int(pupil_y) - 17)

        draw_eye2(110, 107)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()
