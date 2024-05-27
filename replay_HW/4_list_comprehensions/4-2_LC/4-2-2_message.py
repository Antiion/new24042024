line = 'hello'#input('Введите строку: ')
symbol = '!'#input('Введите дополнительный символ: ')
double = [i*2 for i in line]
print('Список удвоенных символов:', double)
print('Список с дополнительным символом:', [i+symbol for i in double])
