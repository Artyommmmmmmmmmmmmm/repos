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


line = QVBoxLayout()

hline1 = QHBoxLayout()
hline2 = QHBoxLayout()

line.addLayout(hline1)
line.addLayout(hline2)

hline1.addWidget(g1)
hline1.addWidget(g2)
hline1.addWidget(g3)

hline2.addWidget(g4)
hline2.addWidget(g5)
win.setLayout(line)

app.exec_()
