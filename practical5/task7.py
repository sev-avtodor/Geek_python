# 7. Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

list_firm = []
firm = {}
firm_nonprofit = {}
average_profit = {'average_profit': 0}

with open('../practical5/task7.txt', encoding='utf-8') as f:
    while True:
        for line in f.readlines():
            line = line.rstrip().split()
            profit = int(line[2]) - int(line[3])
            if profit > 0:
                firm[line[0]] = profit
                average_profit['average_profit'] = average_profit['average_profit'] + profit
            else:
                firm_nonprofit[line[0]] = profit
        average_profit['average_profit'] = average_profit['average_profit'] / (len(firm) + len(firm_nonprofit))
        list_firm.append(firm)
        list_firm.append(firm_nonprofit)
        list_firm.append(average_profit)
        break

with open('../practical5/task7.json', 'w') as fj:
    json.dump(list_firm, fj)

print(list_firm)


# образец:
# import json
#
# firm_dict = {}
# average_profit = []
# with open('../practical5/task7.txt') as f:
#     lines = f.readlines()
#     for line in lines:
#         name, form, revenue, costs = line.split()
#         profit = int(revenue) - int(costs)
#         firm_dict[name] = profit
#         if profit > 0:
#             average_profit.append(profit)
#
# average_profit = sum(average_profit) / len(average_profit)
# out_info = [firm_dict, {'average_profit': average_profit}]
#
# with open('../practical5/task7.json', 'w') as f_json:
#     json.dump(out_info, f_json)
#
# with open('../practical5/task7.json') as f_json:
#     print(json.load(f_json))


# на заметку:
# забыл про возможность указать соответствие переменным при split
# разобрать формирование списка в примере