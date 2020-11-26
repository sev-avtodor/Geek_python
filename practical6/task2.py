# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна.
# Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т
class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass_asphalt(self, thickness=1, mass=25):
        print(self._length * self._width * mass * thickness / 1000, ' т')


road = Road(4, 25)
road.mass_asphalt()

# ============================образец решения:
# class Road:
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#
#     def calc_mass(self):
#         mass = self._length * self._width * 25 * 5 / 1000
#         return mass
#
#
# my_road = Road(20, 5000)
# print(my_road.calc_mass(), 'т')

# работа над ошибками:
# забыл сделать return в методе класса