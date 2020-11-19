# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
f_obj = open('practical4/task2.txt', encoding='utf-8')
number_of_lines = f_obj.readlines()
print(f'Количество строк: {len(number_of_lines)}')
