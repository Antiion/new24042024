# text = input('Введите текст: ')
text = 'Вот такой вот текст'
text = list(text.lower())

def sym_counter(text_list):
    my_dic = {}
    for i_sym in text_list:
        if i_sym not in my_dic and i_sym != ' ':
            my_dic[i_sym] = text.count(i_sym)
    return my_dic

hist= sym_counter(text)
for sym in sorted(sym_counter(text).keys()):
    print(sym, ':', sym_counter(text)[sym])
print("Максимальная частота:", max(hist.values()))
