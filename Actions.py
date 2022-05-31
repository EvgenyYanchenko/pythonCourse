import os
import shutil
import datetime


def create_File(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_Folder(name):
    os.mkdir(name)


def deleting(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copying(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже есть')

    else:
        shutil.copy(name, new_name)


def save_info_log(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt','a',encoding='utf-8') as f:
        f.write(result+'\n')
