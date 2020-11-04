print('4. Пользователь вводит целое положительное число.\n'
      'Найдите самую большую цифру в числе.\n'
      'Для решения используйте цикл while и арифметические операции.')


def chek(number):
    if int(number) > 0:
        if float(number) % 1 == 0:
            return number
        else:
            print('число не целое')
    else:
        print('число 0 или отрицательное')


user_number = float(input('Введите целое положительное число: '))
while chek(user_number) != user_number:
    user_number = float(input(f'Введите целое положительное число: '))

while user_number:
    list_numbers = list(str(int(user_number)))
    print(f'Наибольшее число: {max(list_numbers)}')
    break
