from MyFunc import *
from games.victory import victory_game
from games.balance_game import balance_game

while True:
    print('1.Создать папку')
    print('2.Удалить папку')
    print('3.Копировать папку')
    print('4.Создать файл')
    print('5.Удалить файл')
    print('6.Копировать файл')
    print('7.Просмотр содержимого рабочей директории')
    print('8.Сохранить содержимое папки в файл')
    print('9.Посмотреть только папки')
    print('10.Посмотреть только файлы')
    print('11.Просмотр информации о ОС')
    print('12.Создатель программы')
    print('13.Играть в викторину')
    print('14.Мой банковйский счет')
    print('15.Смена рабочей директории')
    print('16.Выход')

    user_choose = input('Введите номер пункта:\n')
    # Выбор
    match user_choose:
        case '1':
            folder_name = input(f'Введите имя папки:\n')
            create_folder(folder_name)
        case '2':
            folder_name = input(f'Введите имя папки:\n')
            delete_folder(folder_name)
        case '3':
            folder_name = input(f'Введите имя папки:\n')
            if folder_name in os.listdir():
                new_folder_name = input('Введите имя для копии папки:\n')
                copy_folder(folder_name, new_folder_name)
            else:
                print('Папки с таким именем не существует!')
        case '4':
            create_file()
        case '5':
            delete_file()
        case '6':
            copy_file()
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
