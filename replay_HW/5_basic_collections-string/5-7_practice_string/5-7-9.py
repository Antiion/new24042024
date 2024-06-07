def caplow(line):
    line = str(line)
    cap, low = 0, 0
    for i in line:
        if i.islower():
            low += 1
        elif i.isupper():
            cap += 1
    return cap, low

line = input('Введите строку: ')
print('Количество заглавных букв: {}\n'
      'Количество строчных букв: {}'.format(caplow(line)[0], caplow(line)[1]))
