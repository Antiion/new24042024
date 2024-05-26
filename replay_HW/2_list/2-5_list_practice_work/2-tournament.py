name_list = 'Артемий, Борис, Влад, Гоша, Дима, Евгений, Женя, Захар'.split(', ')
print(*(i for i in name_list if name_list.index(i)%2==0))
