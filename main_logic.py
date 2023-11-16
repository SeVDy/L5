from MyFunc import *
from games.victory import victory_game
from games.balance_game import balance_game

while True:
    print('\n',
          ' 1.Создать папку                              2.Удалить папку\n',
          ' 3.Копировать папку                           4.Создать файл\n',
          ' 5.Удалить файл                               6.Копировать файл\n',
          ' 7.Просмотр содержимого рабочей директории    8.Сохранить содержимое папки в файл\n',
          ' 9.Посмотреть только папки                   10.Посмотреть только файлы\n',
          '11.Просмотр информации о ОС                  12.Создатель программы\n',
          '13.Играть в викторину                        14.Мой банковйский счет\n',
          '15.Смена рабочей директории                  16.Выход')

    user_choose = input('Введите номер пункта:\n')
    # Выбор
    match user_choose:
        case '1':
            folder_name = get_name_func('папки')
            print(create_folder(folder_name))
        case '2':
            folder_name = get_name_func('папки')
            print(delete_folder(folder_name))
        case '3':
            folder_name = get_name_func('папки')
            copy_folder_name = input('Введите имя для копии папки:\n')
            print(copy_folder(folder_name, copy_folder_name))
        case '4':
            file_name = get_name_func('файла')
            print(create_file(file_name))
        case '5':
            file_name = get_name_func('файла')
            print(delete_file(file_name))
        case '6':
            file_name = get_name_func('файла')
            copy_file_name = input('Введите имя для копии файла:\n')
            print(copy_file(file_name, copy_file_name))
        case '7':
            list_folder()
        case '8':
            save_list_folder('listdir.txt')
        case '9':
            list_only_folder()
        case '10':
            list_only_files()
        case '11':
            system_info()
        case '12':
            user_info()
        case '13':
            victory_game()
        case '14':
            balance_game()
        case '15':
            change_directory()
        case '16':
            exit()
        case _:
            pass
