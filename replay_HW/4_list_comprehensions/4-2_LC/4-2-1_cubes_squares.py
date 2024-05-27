left_side = int(input('Введите левую границу: '))
right_side = int(input('Введите правую границу: '))
cubes_list = [i**3 for i in range(left_side, right_side+1)]
square_list = [i**2 for i in range(left_side, right_side+1)]
print(f'Список кубов чисел в диапазоне {left_side}->{right_side}: {cubes_list}')
print(f'Список квадратов чисел в диапазоне {left_side}->{right_side}: {square_list}')