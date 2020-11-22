# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход).
# Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
# и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных
# (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": 35000, "bonus": 15000}


class Position(Worker):
    def get_full_name(self):
        return self.name

    def get_total_income(self):
        income = sum([y for x, y in self._income.items()])
        return income


director = Position('Александр', 'Смирнов', 'Директор')
print(director.get_full_name())
print(director.get_total_income())


# на заметку:
# получилось заюзать генератор из 6ой задачки прошлого урока)))
