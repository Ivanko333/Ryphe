from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.connects()
        self.set_appear()

    def set_appear(self):
        pass

    def initUI(self):
        button = QPushButton("СТАРТ!")
        start_text = QLabel('')
        instruction = QLabel('')
        v_line = QVBoxLayout()
        v_line.addWidget(button, alignment=Qt.AlignCenter)
        v_line.addWidget(start_text, alignment=Qt.AlignCenter)
        v_line.addWidget(instruction, alignment=Qt.AlignCenter)
        self.setLayout(v_line)

    def connects(self):
        pass
