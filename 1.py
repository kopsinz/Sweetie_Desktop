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


        

class InvisibleArea(QLabel):
    HoverEnter = pyqtSignal()
    HoverLeave = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__()
        QLabel.__init__(self, parent=parent)
    
    def enterEvent(self, e):
        #print("Mouse Entered")
        self.HoverEnter.emit()
        
    def leaveEvent(self, e):
        #print ("Mouse Left")
        self.HoverLeave.emit()
        

class Label(QLabel):
    clicked = pyqtSignal()
    clicked2 = pyqtSignal()
    dbl_clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__()
        QLabel.__init__(self, parent=parent)

    def mousePressEvent(self, e):
        self.clicked.emit()

    def mouseReleaseEvent(self, e):
        self.clicked2.emit()

    def doubleClicked(self, e):
        self.dbl_clicked.emit()
    


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # self.window1 = AnotherWindow()
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        
        #self.setGeometry(1481, 857, 301, 172)
        
        self.setGeometry(1860, 400, 60, 400)
        #self.setGeometry(3790, 400, 50, 400)
        

        

        self.mane_window = QWidget(self)
        self.mane_window.setGeometry(30, 0, 40, 90)
        self.mane_window.setStyleSheet("""background: #131414; border: 1px solid #403e53; border-radius: 10px; 
                           padding: 0px; font-size: 8pt; font-family: montserrat; font-weight: 500; color: #ded9e2""")
        
        #self.layout_butt = QVBoxLayout(self)
        #self.layout_butt.setGeometry(0, 0, 70, 400)
        
        self.btn_above = Label(self)
        self.btn_above.setGeometry( 0, 0, 70, 400)

        self.btn_above1 = Label(self)
        self.btn_above1.setGeometry( 0, 0, 70, 400)
        self.btn_above1.hide()


        self.btn_1 = Label(parent=self.mane_window)
        self.btn_1.setGeometry(10, 10, 40, 70)
        self.pixmap = QPixmap('media/button.svg')
        self.btn_1.setPixmap(self.pixmap)
        #self.layout_butt.addWidget(self.btn_1)
        
        self.btn_2 = QLabel(parent=self.mane_window)
        self.btn_2.setGeometry(10, 90, 40, 70)
        self.pixmap = QPixmap('media/button.svg')
        self.btn_2.setPixmap(self.pixmap)
        #self.layout_butt.addWidget(self.btn_2)

        self.btn_3 = QLabel(parent=self.mane_window)
        self.btn_3.setGeometry(10, 170, 40, 70)
        self.pixmap = QPixmap('media/button.svg')
        self.btn_3.setPixmap(self.pixmap)
        #self.layout_butt.addWidget(self.btn_3)

        self.btn_4 = QLabel(parent=self.mane_window)
        self.btn_4.setGeometry(10, 250, 40, 70)
        self.pixmap = QPixmap('media/button.svg')
        self.btn_4.setPixmap(self.pixmap)
        #self.layout_butt.addWidget(self.btn_4)

        #self.sec_window = QWidget(self)
        #self.sec_window.setGeometry(1000, 400, 1000, 700)
        
        self.animation1 = QPropertyAnimation(self.mane_window, b"geometry")
        self.animation1.setDuration(400)
        self.animation1.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation1.setStartValue(QRect(30, 0, 40, 90))
        self.animation1.setEndValue(QRect(0, 0, 70, 330))

        #self.__pingAnimation = QPropertyAnimation(self, "scale", self)
        #self.__pingAnimation.setDuration(250)
        #self.__pingAnimation.setKeyValues([(0.0, 1.0), (0.5, 1.1), (1.0, 1.0)])

        self.animation2 = QPropertyAnimation(self.mane_window, b"geometry")
        self.animation2.setDuration(400)
        self.animation2.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation2.setStartValue(QRect(0, 0, 70, 330))
        self.animation2.setEndValue(QRect(30, 0, 40, 90))

        #self.btn_above.dbl_clicked.connect(self.open_anim1)
        #self.btn_above1.dbl_clicked.connect(self.close_anim1)
        
        #self.btn_1.clicked.connect(self.close_anim)
        self.closed = True

        
        


    def wheelEvent(self, event: QWheelEvent):
        delta = event.angleDelta().y()
        print(delta)
        if delta < 0 and self.closed == True:
            self.open_anim1()
        elif delta > 0 and self.closed == False:
            self.close_anim1()
        else:
            print("hopless")


    def open_anim1(self):
        
        print("open")
        #self.btn_above.enter.disconnect(self.open_anim1)
        #self.btn_above.leave.disconnect(self.close_anim1)
        
        
        if self.animation2.state() == QPropertyAnimation.Stopped:
                #print("run")
                self.closed = False
                self.animation1.start() 
                

        else: 
            print("not able")  

        


    def close_anim1(self):
        print("close")
        #self.btn_above.enter.disconnect(self.open_anim1)
        #self.btn_above.leave.disconnect(self.close_anim1)
        
       
        if self.animation1.state() == QPropertyAnimation.Stopped:
                #print("run")
                self.closed = True
                self.animation2.start() 
                

        else: 
            print("not able")  

        
            



app = QApplication(sys.argv)
w = MainWindow()

w.show()
app.exec()