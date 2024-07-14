import random
llist_1 = [chr(random.randint(1072, 1103)) for _ in range(10)]
llist_2 = [chr(random.randint(1072, 1103)) for _ in range(10)]
print(f'Первый список: {llist_1}\n'
      f'Второй список: {llist_2}')

sym_dict_1 = {ind: sym for ind, sym in enumerate(llist_1)}
sym_dict_2 = {ind: sym for ind, sym in enumerate(llist_2)}
print(f'Первый словарь: {sym_dict_1}\nВторой словарь: {sym_dict_2}')