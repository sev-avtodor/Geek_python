# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
f_obj = open('../practical5/task2.txt', encoding='utf-8')
lists = f_obj.readlines()
print(f'Количество строк: {len(lists)}')
for i, lines in enumerate(lists):
    count = lines.split()
    print(f'В строке номер {i+1} слов: {len(count)}')


# образец решения:
# with open('../practical5/task2.txt', encoding='utf-8') as f:
#     lines = f.readlines()
#     print('Количество строк:', len(lines))
#     for num_line, line in enumerate(lines, start=1):
#         print('{} cтрока содержит - {} слов'.format(num_line, len(line.split())))

# на заметку:
# в цикле в конструкции enumerate() указано с какого числа начинать нумерацию
# повторил вывод строки через .format