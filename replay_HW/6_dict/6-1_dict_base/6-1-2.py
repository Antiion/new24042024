# student_inp = input('Введите ваши данные через пробел\n'
#                      '(Имя Фамилия Город Место учебы Оценки):')

student_inp = 'Антон Соколов Москва МГУ 5 6 7 8 9 9'
student_list = student_inp.split()
# print(student_list)
student_dict = dict()
student_dict['Имя'] = student_list[0]
student_dict['Фамилия'] = student_list[1]
student_dict['Город'] = student_list[2]
student_dict['Место учебы'] = student_list[3]
student_dict['Оценки'] = []
for i_ball in student_list[4:]:
    student_dict['Оценки'].append(int(i_ball))

for i_key in student_dict:
    print(f'{i_key} - {(student_dict[i_key])}')

