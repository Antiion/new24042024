text = input('Введите текст: ')
lower_count, upper_count = 0, 0
for t in text:
    if t.islower():
        lower_count += 1
    elif t.isupper():
        upper_count += 1

if lower_count > upper_count:
    print(text.lower())
else:
    print(text.upper())
