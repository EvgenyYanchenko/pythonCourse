import sys
from PyQt5.QtWidgets import  QApplication, QWidget
from PyQt5 import uic
try:
    from PyQt5.QtWidgets import *
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *

except:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *

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

    def click(self,num='text'):
        self.table1set(text=num)

    def table1set(self,text='text'):
       print(text)
       self.ui.tableWidget.setRowCount(3)
       self.ui.tableWidget.setItem(0,0,QTableWidgetItem(str(text*2)))




if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()