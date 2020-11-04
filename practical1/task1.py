print('1. Поработайте с переменными')


def experience(user_experience, user_age):
    if age <= 16:
        if stag >= 12:
            text = 'Ого, да Вы матерый зубр Python)'
            return text
        else:
            text = 'Отличный возраст - Вы своеверменно начали изучать Python!)'
            return text
    else:
        if stag <= 12:
            text = 'Вы молодец - Мы попробуем углубить Ваши знания Python!)'
            return text
        else:
            text = 'Учится никогда не поздно! Добро пожаловать в мир Python!)'
            return text


name = input('Давайте знакомиться! Как Вас зовут?: ')
age = int(input('Сколько Вам полных лет?: '))
stag = int(input('Как давно в месяцах Вы изучаете Python?: '))
print(f'Рад знакомсту, {name}! {experience(stag, age)}')