import os
import shutil
import sys

#***********
#Все функции
#***********
def get_name_func(type):
    name = input(f'Введите имя {type}:\n')
    return name
def get_type_file():
    type = input(f'Введите расширение файла:\n')
    return type
def create_folder():
    folder_name = get_name_func('папки')
    if folder_name not in os.listdir():
        os.mkdir(folder_name)
        print('Папка создана!')
    else:
        print('Папка с таким именем уже существует!')

def delete_folder():
    folder_name = get_name_func('папкм')
    if  folder_name in os.listdir():
        os.rmdir(folder_name)
        print('Папка удалена!')
    else:
        print('Папка с таким именем не найдена!')

def copy_folder():
    folder_name = get_name_func('папкм')
    if folder_name in  os.listdir():
        new_folder_name = input('Введите имя для копии папки:\n')
        if new_folder_name not in os.listdir():
            shutil.copytree(folder_name, new_folder_name)
            print('Копия создана!')
        else:
            print('Папка с таким именем существует!')
    else:
        print('Папки с таким именем не существует!')

def create_file():
    file_name = get_name_func('файла') +get_type_file()
    if file_name not in os.listdir():
        new_file = open(file_name,'x')
        new_file.close
        print('Файл создан!')
    else:
        print('Файл с таким именем существует!')

def delete_file():
    file_name = get_name_func('файла') + get_type_file()
    if file_name  in os.listdir():
        os.remove(file_name)
        print('Файл удален!')
    else:
        print('Файла с таким именем не существует!')

def copy_file():
    file_type = get_type_file()
    file_name = get_name_func('файла') +    file_type
    if file_name in os.listdir():
        new_file_name = input('Введите имя для копии файла:\n') +    file_type
        if new_file_name not in os.listdir():
            shutil.copy(file_name, new_file_name)
            print('Файл копирован!')
        else:
            print('Файл с таким именем существует!')
    else:
        print('Файл с таким именем не существует')

def list_folder():
    print(os.listdir())

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
#C:\Users\flap\Desktop\HomeWorks (python creator)\L5
def change_directory():
    os.chdir(input('Укажите путь:\n'))
    print(f'Путь {os.getcwd()}')