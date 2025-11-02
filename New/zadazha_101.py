# 3 буквы 3 цифры
# 4 цифры 3 буквы
# генерация 50\50 

import random
import string

def random_sign_car_2_times(quantity_sign_car):
    for i in range(quantity_sign_car//2):
        digits = "".join([str(random.randint(0,9)) for _ in range(3)])
        latters = "".join([random.choice(string.ascii_uppercase) for _ in range(3)])
        results= digits + latters
        
        digits_1 = "".join([str(random.randint(0,9)) for _ in range(4)])
        latters_1 = "".join([random.choice(string.ascii_uppercase) for _ in range(3)])
        results_1= digits_1 + latters_1
        print("первый знак",results,"второй знак",results_1)
        

print(random_sign_car_2_times(10))
