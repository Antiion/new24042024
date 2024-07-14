line = input('Введите строку: ')
# line = 'so~mec~od~e'

print('Ответ:', *[i for i, sym in enumerate(line) if sym == '~'])
