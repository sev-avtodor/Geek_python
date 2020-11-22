# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.
class Car:
    def __init__(self, speed=None, color=None, name=None, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        # машина поехала
        print(self.name, '- машина поехала')

    def stop(self):
        # машина остановилась
        print(self.name, '- машина остановилась')

    def turn(self, direction):
        # машина повернула, куда повернула
        print(self.name, 'повернула', direction)

    def get_show_speed(self, max_speed=None):
        # вывод текущей скорости
        speed_message = f'{self.name}\nТекущая скорость: {self.speed}'
        print(speed_message)


class TownCar(Car):

    def get_show_speed(self, max_speed=40):
        message_error = ''
        if max_speed:
            if self.speed > max_speed:
                message_error = f'Превышение скорости на {self.speed - max_speed}!' \
                                f'\nМаксимальная скорость: {max_speed}\n'
        super().get_show_speed()
        print(message_error)


class SportCar(Car):
    pass


class WorkCar(Car):

    def get_show_speed(self, max_speed=60):
        message_error = ''
        if max_speed:
            if self.speed > max_speed:
                message_error = f'Превышение скорости на {self.speed - max_speed}!' \
                                f'\nМаксимальная скорость: {max_speed}\n'
        super().get_show_speed()
        print(message_error)


class PoliceCar(Car):
    pass


town_car = TownCar(80, 'Зеленый', 'Такси')
sport_car = SportCar(120, 'Красный', 'Спорткар')
work_car = WorkCar(65, 'Оранжевый', 'Коммунальная машина')
police_car = PoliceCar(75, 'Бело-синий', 'Полицейская машина', True)

print('Название: {}, цвет: {}, текущая скорость: {}, полицейская: {}'.format(town_car.name, town_car.color, town_car.speed, town_car.is_police))
print('Название: {}, цвет: {}, текущая скорость: {}, полицейская: {}'.format(sport_car.name, sport_car.color, sport_car.speed, sport_car.is_police))
print('Название: {}, цвет: {}, текущая скорость: {}, полицейская: {}'.format(work_car.name, work_car.color, work_car.speed, work_car.is_police))
print('Название: {}, цвет: {}, текущая скорость: {}, полицейская: {}'.format(police_car.name, police_car.color, police_car.speed, police_car.is_police))
work_car.get_show_speed()
sport_car.stop()
town_car.go()
police_car.turn('за угол')
