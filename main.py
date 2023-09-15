from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,QMessageBox,QRadioButton

app = QApplication([])

window = QWidget()
window.show()
window.resize(500,300)
window.setWindowTitle('Конкурс від Logika')

question = QLabel('Як називається бібліотека, яку ми вивчаємо?')

ans1 = QRadioButton('PyQt5')
ans2 = QRadioButton('Turtle')
ans3 = QRadioButton('PyGame')
ans4 = QRadioButton('Panda3D')

main_layout = QVBoxLayout()
l1 =  QHBoxLayout()
l2 =  QHBoxLayout()
l3 =  QHBoxLayout()

l1.addWidget(question,alignment=Qt.AlignCenter)
l2.addWidget(ans1,alignment=Qt.AlignCenter)
l2.addWidget(ans2,alignment=Qt.AlignCenter)
l3.addWidget(ans3,alignment=Qt.AlignCenter)
l3.addWidget(ans4,alignment=Qt.AlignCenter)
main_layout.addLayout(l1)
main_layout.addLayout(l2)
main_layout.addLayout(l3)

window.setLayout(main_layout)

def show_win():
    victory_win = QMessageBox()
    victory_win.setText('Правильно!Ви отримуєте 1 логік!')
    victory_win.exec_()

def show_loose():
    loose = QMessageBox()
    loose.setText('Невірно! На вашому балансі 0 логіків! Ви банкрот!')
    loose.exec_()

ans1.clicked.connect(show_win)
ans2.clicked.connect(show_loose)
ans3.clicked.connect(show_loose)
ans4.clicked.connect(show_loose)


app.exec_()
