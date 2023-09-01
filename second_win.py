from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from instr import *


class SecondWin(QWidget):
    def __init__(self) -> object:
        super().__init__()
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
        button1 = QPushButton(txt_starttest1)
        button2 = QPushButton(txt_starttest2)
        button3 = QPushButton(txt_starttest3)
        v_line1 = QVBoxLayout()
        v_line2 = QVBoxLayout()
        h_line = QHBoxLayout
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
        self.setLayout(h_line)
        self.setLayout(v_line1)
        self.setLayout(v_line2)

    def connects(self):
        pass
