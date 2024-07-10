violator_songs = {'World in My Eyes': 4.86,
                  'Sweetest Perfection': 4.43,
                  'Personal Jesus': 4.56,
                  'Halo': 4.9,
                  'Waiting for the Night': 6.07,
                  'Enjoy the Silence': 4.20,
                  'Policy of Truth': 4.76,
                  'Blue Dress': 4.29,
                  'Clean': 5.83
                  }
# while True:
#     song_quant = int(input('Сколько песен выбрать? '))
#     if song_quant <= len(violator_songs):
#         break
#     else:
#         print(f'В списке всего {len(violator_songs)} песен. Вы не можете выбрать больше.')

# my_songs = {input(f'Введите название {i_num}-ой песни:')
#             for i_num in range(1, song_quant+1)
#             }
my_songs = {'Enjoy the Silence', 'Halo', 'Clean'}
my_songs = my_songs.intersection(set(violator_songs.keys()))
my_songs = {i_song: violator_songs[i_song] for i_song in my_songs}

print(f'Список песен: {my_songs}\n'
      f'Общее время звучания: {sum(my_songs.values())}')
