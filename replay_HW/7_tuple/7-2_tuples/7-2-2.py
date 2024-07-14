import math

def side_full(r, h):
    side = 2 * math.pi * r * h
    full = side + 2 * math.pi * r**2
    return (side, full)

r = float(input('Введите радиус: '))
h = float(input('Введите высоту: '))

quest = side_full(r, h)
print(f'Площадь боковой поверхности цилиндра: {quest[0]}\n'
      f'Полная площадь поверхности цилиндра: {quest[1]}')
