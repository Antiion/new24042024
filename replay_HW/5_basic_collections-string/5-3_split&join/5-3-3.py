# reference = input('Введите шаблон поздравления, используя {name}{age}: ')
reference = 'Дорогой {name}, поздравляю с {age}-летием!'


name = input('Введите имена через запятую: ').split(', ')
age = input('Введите возрасты через пробел: ').split()

for i in range(len(name)):
    print(reference.format(name=name[i], age=age[i]))

# print(','.join([' '.join([name[i], age[i]]) for i in range(len(name))]))
print(*[' '.join([name[i], str(age[i])]) for i in range(len(name))], sep=', ')

