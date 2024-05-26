cases_list = [165, 163, 160, 160, 157, 157, 154]

while True:
    weight_case = int(input('Введите вес контейнера: '))
    if 80 <= weight_case <= 200:
        break

cases_list.append(weight_case)
cases_list.sort()
cases_list = cases_list[::-1]
print(cases_list)
print('Номер нового контейнера:', cases_list.index(weight_case)+cases_list.count(weight_case))