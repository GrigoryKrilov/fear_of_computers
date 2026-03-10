import random 
import string
my_dict = {}
i = 0
while i <= 10 :
        random_key = random.choice(string.ascii_letters)
        random_value = random.randint(1,100)

        my_dict[random_key] = random_value

        i = i + 1
print(my_dict)


def find_keys(my_dict_1):
    key_list = list(my_dict_1.keys())
    return key_list

print(find_keys(my_dict))