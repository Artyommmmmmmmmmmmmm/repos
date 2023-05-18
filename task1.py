from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QRadioButton, QPushButton, QGroupBox, QButtonGroup, QTextEdit, QListWidget, QLineEdit
app = QApplication([])
win = QWidget()

win.setWindowTitle('ВАШ Текст!')
win.setFixedSize(900, 700)

win.show()

g1 = QPushButton('a')
g2 = QPushButton('aa')
g3 = QPushButton('aaa')


line = QHBoxLayout()
line.addWidget(g1)
line.addWidget(g2)
line.addWidget(g3)
win.setLayout(line)

app.exec_()
