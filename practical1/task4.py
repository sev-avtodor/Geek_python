# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

# проверка введенного числа на целое
def chek(number):
    if int(number) > 0:
        if float(number) % 1 == 0:
            return number
        else:
            print('введенное число не целое')
    else:
        print('введенное число 0 или отрицательное')


user_number = float(input('Введите целое положительное число: '))
while chek(user_number) != user_number:
    user_number = float(input(f'Введите целое положительное число: '))

while user_number:
    list_numbers = list(str(int(user_number)))
    print(f'Наибольшее число: {max(list_numbers)}')
    break
