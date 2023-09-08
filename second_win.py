from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtGui import QFont
from instr import *
from third_win import ThirdWin


class SecondWin(QWidget):
    def __init__(self):
        super().__init__()
        self.t3 = None
        self.t2 = None
        self.t1 = None
        self.age_input = None
        self.name_input = None
        self.timer = None
        self.button2 = None
        self.button3 = None
        self.button1 = None
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
        self.text_timer.setFont(QFont('Times', 40, QFont.Bold))
        self.button1 = QPushButton(txt_starttest1)
        self.button2 = QPushButton(txt_starttest2)
        self.button3 = QPushButton(txt_starttest3)
        self.button4 = QPushButton(txt_sendresults)
        h_line = QHBoxLayout()
        v_line1 = QVBoxLayout()
        v_line2 = QVBoxLayout()
        self.name_input = QLineEdit(txt_hintname)
        self.age_input = QLineEdit(txt_hintage)
        self.t1 = QLineEdit(txt_hinttest1)
        self.t2 = QLineEdit(txt_hinttest2)
        self.t3 = QLineEdit(txt_hinttest3)

        v_line1.addWidget(name_txt, alignment=Qt.AlignLeft)
        v_line1.addWidget(self.name_input, alignment=Qt.AlignLeft)
        v_line1.addWidget(age, alignment=Qt.AlignLeft)
        v_line1.addWidget(self.age_input, alignment=Qt.AlignLeft)
        v_line1.addWidget(test1, alignment=Qt.AlignLeft)
        v_line1.addWidget(self.button1, alignment=Qt.AlignLeft)
        v_line1.addWidget(self.t1, alignment=Qt.AlignLeft)
        v_line1.addWidget(test2, alignment=Qt.AlignLeft)
        v_line1.addWidget(self.button2, alignment=Qt.AlignLeft)
        v_line1.addWidget(test3, alignment=Qt.AlignLeft)
        v_line1.addWidget(self.button3, alignment=Qt.AlignLeft)
        v_line1.addWidget(self.t2, alignment=Qt.AlignLeft)
        v_line1.addWidget(self.t3, alignment=Qt.AlignLeft)
        v_line1.addWidget(self.button4, alignment=Qt.AlignCenter)
        v_line2.addWidget(self.text_timer, alignment=Qt.AlignCenter)
        h_line.addLayout(v_line1)
        h_line.addLayout(v_line2)
        self.setLayout(h_line)

    def next(self):
        self.third_win = ThirdWin(self.age, self.t1, self.t2, self.t3)
        self.hide()

    def test_timer1(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1_event)
        self.timer.start(1000)

    def timer1_event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        if time.toString('ss') == '00':
            self.timer.stop()

    def test_timer2(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2_event)
        self.timer.start(1500)

    def timer2_event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('ss'))
        if time.toString('ss') == '00':
            self.timer.stop()

    def test_timer3(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3_event)
        self.timer.start(1000)

    def timer3_event(self):
        global time
        time = time.addSecs(-1)
        self.text_timer.setText(time.toString('hh:mm:ss'))
        if time.toString('ss') == '00':
            self.timer.stop()
        if time.toString('ss') >= '59':
            self.text_timer.setStyleSheet('color: rgb(0,255,0)')
        if time.toString('ss') <= '45':
            self.text_timer.setStyleSheet('color: rgb(0, 0, 0)')
        if time.toString('ss') <= '15':
            self.text_timer.setStyleSheet('color: rgb(0,255,0)')

    def connects(self):
        self.button4.clicked.connect(self.next)
        self.button1.clicked.connect(self.test_timer1)
        self.button2.clicked.connect(self.test_timer2)
        self.button3.clicked.connect(self.test_timer3)
