from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from instr import *
from second_win import SecondWin


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.second_win = None
        self.button = None
        self.initUI()
        self.connects()
        self.set_appear()

    def set_appear(self):
        self.resize(win_width, win_height)
        self.setWindowTitle(txt_title)
        self.show()

    def initUI(self):
        self.button = QPushButton("СТАРТ!")
        start_text = QLabel(txt_hello)
        instruction = QLabel(txt_instruction)
        v_line = QVBoxLayout()
        v_line.addWidget(start_text, alignment=Qt.AlignCenter)
        v_line.addWidget(instruction, alignment=Qt.AlignCenter)
        v_line.addWidget(self.button, alignment=Qt.AlignCenter)
        self.setLayout(v_line)

    def next(self):
        self.second_win = SecondWin()
        self.hide()
    
    def connects(self):
        self.button.clicked.connect(self.next)


app = QApplication([])
win = MainWin()
app.exec_()
