n = int(input('Сколько чисел будем вводить? '))
num_list = [int(input(f'Введите {i+1} число: ')) for i in range(n)]
divisor = int(input('Введите делитель: '))

index, ind_summ, flag = 0, 0, 1

print(num_list)

for i in num_list:
    if i%divisor == 0:
        print(f'Индекс числа {i}: {index}')
        ind_summ += index
        flag = False
    index += 1

if flag:
    print('В списке нет чисел, кратных', divisor)
else:
    print('Сумма индексов =', ind_summ)
