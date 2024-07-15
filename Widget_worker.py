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
    QSizeGrip
)
from PyQt5 import QtCore, QtGui, QtWidgets

class Area(QLabel):
    Wheel = pyqtSignal(int)
    HoverEnter = pyqtSignal()
    HoverLeave = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__()
        QLabel.__init__(self, parent=parent)
    
    def wheelEvent(self, event: QWheelEvent):
        delta = event.angleDelta().y()
        #print(delta)
        self.Wheel.emit(delta)

    def enterEvent(self, e):
        #print("Mouse Entered")
        self.HoverEnter.emit()
        
    def leaveEvent(self, e):
        #print ("Mouse Left")
        self.HoverLeave.emit()
           
class CustomTitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setAutoFillBackground(True)
        self.setBackgroundRole(QPalette.ColorRole.Highlight)
        self.initial_pos = None
        title_bar_layout = QHBoxLayout(self)
        title_bar_layout.setContentsMargins(1, 1, 1, 1)
        title_bar_layout.setSpacing(2)

        self.title = QLabel(f"{self.__class__.__name__}", self)
        self.title.setStyleSheet(
            """font-weight: bold;
               border: 2px solid black;
               border-radius: 12px;
               margin: 2px;
            """
        )
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        if title := parent.windowTitle():
            self.title.setText(title)
        title_bar_layout.addWidget(self.title)

        self.min_button = QToolButton(self)
        min_icon = self.style().standardIcon(
            QStyle.StandardPixmap.SP_TitleBarMinButton
        )
        self.min_button.setIcon(min_icon)
        self.min_button.clicked.connect(self.window().showMinimized)

        # Max button
        self.max_button = QToolButton(self)
        max_icon = self.style().standardIcon(
            QStyle.StandardPixmap.SP_TitleBarMaxButton
        )
        self.max_button.setIcon(max_icon)
        self.max_button.clicked.connect(self.window().showMaximized)

        # Close button
        self.close_button = QToolButton(self)
        close_icon = self.style().standardIcon(
            QStyle.StandardPixmap.SP_TitleBarCloseButton
        )
        self.close_button.setIcon(close_icon)
        self.close_button.clicked.connect(self.window().close)

        # Normal button
        self.normal_button = QToolButton(self)
        normal_icon = self.style().standardIcon(
            QStyle.StandardPixmap.SP_TitleBarNormalButton
        )
        self.normal_button.setIcon(normal_icon)
        self.normal_button.clicked.connect(self.window().showNormal)
        self.normal_button.setVisible(False)

        buttons = [
            self.min_button,
            self.normal_button,
            self.max_button,
            self.close_button,
        ]
        for button in buttons:
            button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            button.setFixedSize(QSize(28, 28))
            button.setStyleSheet(
                """QToolButton { border: 2px solid white;
                                 border-radius: 12px;
                                }
                """
            )
            title_bar_layout.addWidget(button)

class MoveMagic(QLabel):
    moved = pyqtSignal(int, int)
    

    def __init__(self, parent=None):
        super().__init__()
        QLabel.__init__(self, parent=parent)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
        
    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        move_x = (delta.x())
        move_y = (delta.y())
        self.oldPos = event.globalPos()
        self.moved.emit(move_x, move_y)

