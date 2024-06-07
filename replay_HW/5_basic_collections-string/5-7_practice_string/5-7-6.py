import itertools
line = input('Введите строку: ')
new_line = []

counter = 0
for i in range(len(line)):
    counter += 1
    if line[i] != line[i+1:i+2]:
        new_line.append([line[i], counter])
        counter = 0
new_line = itertools.chain(*new_line)
print(*new_line, sep='')
