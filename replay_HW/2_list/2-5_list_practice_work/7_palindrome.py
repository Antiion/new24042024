word = input('Введите слово: ')

flag = True
for i in range(len(word)//2):
    print(word[i], word[-i - 1])
    if word[i] != word[-i-1]:
        flag = False
        break

if flag:
    print('Слово является палиндромом.')
else:
    print('Слово не является палиндромом.')