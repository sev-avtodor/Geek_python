# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def division(x, y):
    try:
        answer = x / y
    except ZeroDivisionError:
        answer = 'Вы ввели недопустимое значение'
    return answer


x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
print(division(x, y))