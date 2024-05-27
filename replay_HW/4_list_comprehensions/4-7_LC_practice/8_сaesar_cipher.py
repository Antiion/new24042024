alpabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

text = 'это питон'#input('Введите текст: ')
cypher = ''
shift = int(input('Введите свдиг: '))
for symbol in text:
    if symbol.lower() in alpabet:
        cypher += alpabet[(alpabet.find(symbol.lower())+shift)%33]
    else:
        cypher += symbol
print(cypher)
