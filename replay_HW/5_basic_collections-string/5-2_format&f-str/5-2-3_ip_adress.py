ip_address = '{0}.{1}.{2}.{3}'
ip_list = []
for i in range(1, 5):
    num = int(input(f'Введите {i}-е число адреса: '))
    while num<0 or num>255:
        num = int(input('Число должно быть в диапазоне 0-255.\n'
                        'Введите число еще раз: ')
                  )

    ip_list.append(num)

print(ip_address.format(ip_list[0], ip_list[1], ip_list[2], ip_list[3]))
