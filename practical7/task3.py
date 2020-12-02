# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
#
# Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток, соответственно.
#
# В методе деления должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
#
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.
class Cell():
    iMenuNumber = 0

    def __init__(self, input):
        self.__class__.iMenuNumber = self.__class__.iMenuNumber + 1
        self.param = [input, len(str(input))]
        self.number = self.__class__.iMenuNumber

    def __add__(self, other):
        return f'Сумма клеток {self.number} и {other.number}: {self.param[0] + other.param[0]}, ячеек: {self.param[1]}'

    def __sub__(self, other):
        if self.param[0] - other.param[0] > 0:
            return f'Разница клетки {self.number} и {other.number}: {self.param[0] - other.param[0]}, ячеек: {self.param[1]}'
        else:
            return f'Разница клеток {self.number} и {other.number} отрицательна'

    def __mul__(self, other):
        return f'Произведение клеток {self.number} и {other.number}: {self.param[0] * other.param[0]}, ячеек: {self.param[1] * other.param[1]}'

    def __truediv__(self, other):
        return f'Произведение клеток {self.number} и {other.number}: {self.param[0] / other.param[0]}, ячеек: {self.param[1] // other.param[1]}'

    def make_order(self, leight_line):
        text = ''
        kletok_vsego = self.param[0]
        kletok_v_stroke = leight_line
        # while kletok_vsego >= kletok_v_stroke:
        #     for i in range(kletok_v_stroke):
        #         text += '*'
        #     text += '\n'
        #     kletok_vsego -= kletok_v_stroke
        # else:
        #     for i in range(kletok_vsego % kletok_v_stroke):
        #         text += '*'
        #     text += '\n'
        # return text
        while kletok_vsego >= kletok_v_stroke:
            text = ''.join('*' for i in range(8)) + '\n'
            kletok_vsego -= kletok_v_stroke
        else:
            text += ''.join('*' for i in range(kletok_vsego % kletok_v_stroke))
        return text


kletka1 = Cell(15)
kletka2 = Cell(2)
kletka3 = Cell(13)
kletka4 = Cell(4)
print('Количество клеток:', Cell.iMenuNumber)
print(kletka1 + kletka2)
print(kletka4 - kletka3)
print(kletka3 - kletka2)
print(kletka1 * kletka4)
print(kletka1 / kletka4)
print(kletka1.make_order(8))
# x = '*'
# text = ''.join('*' for i in range(8))
# print(text)
# print(kletka1 + kletka2)

