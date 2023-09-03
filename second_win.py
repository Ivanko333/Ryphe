from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *
from third_win import ThirdWin


class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.button4 = None
        self.text_timer = None
        self.third_win = None
        self.initUI()
        self.connects()
        self.set_appear()

    def set_appear(self):
        self.resize(win_width, win_height)
        self.setWindowTitle(txt_title)
        self.show()

    def initUI(self):
        name_txt = QLabel(txt_name)
        age = QLabel(txt_age)
        test1 = QLabel(txt_test1)
        test2 = QLabel(txt_test2)
        test3 = QLabel(txt_test3)
        self.text_timer = QLabel('00:00:00')
        button1 = QPushButton(txt_starttest1)
        button2 = QPushButton(txt_starttest2)
        button3 = QPushButton(txt_starttest3)
        self.button4 = QPushButton(txt_sendresults)
        h_line = QHBoxLayout()
        v_line1 = QVBoxLayout()
        v_line2 = QVBoxLayout()
        input1 = QLineEdit(txt_hintname)
        input2 = QLineEdit(txt_hintage)
        input3 = QLineEdit(txt_hinttest1)
        input4 = QLineEdit(txt_hinttest2)
        input5 = QLineEdit(txt_hinttest3)

        v_line1.addWidget(name_txt, alignment=Qt.AlignLeft)
        v_line1.addWidget(input1, alignment=Qt.AlignLeft)
        v_line1.addWidget(age, alignment=Qt.AlignLeft)
        v_line1.addWidget(input2, alignment=Qt.AlignLeft)
        v_line1.addWidget(test1, alignment=Qt.AlignLeft)
        v_line1.addWidget(button1, alignment=Qt.AlignLeft)
        v_line1.addWidget(input3, alignment=Qt.AlignLeft)
        v_line1.addWidget(test2, alignment=Qt.AlignLeft)
        v_line1.addWidget(button2, alignment=Qt.AlignLeft)
        v_line1.addWidget(test3, alignment=Qt.AlignLeft)
        v_line1.addWidget(button3, alignment=Qt.AlignLeft)
        v_line1.addWidget(input4, alignment=Qt.AlignLeft)
        v_line1.addWidget(input5, alignment=Qt.AlignLeft)
        v_line1.addWidget(self.button4, alignment=Qt.AlignCenter)
        v_line2.addWidget(self.text_timer, alignment=Qt.AlignCenter)
        self.setLayout(v_line1)
        self.setLayout(v_line2)
        self.setLayout(h_line)

    def next(self):
        self.third_win = ThirdWin()
        self.hide()

    def connects(self):
        self.button4.clicked.connect(self.next)
