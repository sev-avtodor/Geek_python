# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.
f_obj = open('../practical5/task1.txt', '+w')
txt = f_obj.read()
f_obj.close()
print(txt)
