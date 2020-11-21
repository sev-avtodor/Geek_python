# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.
f_obj = open('../practical5/task4.txt', encoding='utf-8')
lines = f_obj.readlines()

for i, items in enumerate(lines):
    items = items.rstrip('\n')
    items = items.split(' — ')
    item = items[0]
    if items[1] == '1':
        item = 'Один - '
    elif items[1] == '2':
        item = 'Два - '
    elif items[1] == '3':
        item = 'Три - '
    elif items[1] == '4':
        item = 'Четыре - '
    lines[i] = item + items[1]
print(lines)

# Образец решения:
with open('../practical5/task4.txt', encoding='utf-8') as f:
    lines = f.readlines()


with open('../practical5/task4rus.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        if '1' in line:
            line = line.replace('One', 'Один')
        elif '2' in line:
            line = line.replace('Two', 'Два')
        elif '3' in line:
            line = line.replace('Three', 'Три')
        elif '4' in line:
            line = line.replace('Four', 'Четыре')
        f.write(line)


# на заметку:
# не правильно выполнил задание, нужно было не вывести на экран а сохранить в новый файл(
