# three_words = [input(f'Введите {i}-е слово:') for i in range(1, 4)]
three_words = ['я', 'ты', "мы"]
text = input("Введите текст: ").lower().split()

for tw in three_words:
    print(f'{tw} встречается в тексте {text.count(tw)}')
# print(text)