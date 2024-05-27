text = 'Нужно отнести кольцо в Мордор!'
vowels = 'аеёиоуэюя'
vow_list = [i for i in text if i.lower() in vowels]
print(vow_list)
print('Количество гласных в тексте:', len(vow_list))
