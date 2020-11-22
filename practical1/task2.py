# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
from datetime import datetime

# Пока так решил вопрос с впереди стоящим нулем у значений до 10
def chek(number):
    if number < 10:
        number = '0' + str(number)
        return number
    else:
        return number

print('2. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс')
user_time = int(input('Сверим часы. Введите время в секундах: '))
hour = int(user_time // 3600)
minutes = int((user_time / 60) % 60)
seconds = int(user_time % 60)

hour = chek(hour)
minutes = chek(minutes)
seconds = chek(seconds)


servertime = datetime.now()
server_hour = chek(servertime.hour)
servertime_minute = chek(servertime.minute)
servertime_second = chek(servertime.second)

print(f'Ваше текущее время: {hour}:{minutes}:{seconds}. Время на моем сервере: {server_hour}:{servertime_minute}:{servertime_second}')