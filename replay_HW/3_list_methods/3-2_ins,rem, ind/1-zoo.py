zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
zoo.insert(1, 'bear')
zoo.remove('elephant')
print('Зоопарк:', zoo)
print('Лев в клетке №', zoo.index('lion')+1)
print('Обезьяна в клетке №', zoo.index('monkey')+1)
