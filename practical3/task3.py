# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.
argument_list = ('x', 'y', 'z')
arguments = {}


def my_func(x, y, z):
    lists = [x, y, z]
    max_number1 = max(lists)
    lists.remove(max_number1)
    max_number2 = max(lists)
    return max_number1 + max_number2


for n, i in enumerate(argument_list):
    answer = float(input(f'Введите численное значение аргумента {i}: '))
    arguments[n] = answer
print(f'Сумма двух наибольших аргументов равна: {my_func(arguments[0], arguments[1], arguments[2])}')
