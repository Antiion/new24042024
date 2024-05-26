n_list = input('Введите числа через пробел: ').split(' ')
n_list.sort()
print(list(int(i) for i in n_list))
