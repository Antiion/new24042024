def sym_counter(anytext): #создание словаря {символ: кол-во}
    sym_dict = {}
    for sym in anytext:
        if sym not in sym_dict:
            sym_dict[sym] = 1
        else:
            sym_dict[sym] += 1
    return (sym_dict)
def invertor(anydict):
    invert_dict = {}
    for i_sym in anydict:
        if anydict[i_sym] not in invert_dict:
            invert_dict[anydict[i_sym]] = str(i_sym)
        else:
            invert_dict[anydict[i_sym]] += str(i_sym)
    return invert_dict

text = list(input('Введите текст: '))
for i in sym_counter(text):
    print(i, ':', sym_counter(text)[i])

print('Инвертированный словарь частот:')
for ii in set(invertor(sym_counter(text))):
    print(ii, ':', list(invertor(sym_counter(text))[ii]))



