ppl_amount = 5#int(input('Количество человек в кругу: '))
people_list = [i + 1 for i in range(ppl_amount)]
remove_num = 2#int(input('Какое число в считалке? '))
print(f'Выбывает каждый {remove_num}-й человек')

start_num = 0
for i in range(ppl_amount-1):
    print('Текущий круг людей:', people_list)
    num_del = (start_num+remove_num-1) % len(people_list)
    # print('Индекс удаления:', num_del)
    # print('Удаляемое число:', people_list[num_del])
    print('Выбывает человек под №', people_list.pop(num_del))
    start_num = num_del
    print()

print('Остался человек №', *people_list)