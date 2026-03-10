import random
dict_numwords = {'first': 1,'second': 2,'third': 3,'fourth': 4,'fifth': 5,'sixth': 6,'seventh': 7,'eighth': 8,'ninth': 9}


words = ["first", "second", "third", "fourth" ,"fifth" ,"sixth" ,"seventh" ,"eighth" ,"ninth" ]
random_words = [random.choice(words) for _ in range(30)]

uniqule_words = list(set(random_words))
sorted_words = sorted(uniqule_words, key=lambda x: dict_numwords[x])

print(sorted_words)
