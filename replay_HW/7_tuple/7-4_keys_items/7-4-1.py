# my_dict = {chr(i).upper(): i-1070 for i in range(1072, 1077)}
# print(my_dict)
#
# for ind, sym in (my_dict.items()):
#     print(ind, sym)

incomes = {'apple': 5600.20, 'orange': 3500.45, 'banana': 5000.00,
           'bergamot': 3700.56, 'durian': 5987.23, 'peach': 10000.50,
           'pear': 1020.00, 'persimmon': 310.00
           }
for name, cost in incomes.items():
    print(f'{name} -- {cost}')
