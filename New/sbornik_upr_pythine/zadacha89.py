import random

random_numbers = random.randint(1,3)
print(random_numbers)

my_dickt = {"1":"один","2":"два","3":"три"}

def num2words (keys):
    if keys == 1:
        print(my_dickt.get("1"))
    elif keys ==2:
        print(my_dickt.get("2"))
    else:
        print(my_dickt.get("3"))
        return
print(num2words(random_numbers)) 
