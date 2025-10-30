# я хочу создать функцию которая будет вынимать из мтроки только цифры и превращать их в другой тип данных int

import random
import string
        
def random_str_letters_digits(lenght):


    charaters = string.ascii_letters + string.digits+string.punctuation
    random_text ="".join (random.choice(charaters) for _ in range(lenght))


    return random_text

text = random_str_letters_digits(50)

digits = ""

for i in text:
    if i.isdigit():
        digits += i
        
print(digits)
print(type(digits))