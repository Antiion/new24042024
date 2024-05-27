import random

original_prices = [random.randint(-20, 20) for _ in range(5)]
print(original_prices)
new_prices = [i if i >=0 else 0 for i in original_prices]
print('Мы потеряли:', abs(sum(original_prices) - sum(new_prices)))