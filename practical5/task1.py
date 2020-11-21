# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
f_obj = open('../practical5/task1.txt', '+w')
while True:
    text = input('Введите текст')
    if text != '':
        f_obj.write(text + '\n')
    else:
        break
f_obj.close()

# обарзец решения:
with open('../practical5/task1.txt', '+w') as f:
    while True:
        text = input('Введите текст')
        if text == '':
            break
        f_obj.write(text + '\n')

# на заметку:
# конструкция условия короче в образце
# в образце почему то не закрыли файл для завершения записи
