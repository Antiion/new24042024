worker_amount = int(input('Введите кол-во сотрудников: '))
sal_list = []
for wa in range(worker_amount):
    sal = int(input(f'Введите зарплату {wa+1} сотрудника: '))
    if sal != 0:
        sal_list.append(sal)

print(f'Осталось сотрудников: {len(sal_list)}\nЗарплатный лист: {sal_list}')

