guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f'Сейчас на вечеринке {len(guests)} человек: {', '.join(guests)}')
    move_guest = input('Гость пришел или ушел? ')
    if move_guest == 'stop':
        break
    elif move_guest.lower() not in ['пришел', 'пришёл', "ушел", "ушёл"]:
        print('Ошибка ввода. Попробуйте еще раз.')
        continue
    name_guest = input('Имя гостя: ')
    if move_guest.lower() in ['пришел', 'пришёл']:
        if len(guests)<6:
            guests.append(name_guest)
            print('Добро пожаловать', name_guest, '!')
        else:
            print(f'Извини {name_guest}, мест нет.')
    elif move_guest.lower() in ["ушел", "ушёл"]:





