three_words = input('Введите три слова через пробел: ').split(' ')
# print(three_words)
text = input('Введите текст:')

punc_marks = ['.', ',', '!', '?', ';', ':', '-']
for i in punc_marks:
    text = text.replace(i, '')
text = text.replace('  ', ' ').split(' ')
# print(text)

print('Подсчет слов в тексте.')
for i1 in three_words:
    print(f'{i1}: {text.count(i1)} раз')
