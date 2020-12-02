# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно
# — первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
class Matrix:

    def __init__(self, data):
        self.matrix = data

    def __str__(self):
        # for row in self.matrix:
        #     for x in row:
        #         return '\n'.join(' '.join(str(x)))
        return '\n'.join(' '.join([str(elem) for elem in line]) for line in self.matrix)

    def __add__(self, other):
        text = ''
        if len(self.matrix) == len(other.matrix):
            for line1, line2 in zip(self.matrix, other.matrix):
                if len(line1) != len(line2):
                    return 'Матрицы разной разрядности'

                summ_line = [x + y for x, y in zip(line1, line2)]
                text += ' '.join([str(i) for i in summ_line]) + '\n'
        else:
            return 'Матрицы разной разрядности'
        return text


matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(matrix1)
print('=====')
print(matrix1 + matrix2)