class LabelMoveMagic(QLabel):
    #clicked = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__()
        QLabel.__init__(self, parent=parent)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()
        
    def mouseMoveEvent(self, event):
        delta = QPoint (event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

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
    
class Main(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setAttribute(Qt.WA_NoSystemBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        self.sizePolicy1 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        self.sizePolicy2 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.layout_butt = QVBoxLayout(self)
        
        self.setMinimumSize(80, 60)

        self.main = QLabel(self)
        self.setGeometry(1000, 200, 200, 200)
        #self.main.setGeometry(0, 0, 200, 200)
        self.main.setStyleSheet("""background:  rgba(255, 255, 255, 0.004) ; border: 0px solid #403e53; border-radius: 10px; 
                                padding: 0px; font-size: 8pt; font-family: montserrat; font-weight: 500; color: #ded9e2""")
        
        self.titlebar = QLabel(self.main)
        #self.titlebar.setGeometry(0, 0, 200, 40)
        self.titlebar.setFixedHeight(30)
        #self.titlebar.setMaximumHeight(20)
        self.titlebar.setStyleSheet("""background:  rgba(255, 255, 255, 0.004); border: 0px solid #403e53; border-top-left-radius: 10px; 
                                border-top-right-radius: 10; border-bottom-left-radius: 0px; border-bottom-right-radius: 0; 
                                padding: 0px; font-size: 8pt; font-family: montserrat; font-weight: 500; color: #ded9e2""")
        self.mane_bar = QLabel(self.main)
        self.mane_bar.setStyleSheet("""background: #131414; border: 1px solid #403e53; border-top-left-radius: 0px; 
                                border-top-right-radius: 0; border-bottom-left-radius: 10px; border-bottom-right-radius: 10; 
                                padding: 0px; font-size: 8pt; font-family: montserrat; font-weight: 500; color: #ded9e2""")
        
        self.delet = Label(self.titlebar)
        self.delet.setSizePolicy(self.sizePolicy2)
        self.delet.setFixedWidth(50)
        self.delet.setStyleSheet("""background: #b4dcb9; border: 1px solid #403e53; border-top-left-radius: 0px; 
                                border-top-right-radius: 10; border-bottom-left-radius: 0px; border-bottom-right-radius: 0; 
                                padding: 0px; font-size: 8pt; font-family: montserrat; font-weight: 500; color: #ded9e2""")
        
        
        self.title = MoveMagic(self.titlebar)
        self.title.setStyleSheet("""background: #131414; border: 1px solid #403e53; border-top-left-radius: 10px; 
                                border-top-right-radius: 0; border-bottom-left-radius: 0px; border-bottom-right-radius: 0; 
                                padding: 0px; font-size: 8pt; font-family: montserrat; font-weight: 500; color: #ded9e2""")
        self.title.setSizePolicy(self.sizePolicy2)
        self.title.setText("ClipBoard")

        self.layout_butt2 = QVBoxLayout(self.main)
        self.layout_butt3 = QHBoxLayout(self.titlebar)

        self.layout_butt2.addWidget(self.titlebar)
        self.layout_butt2.addWidget(self.mane_bar)
        self.layout_butt3.addWidget(self.title)
        self.layout_butt3.addWidget(self.delet)

        
        self.layout_butt.setContentsMargins(0, 0, 0, 0)
        self.layout_butt2.setContentsMargins(0, 0, 0, 0)
        self.layout_butt3.setContentsMargins(0, 0, 0, 0)
        #self.layout_butt2.addStretch(1)
        self.layout_butt2.setSpacing(0)
        self.layout_butt3.setSpacing(0)
        

        self.titlebar.setSizePolicy(self.sizePolicy2)

        
        self.delet.clicked.connect(self.window().hide)
        

        #self.setLayout(self.layout_butt)
        self.layout_butt.addWidget(self.main)
        self.setCentralWidget(self.main)

        self.title.moved.connect(self.moved)
        
        self.set_grips()

    

    def moved(self, move_x, move_y):
        print("moved", move_x, move_y)
        #move_p = (int(move_px))
        self.move(self.x() + move_x, self.y() + move_y)


    def set_grips(self):
        self.gripSize = 10
        self.grips = []
        for i in range(4):
            grip = QSizeGrip(self)
            grip.setStyleSheet("""
                background-color: transparent; 
            """)
            grip.resize(self.gripSize, self.gripSize)
            self.grips.append(grip)

    def resizeEvent(self, event):
        QMainWindow.resizeEvent(self, event)
        rect = self.rect()
        # top left grip doesn't need to be moved...
        # top right
        self.grips[1].move(rect.right() - self.gripSize, 0)
        # bottom right
        self.grips[2].move(
            rect.right() - self.gripSize, rect.bottom() - self.gripSize)
        # bottom left
        self.grips[3].move(0, rect.bottom() - self.gripSize)

