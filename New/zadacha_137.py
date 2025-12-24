import random

dict_mach = {}
i=0
while i < 10:
    random_dice_1 = random.randint(1,12)
    random_dice_2 = random.randint(1,12)
    summ_d1_d2 = random_dice_1 +random_dice_2
    
    if random_dice_1 not in dict_mach:
        dict_mach[random_dice_1] = random_dice_2
        i = i+1
    else:
        continue

print(dict_mach)

