from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from instr import *


class ThirdWin(QWidget):
    def __init__(self, age, t1, t2, t3):
        super().__init__()
        self.index = None
        self.t1 = t1
        self.t2 = t2
        self.t3 = t3
        self.age = age
        self.set_appear()
        self.initUI()
        self.show()

    def set_appear(self):
        self.resize(win_width, win_height)
        self.setWindowTitle(txt_title)
        self.show()

    def initUI(self):
        final_text1 = QLabel(str(self.get_results()))
        final_text2 = QLabel()
        v_line = QVBoxLayout()
        v_line.addWidget(final_text1, alignment=Qt.AlignCenter)
        v_line.addWidget(final_text2, alignment=Qt.AlignCenter)
        self.setLayout(v_line)

    def get_results(self):
        if int(self.age) < 8:
            self.index = 0
            return 'Ошибка возраста!!!'
        self.index = (4 * (int(self.t1) + int(self.t2) + int(self.t3)) - 200) / 10
        return self.index
