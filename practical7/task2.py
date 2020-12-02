# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):
    summary = []

    def __init__(self, name, param):
        self.name = name
        self.param = param
        self.type = ('coat', 'costume')


    @abstractmethod
    def summ(self, param):
        self.summary.append(int(param))


class Coat(Clothes):
    globals()

    @property
    def summ(self):
        text = round(self.param / 6.5 + 0.5)
        self.summary.append(text)
        return text


class Costume(Clothes):
    globals()

    @property
    def summ(self):
        text = round(self.param / 6.5 + 0.5)
        self.summary.append(text)
        return text


palto1 = Coat('Снежинка', 35)
palto2 = Coat('Рабочий', 55)
costume1 = Costume('Деловой', 175)
print(palto1.summ)
print(palto2.summ)
print(costume1.summ)
# Реализовать общий подсчет расхода ткани.
# print(f'Общий объем ткани составит: {palto1.summ + palto2.summ + costume1.summ}')
print(sum([int(i) for i in Clothes.summary]))
