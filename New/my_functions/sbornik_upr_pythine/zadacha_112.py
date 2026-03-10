# избавиться от экстремально низких и высоких значений.
# создать копию списка.

import random

list_random = [random.randint(0,100) for _ in range(4)]
# print(list_random)
list_random_copy = list_random.copy()
print(list_random_copy)
sorted_list_num = sorted(list_random_copy)
print(sorted_list_num)
del sorted_list_num[-1]
del sorted_list_num[0]
print(sorted_list_num)
