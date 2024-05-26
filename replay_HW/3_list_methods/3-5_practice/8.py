# list1 = [1, 2, 3, 4, 5]
user_len = int(input('Количество чисел в списке: '))
list1 = [int(input('Введите число: ')) for _ in range(user_len)]
print(list1)

len_list = len(list1)
i = 0
while list1 != list1[::-1]:
    x = list1[i]
    list1.insert(len_list, x)
    print(list1)
    i += 1

print('Нужно приписать чисел:', i)
print('Симметричный список:', list1)