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
    print('8.Посмотреть только папки')
    print('9.Посмотреть только файлы')
    print('10.Просмотр информации о ОС')
    print('11.Создатель программы')
    print('12.Играть в викторину')
    print('13.Мой банковйский счет')
    print('14.Смена рабочей директории')
    print('15.Выход')

    user_choose = input('Введите номер пункта:\n')
#Выбор пунктов
    match user_choose:
        case '1':
            create_folder()
        case '2':
            delete_folder()
        case '3':
            copy_folder()
        case '4':
            create_file()
        case '5':
            delete_file()
        case '6':
           copy_file()
        case '7':
            list_folder()
        case '8':
            list_only_folder()
        case '9':
            list_only_files()
        case '10':
            system_info()
        case '11':
            user_info()
        case '12':
            victory_game()
        case'13':
            balance_game()
        case'14':
            change_directory()
        case'15':
            exit()
        case _:
            pass