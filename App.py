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
        self.set_disk('D:/')
        self.create_Disk_Bar()
        self.generate_Dict()





    def start(self):
        self.ui = uic.loadUi("FileManagerMainWindow.ui")
        self.ui.show()

    #создаем словарь чекбокс=диск
    def generate_Dict(self,list=[]):
        list = self.get_disklist()
        Disks = dict()

        Disks['radioButton_1'] = list[0]
        Disks['radioButton_2'] = list[1]
        Disks['radioButton_3'] = list[2]
       # Disks['radioButton_4'] = list[3]



    def set_disk(self,path='C:/'):
        self.ui.textBrowser.setText(path)



    def get_disklist(self):
        disk_list = []
        for c in string.ascii_uppercase:
            disk = c + ':'
            if os.path.isdir(disk):
                disk_list.append(disk)
        return disk_list


#  Naming all radioButton
    def create_Disk_Bar(self, list=[]):
        list=self.get_disklist()
        print(len(list))


    def set(self):
        self.ui.pushButton_5.clicked.connect(lambda: self.click())



    def get_list_direcrory(self, path):
        print(os.listdir(path))

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