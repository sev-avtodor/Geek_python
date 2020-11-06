''' 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2]. '''
my_rating = [7, 5, 3, 3, 2]


def rating_sort(user_rating, user_count):
    global my_rating
    def_count = 0
    while def_count < user_count:
        if not def_count == 0:
            user_rating = int(input(f'{def_count + 1}. Введите рейтинг натуральным числом: '))
            while user_rating < 0:
                user_rating = int(input(f'Вы ошиблись.\n'
                                        f'{def_count + 1}. Введите рейтинг целым положительным числом: '))
        print(f'Текущий рейтинг:\n{my_rating}')
        print(f'Добавляем введенное Вами значение: {user_rating}')
        try:
            my_rating.reverse()
            i = my_rating.index(user_rating)
            my_rating.insert(i, user_rating)
            my_rating.reverse()
        except ValueError:
            my_rating.reverse()
            my_rating.insert(0, user_rating)
        print(f'Результат выполнения: {my_rating}')
        def_count += 1


count = int(input("Введите количество цифр рейтинга для ввода: "))
user = int(input('1. Введите рейтинг натуральным числом: '))
while user < 0:
    user = int(input('Вы ошиблись.\n'
                     '1. Введите рейтинг целым положительным числом: '))
rating_sort(user, count)
