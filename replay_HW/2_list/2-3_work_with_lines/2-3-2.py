S = list(input('Введите строку: '))
index = int(input('Введите номер символа: '))

while abs(index) > len(S):
    print('Длина строки', len(S), 'символов.')
    index = int(input('Введите номер символа: '))

s_slice = S[index-2:index+1:]
print(f'Символ слева {s_slice[0]}\nСимвол справа {s_slice[2]}')

if s_slice.count(s_slice[1]) == 2:
    print('Есть еще один такой символ.')
elif s_slice.count(s_slice[1]) == 3:
    print('Все символы одинаковы.')
else:
    print('Таких символов больше нет.')
