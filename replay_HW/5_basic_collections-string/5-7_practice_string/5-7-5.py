def num_check(line):
    line = str(line)
    check = -2
    for l in line:
        if l.isdigit():
            check += 1
    return check

def upup(line):
    line = str(line)
    up = 0
    for l in line:
        if l.isupper():
            up += 1
    return up

while True:
    password = input('Введите пароль: ')
    if len(password) > 7 and num_check(password) and upup(password):
        print('Это надежный пароль.')
        break
    print('Пароль ненадежный, попробуйте еще раз.')
