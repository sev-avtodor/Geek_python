print('3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn')
x = str(input('Введите число "X": '))
x = int(x) + int(x + x) + int(x + x + x)
print(f'x + xx + xxx = {x}')
