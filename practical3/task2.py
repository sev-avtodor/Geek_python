# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.
data = {
    'name': 'имя',
    'surname': 'фамилия',
    'year_birth': 'год рождения',
    'city': 'город проживания',
    'email': 'email',
    'phone': 'телефон'
}


def opros():
    text = {}
    count = 0
    for key, items in data.items():
        count += 1
        answer = input(f'Введите "{items}": ')
        while (answer == '' and count == 1) or (answer == '' and count == 2):
            answer = input(f'Введите обязательное значение "{items}": ')
            break
        while answer:
            text[key] = answer
            break
    return otvet(name=text.get('name'), year_birth=text.get('year_birth'), city=text.get('city'), email=text.get('email'), phone=text.get('phone'), surname=text.get('surname'))


def otvet(name, surname, year_birth='None', city='None', email='None', phone='None'):
    text = f'Здравствуйте {surname} {name}! ' \
           f'Проверьте введенные данные: ' \
           f'День рождения: {year_birth}; Город: {city}; E-mail: {email}; Телефон: {phone}'
    return text


ask = input(opros())
print(ask)
