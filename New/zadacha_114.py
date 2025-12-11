import random

random_num = [random.randint(-100, 100) for _ in range(10)]
zero = 0
random_num.append(zero)
# print(random_num)

sordet_numbers = sorted(random_num)
print(sordet_numbers)