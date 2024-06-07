# path = input(('Введите путь к файлу: '))
path = 'C:/user/docs/folder/new_file.txt'
disk = input('На каком диске должен лежать файл: ')
file_ext = input('Расширение файла: ')

if path.startswith(disk.upper()) and path.endswith(file_ext.lower()):
    print('Путь корректен.')
else:
    print('Неправильный путь.')