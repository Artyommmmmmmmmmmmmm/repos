from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QRadioButton, QPushButton, QGroupBox, QButtonGroup, QTextEdit, QListWidget, QLineEdit
app = QApplication([])
win = QWidget()

win.setWindowTitle('ВАШ Текст!')
win.setFixedSize(900, 700)

win.show()

g1 = QPushButton('a')
g2 = QPushButton('aa')
g3 = QPushButton('aaa')
g4 = QPushButton('aaaa')
g5 = QPushButton('aaaaa')
g6 = QPushButton('aaaaaa')
g7 = QPushButton('aaaaaaa')


line = QHBoxLayout()

vline1 = QVBoxLayout()
vline2 = QVBoxLayout()
vline3 = QVBoxLayout()

line.addLayout(vline1)
line.addLayout(vline2)
line.addLayout(vline3)

vline1.addWidget(g1)
vline1.addWidget(g2)
vline1.addWidget(g3)
vline2.addWidget(g4)
vline3.addWidget(g5)
vline3.addWidget(g6)
vline3.addWidget(g7)

win.setLayout(line)
app.exec_()
