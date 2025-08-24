#         # file:///C:/Users/user/Desktop/обучение/Python%20Сборник%20упражнений-1.pdf
# # задача 84

import random
import statistics

g = 0

middle_value = []
while g < 10:
    my_list=[]

    i = True

    while i :
        result = random.randint(0,1)
        if result == 1:
            result = "р"
        else:
            result = "о" 

        my_list.append(result)

        serch_recka = my_list.count("р")
        serch_orel = my_list.count("о")


        
        dlina_list= len(my_list)
        for j in range(dlina_list-2):
            if my_list[j] == my_list[j+1] == my_list[j+2]:
                generator_true_flase = True
                print(my_list[j],my_list[j+1],my_list[j+2])
                i = False
                count_1 = len(my_list)
                middle_value.append(count_1)
                print(my_list,"количество попыток",count_1)
                average = statistics.mean(middle_value)
            
                g = g+1
            
print("среднее значение",(round(average)))

