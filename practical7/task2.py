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

class Clothes:

    def __init__(self, name):
        self.name = name
        self.type = ('coat', 'costume')

    # def summ(self):
    #     sum_consumption = sum(x.consumption for x in self.__dict__.items())
    #     return sum_consumption


class Coat(Clothes):

    def __init__(self, name, V):
        self.V = V

    def tissue_consumption(self):
        self.__setattr__('consumption', self.V / 6.5 + 0.5)
        return self.consumption


class Costume(Clothes):

    def __init__(self, name, H):
        self.H = H

    def tissue_consumption(self):
        self.__setattr__('consumption', 2 * self.H + 0.3)
        return self.consumption


palto1 = Coat('Снежинка', 35)
palto2 = Coat('Рабочий', 55)
costume1 = Costume('Деловой', 175)
print(palto1.tissue_consumption())
print(palto1.tissue_consumption())
print(costume1.tissue_consumption())


def summ():
    # sum_consumption = sum(x for x.consumption in Clothes.__dict__.items())
    print(sum(int((x for x in Clothes.__dict__.values()))))
    # return sum_consumption


print(summ())
