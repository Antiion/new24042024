# template = 'Здравствуйте, {0}! Ваш номер заказа: {1}. Приятного дня!'
# print(template.format(input('Имя: ').capitalize(), input('Номер заказа: ')))
#

# калькулятор для студентов

mem_sum = []
print("Чтобы выйти, введите только один символ и нажмите 'enter'\n"
      "Дробные числа вводятся через точку(.), например - 1.5")
while True:
    summ_ball = []
    balls = input('\nВведите баллы через пробел: ').split()
    if len(balls) == 1:
        break
    else:
        for b in balls:
            try:
                summ_ball.append(float(b))
            except ValueError:
                continue
        print(summ_ball)
        print('Сумма баллов:', sum(summ_ball))
        mem_sum.append(sum(summ_ball))

print('\nСписок всех сумм баллов:', mem_sum, end = '  ')
print('Вы вышли из калькулятора.')
# калькулятор для студентов
