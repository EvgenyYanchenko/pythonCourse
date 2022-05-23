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
import string


class App(QWidget):
    def __init__(self):
        self.start()
        self.set()
        self.get_disklist()
        self.create_Disk_Bar()
        #self.get_disklist()




    def start(self):
        self.ui = uic.loadUi("FileManagerMainWindow.ui")
        self.ui.show()


    def get_disklist(self):
        disk_list = []
        for c in string.ascii_uppercase:
            disk = c + ':'
            if os.path.isdir(disk):
                disk_list.append(disk)
        return disk_list





    def create_Disk_Bar(self, list=get_disklist):
        print('work')
        self.ui.radioButton_1.setText(str(list))

    #    lbl = self.Label(self.window, text='each_contact').place(x=5, y=5)


    def set(self):
        self.ui.pushButton_5.clicked.connect(lambda: self.click())

    def show_path(self,path):
        self.ui.textBrowser.setText(path)

    def get_list_direcrory(self, path):
        print(os.listdir(path))



    def click(self,num='text'):
        self.table1set(text=num)
        self.show_path('eee')



    def table1set(self,text='text'):
       print(text)
       self.ui.tableWidget.setRowCount(3)
       self.ui.tableWidget.setItem(0,0,QTableWidgetItem(str(text*2)))







if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = App()
    app.exec_()