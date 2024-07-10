order = {'apple': 2, 'banana': 3, 'pear': 1, 'watermelon': 10, 'chocolate': 5}#товар\кг
incomes = {'apple': 5600.20, 'orange': 3500.45, 'banana': 5000.00,
           'bergamot': 3700.56, 'durian': 5987.23, 'grapefruit': 300.40,
           'peach': 10000.50, 'pear': 1020.00, 'persimmon': 310.00
           } #товар\цена

my_dic = {}
for i_key in order:
    if incomes.get(i_key):
        my_dic[i_key] = order[i_key] * incomes[i_key]
    else:
        my_dic[i_key] = 0

print(my_dic)

