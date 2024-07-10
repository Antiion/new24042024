phone_book = dict()
while True:
    name_inp = input('Введите имя: ')
    if name_inp != '':
        if name_inp not in phone_book:
            phone_book[name_inp] = int(input('Введите номер телефона: '))
        else:
            print('Имя уже занято, переименуйте контакт: ')
            continue
        for i_name in phone_book:
            print(f'{i_name} - {phone_book[i_name]}')
    else:
        break
