import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLineEdit, QPushButton

import llm_work_middle

import threading
import math, re
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


import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QPushButton, QVBoxLayout, QProgressBar
from PyQt5.QtCore import QThread, QObject, pyqtSignal as Signal, pyqtSlot as Slot
from langchain_community.llms.llamacpp import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler


file_name = ('./chat_history.txt')

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

llm = LlamaCpp(
    chat_format="llama-2",
    model_path="./llama-2-7b-chat.Q3_K_S.gguf",
    n_ctx=1024, 
    n_gpu_layers = -1,  # The number of layers to put on the GPU. The rest will be on the CPU. If you don't know how many layers there are, you can use -1 to move all to GPU.
    n_batch = 1024, 
    top_k= 40,
    repeat_penalty= 1.4,
    min_p = 0.05,
    top_p = 0.95,
    callback_manager = callback_manager,
    use_mlock = True,
    verbose= True,
    max_tokens=-1,
    stop=[ "Ai:", "Human:"],
)

class ChatbotWindow(QMainWindow):
    work_requested = Signal(str)
    
    def __init__(self):
        super().__init__()

        

        #self.setAttribute(Qt.WA_TranslucentBackground, True)
        #self.setAttribute(Qt.WA_NoSystemBackground, True)
        #self.setWindowFlags(Qt.FramelessWindowHint)
        #self.setWindowFlags(self.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)

        self.setGeometry(600, 400, 470, 370)

        #chat = ChatbotWindow
        self.sec_window = QLabel(self)
        self.mane_window = QLabel(self)

        self.setStyleSheet("""background: #131414; border: 1px solid #403e53; border-radius: 10px; 
                           padding: 0px; font-size: 8pt; font-family: montserrat; font-weight: 500; color: #ded9e2""")
        

 
        self.title = "Sweetie <Desktop> Bot"
 
        self.mane_window.setWindowTitle(self.title)
        #self.mane_window.setBaseSize(460, 400)
        self.mane_window.setGeometry(0, 0, 470, 370)
        self.sec_window.setGeometry(0, 0, 550, 440)
        self.mane_window.setStyleSheet("background: #131414; border: 1px solid #403e53; border-radius: 10px; padding: 0px; font-size: 8pt; font-family: montserrat; font-weight: 500; color: #ded9e2")

        # Create a scroll area
        self.scroll1 = QtWidgets.QScrollArea(self.mane_window)
        self.scroll1.setGeometry(10, 10, 450, 300)

        # Set scrollbar policies
        self.scroll1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scroll1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
 
        # Create a widget to be scrolled
        self.widget = QtWidgets.QWidget()
        self.layout1 = QtWidgets.QVBoxLayout(self.widget)
        #self.widget.setMaximumWidth(450)
        #widget.setMinimumSize(450, 300)
        
        #self.scroll1.setSizeAdjustPolicy()
 
 
        self.scroll1.setStyleSheet("""
            QWidget {background: rgba(255, 255, 255, 0); border: 0px solid #8f4e21; width: 10px; border-radius: 0px;}
            QScrollArea {background: #161b22; border: 1px solid #403e53; width: 10px; border-radius: 10px;}
            
        """)

        self.label7 = QLabel(self.sec_window)
        self.label7.setGeometry(294, 253, 250, 250)
        self.pixmap = QPixmap('./dial2.svg')
        self.label7.setPixmap(self.pixmap)
        self.label7.setStyleSheet("background: rgba(255, 255, 255, 0); border: 0px solid #403e53; border-radius: 0px; ")
        

        self.input_field = QLineEdit(self.mane_window)
        self.input_field.setGeometry(10, 320, 400, 40)
        self.input_field.setStyleSheet("background: #1a2027; border: 1px solid #403e53; width: 10px; border-radius: 10px; padding: 5px; font-size: 9pt; font-family: montserrat; font-weight: 500; color: #ded9e2")
        
        self.setWindowIcon(QtGui.QIcon('./icon.ico'))
        

        self.button = QPushButton(self.mane_window)
        self.button.setGeometry(420, 320, 40, 40)
        self.button.setIcon(QtGui.QIcon('icon.svg'))
        self.button.setIconSize(QtCore.QSize(40,40))
        self.button.setStyleSheet("background: #3DED97; border: 1px solid #403e53; width: 10px; border-radius: 10px; padding: 0px; font-size: 20pt; font-family: montserrat; font-weight: 400; color: #185254")
        self.button.clicked.connect(self.update_scroll)

        self.sizePolicy1 = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)

        self.process1()

        

        self.input_field.returnPressed.connect(self.send_message)
        

        #====================================================================

        self.worker = llm_work_middle.Worker()
        self.worker_thread = QThread()

        
        self.worker.completed.connect(self.complete_bot)

        self.work_requested.connect(self.worker.do_work)

        self.worker.moveToThread(self.worker_thread)

        self.worker_thread.start()

        #====================================================================

        self.scroll1.setWidgetResizable(True)

        

        self.scroll1.setWidget(self.widget)
        
        self.show()

    
        self.catch_up = self.scroll1.verticalScrollBar().maximum()
        self.scroll1.verticalScrollBar().setValue(self.catch_up)
        

    def process_ai(self, line):
            line = re.sub('ai:', '', line)
            line2 = re.sub(';', '\n', line)
            ai_res = QtWidgets.QLabel()
            ai_res.setText(f"🦄: {line2}")
            ai_res.setContentsMargins(10, 10, 10, 10)
            ai_res.setStyleSheet("background: #1a2027; border: 0px solid #403e53; padding: 0px; border-radius: 5px; font-size: 9pt; font-family: montserrat; font-weight: 500; color: #ded9e2")
            #ai_res.setReadOnly(True)
            #ai_res.setTextFormat(QtCore.Qt.PlainText)
            
            #ai_res.setCodecForTr(QTextCodec.codecForName("System"))
            
            #print(f"human: {line}")
            #ai_res.setMinimumSize(300, 30)
            ai_res.setMaximumWidth(425)
            

            #ai_res.setScaledContents(True)
            ai_res.setWordWrap(True)
            
            ai_res.setSizePolicy(self.sizePolicy1)
            
            self.layout1.addWidget(ai_res)
            self.scroll1.setWidgetResizable(True)

    def process_hu(self, line):
            line = re.sub('human:', '', line)
            line2 = re.sub(';', '\n', line)
            #line2 = re.split("[;]", line)
            
            hu_res = QtWidgets.QLabel()
            hu_res.setText(f"😎: {line2}")
            #hu_res.setReadOnly(True)
            hu_res.setMaximumWidth(425)
            hu_res.setContentsMargins(10, 10, 10, 10)
            hu_res.setWordWrap(True)
            
            hu_res.setStyleSheet("background: #131414; border: 0px solid #403e53; padding: 0px; border-radius: 5px; font-size: 9pt; font-family: montserrat; font-weight: 500; color: #ded9e2")
            
            #hu_res.setContentsMargins
            
            #hu_res.setMinimumSize(300, 30)
            
            #print(f"human: {line}")
            hu_res.setSizePolicy(self.sizePolicy1)
            
            #hu_res.setScaledContents(True)
            self.layout1.addWidget(hu_res)
            self.scroll1.setWidgetResizable(True)

    def send_message(self):
            # Get user input and clear the input field
            #user_input = (f"{input()}")
            user_input = self.input_field.text()
            #user_input_re = re.sub('\n', ';', user_input)
            with open(file_name, "a", encoding='utf-8') as f: 
                f.write(f"human: {user_input}\n")

            self.human_add()

            #self.chat_area.append(f"<p style='allignment: right;font-size:15pt;font-family: montserrat;'><b>Me:</b> {user_input}</p>")
            self.input_field.clear()

            

            #self.work_requested.emit(chat_history)
            self.work_requested.emit(user_input)

            #self.thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
            #self.thread.start()
    
    

            
            
    def human_add(self):
            line2 = self.input_field.text()

            hu_res1 = QtWidgets.QLabel()
            hu_res1.setText(f"😎: {line2}")
            hu_res1.setMaximumWidth(425)
            #hu_res1.setMinimumSize(300, 30)
            hu_res1.setContentsMargins(10, 10, 10, 10)
            hu_res1.setWordWrap(True)
            #hu_res1.setTextFormat(QtCore.Qt.PlainText)
            #hu_res1.setScaledContents(True)
            hu_res1.setStyleSheet("background: #131414; border: 0px solid #403e53; padding: 0px; border-radius: 5px; font-size: 9pt; font-family: montserrat; font-weight: 500; color: #ded9e2")
            hu_res1.setSizePolicy(self.sizePolicy1)
            
            self.layout1.addWidget(hu_res1)
            
            
            
            
            


    def complete_bot(self, response):
            # Get response from the Chatbot and display it in the chat area
            #response = self.chatbot.get_response(user_input)
            
            # Format the response in HTML
            #print(response)
            
            response_re = re.sub('\n', ';', response)
            
            with open(file_name, "a", encoding='utf-8') as f: 
                f.write(f"ai: {response_re}\n")

            

            self.ai_add(response)



    def ai_add(self, response):
            

        ai_res2 = QtWidgets.QLabel()
        ai_res2.setText(f"🦄: {response}")
        ai_res2.setMaximumWidth(425)
        #ai_res2.setMinimumSize(300, 30)
        ai_res2.setContentsMargins(10, 10, 10, 10)
        ai_res2.setWordWrap(True)
        #ai_res2.setTextFormat(QtCore.Qt.PlainText)
        #ai_res2.setScaledContents(True)
        ai_res2.setStyleSheet("background: #1a2027; border: 0px solid #403e53; padding: 0px; border-radius: 5px; font-size: 9pt; font-family: montserrat; font-weight: 500; color: #ded9e2")
        ai_res2.setSizePolicy(self.sizePolicy1)
        
        self.layout1.addWidget(ai_res2)
        
        
        
        
        
        
        
    def update_scroll(self):
        
        
        self.catch_up = self.scroll1.verticalScrollBar().maximum()
        
        self.scroll1.verticalScrollBar().setValue(self.catch_up)
        print(self.catch_up)
    

    def process1(self):
        with open(file_name, "r", encoding='utf-8', buffering=1) as file:
            for line in file:
                line = line.strip()
                        
                if re.match(r"^ai:", line):  # Check if line starts with `#`
                    self.process_ai(line)

                elif re.match(r"^human:", line):  # Check if line starts with `#`
                    self.process_hu(line)

                else:
                    print(line)
        
        



# Create and run the application
#app = QApplication(sys.argv)
#main_window = ChatbotWindow()
#sys.exit(app.exec())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = ChatbotWindow()
    sys.exit(app.exec_())