import random

w = 80
rand_num= random.randint(1,80)
# print(rand_num)
rand_str = rand_num * "a"
len_str = len(rand_str)
# print(rand_str)
# print(len_str)

dif_w_len =  w - len_str
# print(dif_w_len)
print(dif_w_len*" ",rand_str)


