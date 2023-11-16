import os
import shutil
import sys


# Все функции

# Фун-ия запроса имени для папки или файла
def get_name_func(type_obj):
    name = input(f'Введите имя {type_obj}:\n')
    return name


# Фун-ия создание папки с заданным именем №1
def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        result = 'Папка создана!'
    except FileExistsError:
        result = 'Папка с таким именем уже существует!'
    return result


# Фун-ия удаление папки с заданным именем №2
def delete_folder(folder_name):
    try:
        os.rmdir(folder_name)
        result = 'Папка удалена!'
    except FileNotFoundError:
        result = 'Папка с таким именем не найдена!'
    except NotADirectoryError:
        result = 'Объект не является папкой!'
    return result


# Фун-ия создания копии папки с заданным именем и вводом нового имени для копии №3
def copy_folder(folder_name, copy_folder_name):
    try:
        shutil.copytree(folder_name, copy_folder_name)
        result = 'Копия создана!'
    except FileExistsError:
        result = 'Папка с таким именем существует!'
    except FileNotFoundError:
        result = 'Папки с таким именем не существует!'
    except NotADirectoryError:
        result = 'Объект не является папкой!'
    return result


# Фун-ия создания нового файла №4
def create_file(file_name):
    try:
        new_file = open(file_name, 'x')
        new_file.close()
        result = 'Файл создан!'
    except FileExistsError:
        result = 'Файл с таким именем существует!'
    return result


# Фун-ия удаления файла №5
def delete_file(file_name):
    try:
        os.remove(file_name)
        result = 'Файл удален!'
    except FileNotFoundError:
        result = 'Файла с таким именем не существует!'
    except PermissionError:
        result = 'Объект не является файлом!'
    return result


# Фун-ия копирования файла №6
def copy_file(file_name, copy_file_name):
    try:
        shutil.copy(file_name, copy_file_name)
        result = 'Файл копирован!'
    except FileExistsError:
        result = 'Файл с таким именем существует!'
    except FileNotFoundError:
        result = 'Файл с таким именем не существует!'
    except PermissionError:
        result = 'Объект не является файлом!'
    return result


# Фун-ия отображение содержимого текущей папки №7
def list_folder():
    print(os.listdir())


# Фун-ия сохранения содержимого текущей папки в файл с заданным именем №8
def save_list_folder(file_name):
    count = 0
    content_folder = os.listdir()
    f = open(file_name, 'w')
    f.write('files:')
    for i in content_folder:
        if os.path.isfile(i) and count == 0:
            f.write(i)
            count += 1
        elif os.path.isfile(i) and count > 0:
            f.write(', ' + i)
    count = 0
    f.write('\nfolders:')
    for i in content_folder:
        if os.path.isdir(i) and count == 0:
            f.write(i)
            count += 1
        elif os.path.isdir(i) and count > 0:
            f.write(', ' + i)
    f.close()
    return 'Содержимое папки сохранено!'


# Фун-ия отображения только папок №9
def list_only_folder():
    for i in os.listdir():
        if os.path.isdir(i):
            print(i)


# Фун-ия отображения только файлов №10
def list_only_files():
    for i in os.listdir():
        if os.path.isfile(i):
            print(i)


# Фун-ия отображения информации о системе №11
def system_info():
    print(sys.platform)


# Фун-ия отображения имени пользователя №12
def user_info():
    print(os.environ.get('USERNAME'))


# C:\Users\flap\Desktop\HomeWorks (python creator)\L5  - путь по дефолту №15
def change_directory():
    os.chdir(input('Укажите путь:\n'))
    print(f'Путь {os.getcwd()}')
