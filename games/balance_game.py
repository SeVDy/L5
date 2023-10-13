# Функция пополнения счета

import os


def incr_balance(file_name, increase_balance):
    f = open(file_name, 'r')
    account_balance = int(f.read())
    f.close()
    f = open(file_name, 'w')
    account_balance += increase_balance
    f.write(str(account_balance))
    f.close()
    return account_balance


# Функция покупки модифицированная
def purchace(file_name_balance, file_name_history_purch, price_of_purch):
    f = open(file_name_balance, 'r')
    account_balance = int(f.read())
    f.close()
    if price_of_purch > account_balance:
        print('Недостаточно средств для совершения покупки\n')
    else:
        name_of_purch = input('Введите название покупки:\n')
        account_balance -= price_of_purch
        f = open(file_name_balance, 'w')
        f.write(str(account_balance))
        f.close()
        f = open(file_name_history_purch, 'a')
        f.write(f'{name_of_purch}:{price_of_purch}\n')
        f.close()
    return account_balance


# Функция просмотра истории покупок
def history_of_purchaces(file_name_history_purch):
    print('История покупок:')
    f = open(file_name_history_purch, 'r')
    for i in f:
        print(i[:-2])
    f.close()
    print('')


def balance_game():
    # Объявление переменных
    if 'balance_save.txt' not in os.listdir():
        f = open('balance_save.txt', 'w')
        f.write('0')
        f.close()
    if 'history_purch_save.txt' not in os.listdir():
        f = open('history_purch_save.txt', 'w')
        f.close()
    # Логика терминала
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход\n')
        # Выбираем пункт
        choice = input('Выберите пункт:\n')
        # Выполняем действия согласно выбранному пункту
        match choice:
            case '1':
                inc_balance = int(input('Введите сумму для пополнения:\n'))
                print(f'Ваш баланс:\n{incr_balance("balance_save.txt",inc_balance)} руб\n')
            case '2':
                price_purch = int(input('Введите сумму для покупки:\n'))
                balance = purchace('balance_save.txt', 'history_purch_save.txt', price_purch)
                print(f'Ваш баланс:\n{balance} руб\n')
            case '3':
                history_of_purchaces('history_purch_save.txt')
            case '4':
                break
            case _:
                pass
