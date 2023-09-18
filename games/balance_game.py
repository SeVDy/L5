#Функция пополнения счета
def incr_balance(current_balance):
    current_balance += int(input('Введите сумму для пополнения:\n'))
    return  current_balance
#Функция покупки модифицированная
def purchace(current_balance,current_history):
    price_of_purch = int(input('Введите сумму для покупки:\n'))
    if price_of_purch > current_balance:
        print('Недостаточно средств для совершения покупки\n')
    else:
        name_of_purch = input('Введите название покупки:\n')
        current_balance -= price_of_purch
        current_history[name_of_purch] = price_of_purch
    return current_balance, current_history
#Функция просмотра истории
def history_of_purchaces(current_history):
    print('История покупок:')
    for i, j in current_history.items():
            print(f'{i} ---> {j}')
    print('')

def balance_game():
    # Объявление переменных
    balance = 0
    history = {}
    #Логика терминала
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход\n')
        #Выбираем пункт
        choice = input('Выберите пункт:\n')
        #Выполняем действия согласно выбранному пункту
        match choice:
            case '1':
                balance = incr_balance(balance)
                print(f'Ваш баланс:\n{balance} руб\n')
            case '2':
                balance, history = purchace(balance,history)
                print(f'Ваш баланс:\n{balance} руб\n')
            case '3':
                history_of_purchaces(history)
            case '4':
                break
            case _:
                pass
