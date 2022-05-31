import os
import shutil
import datetime

#1 создание текстового файла и запись в него текста
def create_File(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)

#2 вывод списка папок из текущей директории
def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = (f for f in result if os.path.isdir(f))
    print(result)

#3 создание папки
def create_Folder(name):
    os.mkdir(name)

#4 удаление папки или файла
def deleting(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)

# 5 копирование папки
def copying(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже есть')

    else:
        shutil.copy(name, new_name)

# 6 сохранение лога
def save_info_log(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')
