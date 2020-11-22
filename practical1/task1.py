# 1. Поработайте с переменными, создайте несколько, выведите на экран,
# запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

def experience(user_experience, user_age):
    if user_age <= 16:
        if user_experience >= 12:
            text = 'Ого, да Вы матерый зубр Python)'
            return text
        else:
            text = 'Отличный возраст - Вы своеверменно начали изучать Python!)'
            return text
    else:
        if user_experience <= 12:
            text = 'Вы молодец - Мы попробуем углубить Ваши знания Python!)'
            return text
        else:
            text = 'Учится никогда не поздно! Добро пожаловать в мир Python!)'
            return text

print('1. Поработайте с переменными')
name = input('Давайте знакомиться! Как Вас зовут?: ')
age = int(input('Сколько Вам полных лет?: '))
stag = int(input('Как давно в месяцах Вы изучаете Python?: '))
print(f'Рад знакомсту, {name}! {experience(stag, age)}')