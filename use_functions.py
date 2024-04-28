# 1. пополнение счета
# при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
# после того как пользователь вводит сумму она добавляется к счету
# снова попадаем в основное меню
def adding_funds(count):
    result = count + float(input('Введите сумму пополнения: '))
    return result

# 2. покупка
# при выборе этого пункта пользователю предлагается ввести сумму покупки
# если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
# если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
# снимаем деньги со счета
# сохраняем покупку в историю
# выходим в основное меню

def payment(count, purchase_list):
    price = float(input('Введите стоимость покупки: '))
    if price > count:
        print('Недостаточно средств. Пополните счет.')
        new_count = count
    else:
        new_count = count - price
        purchase = input('Введите название покупки: ')
        purchase_list.append([purchase, price])
    return new_count, purchase_list

# 3. история покупок
# выводим историю покупок пользователя (название и сумму)
# возвращаемся в основное меню
def show_purchase_list(purchase_list):
    for purchase in purchase_list:
        print(*purchase)

count = 0
purchase_list = []

while True:
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. выход')

    choice = input('Выберите пункт меню: ')
    if choice == '1':
        count = adding_funds(count)
    elif choice == '2':
        count, purchase_list = payment(count, purchase_list)
    elif choice == '3':
        show_purchase_list(purchase_list)
    elif choice == '4':
        break
    else:
        print('Неверный пункт меню')