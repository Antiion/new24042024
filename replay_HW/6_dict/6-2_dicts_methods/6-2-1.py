small_storage = {'гвозди': 5000, 'шурупы': 3040, 'саморезы': 2000}
big_storage = {'доски': 1000, 'балки': 150, 'рейки': 600}
big_storage.update(small_storage)
# print(big_storage)
request = input('Введите название товара: ').lower()
if big_storage.get(request):
    print((big_storage.get(request)))
else:
    print('Такого товара нет на складе.')
