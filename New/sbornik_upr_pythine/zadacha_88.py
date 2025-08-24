import random
my_list = []
random_list = [random.randint(1,100) for i in range (random.randint(1,100)) ]

while len(my_list) < random.randint(1,100): 
    chislo = random.randint(0,99)
    my_list.append(chislo)
    if len(my_list) == chislo:
        print("")

        

# print(my_list)


def mediana_trex_chisel (a):
    
    sorted_list = sorted(my_list)
    chet_nechet_list = len(my_list)
    if chet_nechet_list % 2 == 0:
        print("четное")
        

    else:
        print("не четное")
    print(chet_nechet_list)
    return sorted_list 

print(mediana_trex_chisel(my_list))
