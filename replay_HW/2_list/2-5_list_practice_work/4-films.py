films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
count_film = int(input('Сколько фильмов хотите добавить? '))
user_films = []
for _ in range(count_film):
    name_film = input('Введите название фильма: ').capitalize()
    if name_film in films:
        user_films.append(name_film)
    else:
        print('К сожалению такого фильма нет в нашей библиотеке.')
print('Список любимых фильмов:', end=' ')
print(*(user_films), sep=',')
