players_dict = {1: {'name': 'Vanya', 'team': 'A', 'status': 'Rest'},
                2: {'name': 'Lena', 'team': 'B', 'status': 'Training'},
                3: {'name': 'Maxim', 'team': 'C', 'status': 'Travel'},
                4: {'name': 'Egor', 'team': 'C', 'status': 'Rest'},
                5: {'name': 'Andrei', 'team': 'A', 'status': 'Training'},
                6: {'name': 'Sasha', 'team': 'A', 'status': 'Rest'},
                7: {'name': 'Alina', 'team': 'B', 'status': 'Rest'},
                8: {'name': 'Masha', 'team': 'C', 'status': 'Travel'}
                }
short = players_dict.values()
# print(short)

A_rest = [player['name'] for player in short if player.get('team') == 'A'
          and player.get('status') == 'Rest']
B_training = [player['name'] for player in short if player.get('team') == 'B'
          and player.get('status') == 'Training']
C_travel = [player['name'] for player in short if player.get('team') == 'C'
          and player.get('status') == 'Travel']

print(f'Все члены команды А, которые отдыхают: {", ".join(i for i in A_rest)}\n'
      f'Все члены команды B, которые тренируются: {", ".join(i for i in B_training)}\n'
      f'Все члены команды С, которые путешествуют: {", ".join(i for i in C_travel)}\n'
      )
