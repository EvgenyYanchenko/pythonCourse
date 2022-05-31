import sys
import Actions
from Actions import create_File, create_Folder, deleting, copying, save_info_log, get_list

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic

# try:
#     from PyQt5.QtWidgets import *
#     from PyQt5.QtGui import *
#     from PyQt5.QtCore import *
#
# except:
#     from PyQt4.QtGui import *
#     from PyQt4.QtCore import *

import os
import string

command = sys.argv[1]
if command == 'list':
    get_list()
elif command == 'create_File':
    name = sys.argv[2]
    create_File(name,'text text text')
elif command == 'create_Folder':
    name = sys.argv[2]
    create_Folder(name)
elif command =='deleting':
    name = sys.argv[2]
    deleting(name)

elif command =='copy':
    name = sys.argv[2]
    new_name = sys.argv[3]
    create_File(name)
    copying(name, new_name)

elif command =='help':
    print('\n' +'list - список файлов')
    print('create_file - создание файла')
    print('deleting - удаление файла')
    print('copy - копирование файла'+'\n')


# class App(QWidget):
#     def __init__(self):
#         self.start()
#         self.set()
#         self.set_disk('D:/')
#         self.create_Disk_Bar()
#
#         self.generate_Dict()
#
#     def start(self):
#         self.ui = uic.loadUi("FileManagerMainWindow.ui")
#         self.ui.show()
#         Actions.create_Folder('Folder_from_app')
#         Actions.create_File('newFile_from_app', 'new text from app')
#         Actions.deleting('newFile_from_app')
#         Actions.copying('')
#         Actions.save_info_log("now")
#
#     # создаем словарь чекбокс=диск
#     def generate_Dict(self, list=[]):
#         #  делаем невидимые все radioButton (диски) кроме C
#         # self.ui.radioButton_2.setHidden(True)
#         self.ui.radioButton_3.setHidden(True)
#         self.ui.radioButton_4.setHidden(True)
#         self.ui.radioButton_5.setHidden(True)
#
#         # заполняем названиями дисков radioButtonы
#         list = self.get_disklist()
#
#         if list[0].isalpha():
#             print("list 0 cont str " + list[0])
#             self.ui.radioButton_1.setText(list[0])
#         else:
#             print("no str " + list[0])
#         # self.ui.radioButton_2.setText(list[1])
#         # self.ui.radioButton_3.setText(list[2])
#         # self.ui.radioButton_4.setText(list[3])
#         # self.ui.radioButton_5.setText(list[4])
#
#     def set_disk(self, path='C:/'):
#         self.ui.textBrowser.setText(path)
#
#     def get_disklist(self):
#         disk_list = []
#         for c in string.ascii_uppercase:
#             disk = c + ':'
#             if os.path.isdir(disk):
#                 disk_list.append(disk)
#         return disk_list
#
#     #  Naming all radioButton
#     def create_Disk_Bar(self, list=[]):
#         list = self.get_disklist()
#         print(len(list))
#
#     def set(self):
#         self.ui.pushButton_5.clicked.connect(lambda: self.click())
#
#     def get_list_direcrory(self, path):
#         print(os.listdir(path))
#
#     def click(self, num='text'):
#         self.table1set(text=num)
#
#     def table1set(self, text='text'):
#         print(text)
#         self.ui.tableWidget.setRowCount(3)
#         self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(str(text * 2)))
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = App()
#     app.exec_()
