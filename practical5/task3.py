# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
def average_income(staff):
    income = 0
    for i, employee in enumerate(staff):
        salary = employee.split()
        if int(salary[1]) > 20000:
            income += int(salary[1])
            print(salary[0])
    print(f'Средний доход сотрудников: {income / (i + 1)}')


f_obj = open('../practical5/task3.txt', encoding='utf-8')
staff = f_obj.readlines()
average_income(staff)
