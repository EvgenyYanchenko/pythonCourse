import sys
from PyQt5.QtWidgets import  QApplication, QWidget
from PyQt5 import uic

import os


class App(QWidget):
    def __init__(self):
        self.start()
        self.set()


    def start(self):
        self.ui = uic.loadUi("FileManagerMainWindow.ui")
        self.ui.show()


    def set(self):
        self.ui.pushButton_5.clicked.connect(lambda: self.click())

    def click(self,num=1):
       print(num)
       self.ui.tableWidget.setItem(0,0,'ee')




if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()