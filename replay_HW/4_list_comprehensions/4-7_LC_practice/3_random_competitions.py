import random

def totwo(x):
    return round(x, 2)

team1 = [totwo(random.uniform(5, 10)) for _ in range(20)]
team2 = [totwo(random.uniform(5, 10)) for _ in range(20)]
print(f'Первая команда: {team1}'
      f'\nВторая команда: {team2}')
winners = [max(team2[i], team1[i]) for i in range(20)]
print('Победители тура:', winners)