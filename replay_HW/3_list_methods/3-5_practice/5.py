violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
song_amount = int(input('Сколько песен выбрать? '))
user_songs = [input(f'Название {i+1}-й: песни: ') for i in range(song_amount)]
print(user_songs)
play_sum = 0
playlist = []
for us in user_songs:
    for vs in violator_songs:
        if us.lower() == vs[0].lower():
            flag = 0
            play_sum += vs[1]
            playlist.append(vs[0])
    if flag:
        print(f'Песни {us} нет в списке.')
print(f'Плейлист: {playlist}\nВремя звучания: {play_sum}')


