import random
n_list = [i+1 for i in range(10)]
l_side = random.randint(0, 9)
r_side = random.randint(l_side, 9)
print(n_list, n_list[l_side:r_side])
n_list[l_side:r_side] = ''
print(n_list)