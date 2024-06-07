text = input('Введите текст: ')
text = text.split()
if len(text) == 1:
    print(f'Самое длинное слово: {text[0]}'
          f'\nДлина слова: {len(text)} символ(ов)')
else:
    sym_count, big_word = 0, ''
    for word in text:
        if len(word) >= sym_count:
            sym_count = len(word)
            big_word = word
    print(f'Самое длинное слово: {big_word}'
          f'\nДлина слова: {sym_count} символ(ов)')


