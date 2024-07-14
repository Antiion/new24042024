# phone_book = dict()
#
# while True:
#     new_contact = input('Введите Фамилия Имя Номер: ').split()
#     if new_contact == []:
#         break
#     # print(new_contact)
#     # print(fam_name)
#     if len(new_contact) == 3:
#         fam_name = tuple(str(fn).capitalize() for fn in new_contact[0:2])
#         number = new_contact[2]
#         while fam_name in phone_book or len(fam_name) != 2:
#             print('Такой контакт уже есть. Поменяйте имя или фамилию')
#             fam_name = (input('Введите Фамилия Имя: ').split())
#             fam_name = tuple(str(fn).capitalize() for fn in fam_name)
#         while not number.isdigit():
#             print('Неверно введен номер. Введите номер еще раз:', end=' ')
#             number = input()
#         phone_book[fam_name] = int(number)
#         for i_cont in phone_book.items():
#             print(f'{" ".join(ic for ic in i_cont[0])} -- {i_cont[1]}')
#             continue
#     else:
#         print('Исправьте ввод.')
#     print()

name = ['Tom', 'Albert', 'Anton']
age = [45, 33, 32]
new = dict(zip(name, age))
print(new)
