import random

num_list = [random.randint(-20, 20) for _ in range(10)]
print(num_list)
print(f'Минимальное число в списке: {sorted(num_list)[0]}\nМаксимальное число в списке: {sorted(num_list)[-1]}')
