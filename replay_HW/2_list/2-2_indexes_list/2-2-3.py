n_list = [0, 1, 10, 3, 4, 5]

maxx, minn = max(n_list), min(n_list)
index_max = n_list.index(maxx)
index_min = n_list.index(minn)
n_list.remove(maxx)
n_list.insert(index_max, minn)
n_list.remove(minn)
n_list.insert(index_min, maxx)
print(n_list)
