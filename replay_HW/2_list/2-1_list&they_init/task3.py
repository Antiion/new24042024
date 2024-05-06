worker_count = input('Введите кол-во сотрудников в офисе: ')
workers =[int(input("ID сотрудника: ")) for _ in range(int(worker_count))]
search = int(input('Какой ID ищем: '))
if search in workers:
    print('Сотрудник на работе.')
else:
    print("Сотрудник не работает!")
