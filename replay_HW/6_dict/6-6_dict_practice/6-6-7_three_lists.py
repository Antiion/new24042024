array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
print("Элементы, которые есть в каждом списке")
print('Решение с множествами:',
      set(array_3).intersection(set(array_2)).intersection(set(array_1))
      )

inter_array = []
for el_a1 in array_1:
    if el_a1 in array_2 and el_a1 in array_3:
        inter_array.append(el_a1)
print('Решение без множеств:', inter_array)

print("Элементы, которые есть только в первом списке")
print("Решение с множествами:",
      (set(array_1).difference(set(array_2))).difference(set(array_3))
      )

only_array1 = []
for i_oa1 in array_1:
    if i_oa1 not in (array_3 and array_2):
        only_array1.append(i_oa1)
print('Решение без множеств:', only_array1)