def value_min(anydict):
    id_min = list(anydict.keys())[0]
    for i_d in anydict:
        if anydict[i_d] < anydict[id_min]:
            id_min = i_d
    return id_min

incomes = {'apple': 5600.20, 'orange': 3500.45, 'banana': 5000.00,
           'bergamot': 3700.56, 'durian': 5987.23, 'grapefruit': 300.40,
           'peach': 10000.50, 'pear': 1020.00, 'persimmon': 310.00,
           }

print(f'Общий доход составил {sum(incomes.values())} руб\n'
      f'Самый маленький доход у {value_min(incomes)}. '
      f'Он составляет {incomes.pop(value_min(incomes))} руб\n'
      f'Итоговый словарь: {incomes}')
