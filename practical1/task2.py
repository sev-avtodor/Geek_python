# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
from datetime import datetime


print('2. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс')
user_time = int(input('Сверим часы. Введите время в секундах: '))
hour = int(user_time / 3600)
minutes = int((user_time - hour * 3600) / 60)
seconds = int(user_time % 60)
mytime = datetime.now()
print(f'Ваше текущее время: {hour}:{minutes}:{seconds}. Вренмя на моем сервере: {mytime.hour}:{mytime.minute}:{mytime.second}')