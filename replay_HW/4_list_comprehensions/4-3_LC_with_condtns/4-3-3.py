squad1 = [77, 75, 76, 77, 76, 73, 57, 67, 76, 52]
squad2 = [53, 51, 31, 60, 49, 37, 31, 60, 37, 47]
hero_squad = ['Погиб' if squad1[i]+squad2[i] >= 100
              else 'Выжил'
              for i in range(10)
              ]
print(hero_squad)
