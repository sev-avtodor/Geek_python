# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
with open('../practical5/task5.txt', 'w', encoding='utf-8') as f:
    numbers = input('введите числа через пробел: ')
    f.write(numbers + '\n')
    numbers = map(int, numbers.split())
    sum_numbers = sum(numbers)
    line = f'Сумма чисел: {sum_numbers}'
    print(line)
    f.write(line + '\n')
    f.close()

# образец решения
# with open('../practical5/task5.txt', 'w') as f:
#     nums = input('Введите целые числа через пробел: ')
#     f.write('Введенные числа: ' + nums + '\n')
#     nums = map(int, nums.split())  # without list
#     sum_nums = sum(nums)
#     f.write('Сумма чисел: ' + str(sum_nums))
#     print('Сумма введенных чисел:', sum_nums)
# print('Все записано в файл')

# на заметку:
# без указания кодировки при создании, получаю криивую кодировку кирилицы при записи
