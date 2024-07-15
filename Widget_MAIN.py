import sys

from random import randint

from Widget_worker import Area, Main, Label

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
from PyQt5.QtCore import QSize, Qt

from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QStyle,
    QToolButton,
    QVBoxLayout,
    QWidget,
    QPlainTextEdit,
    QShortcut,
    QAbstractScrollArea
)

class ClipBoard(Main):
    def __init__(self):
        super().__init__()

        #self.btn = Label(self.mane_bar)
        #self.btn.setSizePolicy(self.sizePolicy2)
        #self.btn.setGeometry(0, 0, 70, 90)
        #self.btn.setStyleSheet("""background: #131414; border: 1px solid #403e53; border-radius: 10px; 
        #                   padding: 0px; font-size: 8pt; font-family: montserrat; font-weight: 500; color: #ded9e2""")
        
        
        
        #self.b.insertPlainText("Copy any text to the clipboard to see it displayed here.\nThis can be from any application or source.\n")
        #self.b.move(10,10)
        #self.b.resize(100,100)
        self.sizePolicy4 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        
        self.layout_paste = QHBoxLayout(self.mane_bar)
        #self.mane_bar.addWidget(self.layout_paste)
        self.layout_paste1 = QVBoxLayout(self.mane_bar)
        self.layout_paste2 = QVBoxLayout(self.mane_bar)

        self.layout_paste.addLayout(self.layout_paste1)
        self.layout_paste.addLayout(self.layout_paste2)
        
        #self.layout_paste1.setSizePolicy(self.sizePolicy4)
        #self.b.setWidgetResizable(True)

        QShortcut(QKeySequence('Ctrl+v'), self).activated.connect(self.paste)

        
        
        
        
        #QApplication.clipboard().dataChanged.connect(self.paste)

    # Handle clipboard changes

    def paste(self):
            print("cntr+v")
            clipboard = QGuiApplication.clipboard()
            mimeData = clipboard.mimeData()

            if mimeData.hasImage():
                image = QPixmap.fromImage(mimeData.imageData())
                print("cntr+v image")
                self.b = QLabel(self.mane_bar)
                self.b.setStyleSheet("""background: #131414; border: 1px solid #403e53; border-radius: 10px; 
                           padding: 6px; font-size: 8pt; font-family: montserrat; font-weight: 500; color: #ded9e2""")
                image2 = image.scaled(150, 150, aspectRatioMode= QtCore.Qt.AspectRatioMode.KeepAspectRatio)
                #self.b.setMaximumSize(150, 150)
                self.b.setMinimumSize(50, 50)
                #image2 = image.scaled(image.width() - 200, image.height()- 200
                self.b.setMaximumSize(image2.width() + 20, image2.height() + 20)
                self.b.setPixmap(image2)
                self.b.setAlignment(Qt.AlignCenter)
                self.b.setSizePolicy(self.sizePolicy4)

                adf = randint(1,2)
                if adf == 1:
                    self.layout_paste1.addWidget(self.b)
                else:
                    self.layout_paste2.addWidget(self.b)
            #elif mimeData.hasHtml():
            #    self.b.setText(mimeData.html())
            #    self.b.setTextFormat(Qt.RichText)
            elif mimeData.hasText():
                text = mimeData.text()
                self.b2 = QPlainTextEdit(self.mane_bar)
                self.b2.setTextInteractionFlags(Qt.TextSelectableByMouse | Qt.TextBrowserInteraction)
                #self.b2.move(200, 10)
                #self.b2.resize(100,100)
                self.b2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
                self.b2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
                #self.b2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
                #self.b2.setSizePolicy(self.sizePolicy4)
                
                self.b2.insertPlainText(text)
                self.b2.setStyleSheet("""background: #131414; border: 1px solid #403e53; border-radius: 10px; 
                           padding: 6px; font-size: 8pt; font-family: montserrat; font-weight: 500; color: #ded9e2""")
                self.b2.setContentsMargins(0, 0, 0, 0)
                #self.b2.setSizePolicy(self.sizePolicy4)
                
                #self.b2.adjustSize()
                #self.b2.size()
                #print(self.b2.size())
                self.b2.setMaximumSize(150, 100)
                self.b2.setMinimumSize(50, 50)
                #self.b2.setContentsMargins(10, 10, 10, 10)
                
                
                #self.b2.setTextFormat(QtCore.Qt.PlainText)
                #self.b2.setScaledContents(True)
                #self.b.setStyleSheet("background: #131414; border: 0px solid #403e53; padding: 0px; border-radius: 5px; font-size: 9pt; font-family: montserrat; font-weight: 500; color: #ded9e2")
                
                #self.b2.setWordWrap(True)
                #self.b2.adjustSize() 
                adf = randint(1,2)
                if adf == 1:
                    self.layout_paste1.addWidget(self.b2)
                else:
                    self.layout_paste2.addWidget(self.b2)
                


            else:
                print("Cannot display data")
        
        

        
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.window2 = ClipBoard()
        self.window2.hide()

        self.sizePolicy1 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
        
        self.setGeometry(1860, 400, 60, 400)
        #self.setGeometry(3790, 400, 50, 400)
    
        self.btn_UU = Area(self)
        
        self.btn_UU.setGeometry(0, 0, 70, 90)
        self.btn_UU.setStyleSheet("""background: rgba(255, 255, 255, 0.004)""")

        self.layout_butt = QVBoxLayout(self.btn_UU)
        #self.layout_butt.setGeometry(50, 0, 70, 90)

        self.mane_window = Area(self.btn_UU)
        
        self.mane_window.setSizePolicy(self.sizePolicy1)
        self.mane_window.setStyleSheet("""background: #131414; border: 1px solid #403e53; border-radius: 10px; 
                           padding: 0px; font-size: 8pt; font-family: montserrat; font-weight: 500; color: #ded9e2""")
        
        self.layout_butt.setContentsMargins(0, 0, 0, 0)
        
        self.layout_butt.addWidget(self.mane_window)
        #self.layout_butt = QVBoxLayout(self)
        self.btn_UU.setLayout(self.layout_butt)
        
        

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
        
        self.animation1 = QPropertyAnimation(self.btn_UU, b"size")
        self.animation1.setDuration(400)
        self.animation1.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation1.setStartValue(QSize(70, 90))
        self.animation1.setEndValue(QSize(70, 330))

        #self.__pingAnimation = QPropertyAnimation(self, "scale", self)
        #self.__pingAnimation.setDuration(250)
        #self.__pingAnimation.setKeyValues([(0.0, 1.0), (0.5, 1.1), (1.0, 1.0)])

        self.animation2 = QPropertyAnimation(self.btn_UU, b"size")
        self.animation2.setDuration(400)
        self.animation2.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation2.setStartValue(QSize(70, 330))
        self.animation2.setEndValue(QSize(70, 90))

        self.animation3 = QPropertyAnimation(self.mane_window, b"pos")
        self.animation3.setDuration(200)
        self.animation3.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation3.setStartValue(QPoint(50, 0))
        self.animation3.setEndValue(QPoint(0, 0))

        #self.__pingAnimation = QPropertyAnimation(self, "scale", self)
        #self.__pingAnimation.setDuration(250)
        #self.__pingAnimation.setKeyValues([(0.0, 1.0), (0.5, 1.1), (1.0, 1.0)])

        self.animation4 = QPropertyAnimation(self.mane_window, b"pos")
        self.animation4.setDuration(200)
        self.animation4.setEasingCurve(QEasingCurve.InOutCubic)
        self.animation4.setStartValue(QPoint(0, 0))
        self.animation4.setEndValue(QPoint(50, 0))

        #self.btn_above.dbl_clicked.connect(self.open_anim1)
        #self.btn_above1.dbl_clicked.connect(self.close_anim1)
        self.close_anim()
        self.btn_1.clicked.connect(self.toggle_clipboard)
        self.btn_UU.HoverEnter.connect(self.open_anim)
        self.btn_UU.HoverLeave.connect(self.close_anim)
        self.mane_window.Wheel.connect(self.wheel)
        self.closed = True

        
    def open_anim(self):
        self.animation3.start() 
        print("32444444444444444444444444")

    def close_anim(self):
        
        self.animation4.start()
        print("sdfdsfdsgvdfg")


    def wheel(self, delta):
        
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

        
    def toggle_clipboard(self):
        if self.window2.isVisible():
            self.window2.hide()

        else:
            self.window2.show()


app = QApplication(sys.argv)
w = MainWindow()

w.show()
app.exec()