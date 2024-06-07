while True:
    flag = 1
    ipaddress = input('Введите IP-адрес: ').split('.')
    # print(ipaddress)
    if len(ipaddress) != 4:
        print('Адрес — это четыре числа, разделённые точками.')
        continue
    for ip in ipaddress:
        if not ip.isdigit():
            print(f'{ip} - это не целое число.')
            flag = 0
            continue
        elif 0 > int(ip) or int(ip) > 255:
            print(ip, 'не в диапазоне 0-255')
            flag = 0
            continue

    if flag:
        print('IP-адрес корректен.')
        break

