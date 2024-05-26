n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in n_list:
    if i % 2 != 0:
        n_list.remove(i)
print(n_list)
# temp_str = '' # первый вариант
# for _ in range(len(n_list)):
#     temp_str += str(n_list.pop(-1))
#     # print(n_list.pop(-1), end=' ')
# print(list(temp_str))

# print(sorted(n_list, reverse=True)) #второй вариант


n_list.sort(key=lambda a: -a)
print(n_list)


