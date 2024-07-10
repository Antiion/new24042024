def invertor(anydict):
    invert_dict = {}
    for i_sym in anydict:
        if anydict[i_sym] not in invert_dict:
            invert_dict[anydict[i_sym]] = str(i_sym)
        else:
            invert_dict[anydict[i_sym]] += str(i_sym)
    return invert_dict

couple_quant = int(input('Введите кол-во пар синонимов: '))
synonym = {}
for i in range(couple_quant):
    pair = input(f'{i+1}-ая пара синонимов: ').split('-')
    synonym[pair[0].strip()] = pair[-1].strip()

# synonym = {"Емкость": "Тара", "Тарелка": "Миска", "Друг": "Товарищ"}
synonym.update(invertor(synonym))
#Теперь реализуем поиск по словарям
user_word = input('Введите слово с большой буквы: ')
if synonym.get(user_word):
    print('Синоним -', synonym.get(user_word))
else:
    print('Синонима вашему слову не найдено.')