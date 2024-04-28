def check_data(data, correct_answer):
    while data not in correct_answer:
        data = input('Неверно. Попробуйте еще раз: ')
    print('Верно')

year = input('Введите год рождения Пушкина: ')

check_data(year, ['1799'])

day = input('Введите день рождения Пушкина: ')

check_data(day, ['06.06', '6 июня', '06 июня', '06/06'])


