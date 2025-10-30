import random
import string
        
def random_str_letters_digits(lenght):


    charaters = string.ascii_letters + string.digits+string.punctuation
    random_text ="".join (random.choice(charaters) for _ in range(lenght))


    return random_text

