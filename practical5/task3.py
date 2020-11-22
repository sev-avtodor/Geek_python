# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
def average_income(staff):
    income = 0
    for i, employee in enumerate(staff, start=1):
        salary = employee.split()
        if int(salary[1]) > 20000:
            income += int(salary[1])
            print(salary[0])
    print(f'Средний доход сотрудников: {income / i}')


f_obj = open('../practical5/task3.txt', encoding='utf-8')
staff = f_obj.readlines()
average_income(staff)

# образец решения:
# with open('../practical5/task3.txt', encoding='utf-8') as f:
#     salaries = []
#     lines = f.readlines()
#     for line in lines:
#         name, salary = line.split()
#         salaries.append(int(salary))
#         if int(salary) < 20000:
#             print(line, end='')
#     print('\nСредняя зарплата: ', sum(salaries) / len(salaries))

# на заметку:
# забываю использовать конструкцию открытия файла
# парамент принта end на заметку
