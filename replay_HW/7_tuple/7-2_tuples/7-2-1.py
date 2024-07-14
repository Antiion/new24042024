import random

cortege_1 = tuple(random.randint(0, 5) for _ in range(10))
cortege_2 = tuple(random.randint(-5, 0) for _ in range(10))
cortege_big = cortege_2 + cortege_1

print(cortege_big)
print(cortege_big.count(0))
