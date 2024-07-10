x = {chr(i) for i in range(48, 58)}
line = input('Введите строку: ')
# line = 'aas6dfg8sf0sdf30sdf'
line = set(line)
# print('Различные цифры в строке:', ', '.join(i for i in line.intersection(x)))
print('Различные цифры в строке:', ', '.join(i for i in line.intersection(x)))

