from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import *
import sys

def application():
    app = QApplication(sys.argv)
    window = QMainWindow()

    window.setWindowTitle('Менеджер Файлов на Python')
    window.setGeometry(300,250, 1000,700)

# Объекты на форме
    main_text = QtWidgets.QLabel(window)
    main_text.setGeometry(20,20,50,50)
    main_text.setFont(QFont('Times', 14))
    main_text.setText("Bold")



    window.show()
    sys.exit(app.exec_())


if __name__ =="__main__":
    application()

