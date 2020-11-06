# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
def split_str(user_str):
    lists = user_str.split()
    answer_print(lists)


def answer_print(answer):
    i = 0
    for world in answer:
        print(f'{i + 1}. {world[:10]}')
        i += 1


user = input('Введите несколько строк разделенных пробелами:\n')
split_str(user)
