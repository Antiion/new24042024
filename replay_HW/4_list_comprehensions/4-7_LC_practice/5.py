import random
# text_list = list(input("Введите строку: "))
text_list = list('sdfg')
print(text_list)

text_list.insert(random.randint(0, len(text_list)), 'h')
text_list.insert(random.randint(0, len(text_list)), 'h') #вставляем на случайные позиции еще 'h'
print(text_list)

l_side = text_list.index('h')
r_side = len(text_list) - text_list[::-1].index('h') - 1 #выясняем индексы крайних h

print('Развернутая последовательность между "h":', ''.join(text_list[l_side+1:r_side][::-1]))