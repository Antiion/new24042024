list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 5, 6, 8, 10]

def merged(list1, list2):
    for i in list2:
        if i not in list1:
            list1.append(i)
    list1.sort()
    return list1

print(merged(list1, list2))