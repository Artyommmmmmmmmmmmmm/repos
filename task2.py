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


line = QHBoxLayout()

vline = QVBoxLayout()

line.addWidget(g1)

line.addLayout(vline)
line.addWidget(g2)

vline.addWidget(g3)
vline.addWidget(g4)
vline.addWidget(g5)
win.setLayout(line)

app.exec_()
