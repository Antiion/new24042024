user_line = input('Введите строку: ').lower()
sym_list = list(user_line)

check = 0
for i_sym in set(sym_list):
    if sym_list.count(i_sym)%2 != 0:
        check += 1
    if check > 1:
        print('Нельзя сделать полиндромом.')
        break
else:
    print('Можно сделать полиндромом')