syms_ban = ['@', '№', '$', '%', '^', '&', '*', '(', ')']
extension = ['.docx', '.txt']
file_name = input('Введите название файла: ')

flag = 1
for i in syms_ban:
    if file_name.startswith(i):
        print('Ошибка: название начинается недопустимым символом.')
        flag = 0
        break
if flag:
    if file_name.endswith(extension[0]) or file_name.endswith(extension[1]):
        print('Файл назван верно.')
    else:
        print('Неверное расширение файла, допускается только .txt или .docx')