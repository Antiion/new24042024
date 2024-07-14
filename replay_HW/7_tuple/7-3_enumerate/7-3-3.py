def even(anyiterobj):
    evenlist = [obj for ind, obj in enumerate(anyiterobj) if ind % 2 == 0]
    return evenlist

# user_inp =  'О Дивный Новый мир!'
user_inp =  [100, 200, 300, 'буква', 0, 2, 'а']

print("Результат:", even(user_inp))