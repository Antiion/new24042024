import random
def totwo(x):
    return round(x, 2)

# prices_list = [float(input('Введите цену на товар: ')) for _ in range(5)]
prices_list = [totwo(random.uniform(1, 100)) for _ in range(5)]
print(prices_list)
inc_1year = 0#int(input('Процент повышения цен за первый год: '))
inc_2year = 10#int(input('Процент повышения цен за второй год: '))
print('Повышение цен за 1-й год:', [totwo(i+i*inc_1year/100) for i in prices_list])

