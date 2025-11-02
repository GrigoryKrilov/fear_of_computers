# проверить строку на  8 символов 1 буква вверхрег 1 цифра 1 буква в ниж реги

import random
import string

# def random_password(len_pass):
datchik = True
while  datchik :

    diggits = "".join ([str(random.randint(0,9)) for _ in range(random.randint(0,5))])
    latters_down = "".join ((random.choice(string.ascii_letters)) for _ in range(random.randint(0,5)))
    latters_up = "".join ((random.choice(string.ascii_uppercase)) for _ in range(random.randint(0,5)))
    results = diggits + latters_down + latters_up
    if 15 > len(results) > 8:
        datchik = False
        

print(results)
print(len(results))