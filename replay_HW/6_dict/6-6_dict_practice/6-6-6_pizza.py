orders_quant = int(input('Введите кол-во заказов: '))
total_order = dict()

print('Заказы вводить по схеме "Фамилия Название пиццы Кол-во"')
for i_order in range(orders_quant):
    order = input(f'{i_order+1}-ый заказ: ').split()
    # order[0] - Фамилия, order[1]-Название пиццы, order[2] - Кол-во пицц
    if order[0].capitalize() not in total_order:
        total_order[order[0]] = {order[1].capitalize(): int(order[2])}
    else:
        if order[1].capitalize() in total_order[order[0].capitalize()]:
            # print(total_order[order[0]])
            total_order[order[0].capitalize()][order[1].capitalize()] += int(order[2])
        else:
            total_order[order[0].capitalize()].update({order[1].capitalize(): int(order[2])})

for to in total_order:
    print(f'{to}: ', end = '')
    for i_to in total_order[to]:
        print(f'{i_to}: {total_order[to][i_to]}')
        print(' '*len(to)+2*' ', end = '')
    print()

# test_ord = {'Лохов': {'Чиз': 5, 'Люкс': 4}, 'Иванов': {"Мясная": 3, "Люкс": 5}}