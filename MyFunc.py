import os
import shutil
import sys


# Все функции

def get_name_func(type_obj):
    name = input(f'Введите имя {type_obj}:\n')
    return name


def get_type_file():
    type_obj = input(f'Введите расширение файла:\n')
    return type_obj


def create_folder(folder_name):
    if folder_name not in os.listdir():
        os.mkdir(folder_name)
        return 'Папка создана!'
    else:
        return 'Папка с таким именем уже существует!'


def delete_folder(folder_name):
    if folder_name in os.listdir():
        os.rmdir(folder_name)
        return 'Папка удалена!'
    else:
        return 'Папка с таким именем не найдена!'


def copy_folder(folder_name, new_folder_name):
    if new_folder_name not in os.listdir():
        shutil.copytree(folder_name, new_folder_name)
        return 'Копия создана!'
    else:
        return 'Папка с таким именем существует!'


def create_file():
    file_name = get_name_func('файла') + get_type_file()
    if file_name not in os.listdir():
        new_file = open(file_name, 'x')
        new_file.close()
        print('Файл создан!')
    else:
        print('Файл с таким именем существует!')


def delete_file():
    file_name = get_name_func('файла') + get_type_file()
    if file_name in os.listdir():
        os.remove(file_name)
        print('Файл удален!')
    else:
        print('Файла с таким именем не существует!')


def copy_file():
    file_type = get_type_file()
    file_name = get_name_func('файла') + file_type
    if file_name in os.listdir():
        new_file_name = input('Введите имя для копии файла:\n') + file_type
        if new_file_name not in os.listdir():
            shutil.copy(file_name, new_file_name)
            print('Файл копирован!')
        else:
            print('Файл с таким именем существует!')
    else:
        print('Файл с таким именем не существует')


def list_folder():
    print(os.listdir())


def save_list_folder(file_name):
    count = 0
    content_folder = os.listdir()
    f = open(file_name, 'w')
    f.write('files:')
    for i in content_folder:
        if ('.' in i and '.' != i[0]) or '.git' == i[0:4]:
            if count == 0:
                f.write(i)
            else:
                f.write(',' + i)
            count += 1
    count = 0
    f.write('\nfolders:')
    for i in content_folder:
        if ('.' not in i or '.' == i[0]) and '.git' != i[0:4]:
            if count == 0:
                f.write(i)
            else:
                f.write(',' + i)
            count += 1
    f.close()
    print('Содержимое папки сохранено!')
    return 'ok'


def list_only_folder():
    for i in os.listdir():
        if os.path.isdir(i):
            print(i)


def list_only_files():
    for i in os.listdir():
        if os.path.isfile(i):
            print(i)


def system_info():
    print(sys.platform)


def user_info():
    print(os.environ.get('USERNAME'))


# C:\Users\flap\Desktop\HomeWorks (python creator)\L5
def change_directory():
    os.chdir(input('Укажите путь:\n'))
    print(f'Путь {os.getcwd()}')
