a_list = [1, 5, 3]
b_list = [1, 5, 1, 5]
c_list = [1, 3, 1, 5, 3, 3]
a_list.extend(b_list)
five = a_list.count(5)
for _ in range(a_list.count(5)):
    a_list.remove(5)
a_list.extend(c_list)
three = c_list.count(3)
print(f'Количество цифр 5 при первом объединении: {five}\nКоличество цифр 3 при втором объединении: {three}')
print(a_list)
