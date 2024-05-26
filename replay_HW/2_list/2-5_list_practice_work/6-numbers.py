numb_list = [int(i) for i in '12345']
print(numb_list)
shift = int(input('Введите сдвиг: '))
new_list = numb_list[-shift::]
new_list.extend(numb_list[:-shift:])
print(new_list)
