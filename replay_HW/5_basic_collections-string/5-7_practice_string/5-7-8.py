line_1 = input('Введите первую строку: ')
line_2 = input('Введите вторую строку: ')

counter, flag = 0, 1
if len(line_2) == len(line_1):
    for l in range(len(line_1)):
        if line_1[counter:]+line_1[0:counter] == line_2:
            print(f'Строку {line_2} можно получить из {line_1}'
                  f'\nСдвиг на {counter}')
            flag = 0
        counter += 1
elif len(line_2) != len(line_1) or flag:
    print(f'Строку {line_2} нельзя получить из {line_1}')
