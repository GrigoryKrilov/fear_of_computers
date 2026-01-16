# задача с словарем.
my_dit_stud_grd = {}

while True:
    new_student = input("имя студента:   ")
    while True:
        new_grades =int(input("введите оценки:   "))
        list_grades = []
        list_grades.append(new_grades)
        qua_0 = input("продолжим ?: 0 1")
        if qua_0 == "1":
            print("продолжаем")
            continue
            
        else:
            my_dit_stud_grd[new_student]=list_grades
            print("закончили!")
            break
    
    qua_1 = input("вводим новое имя 0 1:")
    if qua_1 == 1:
        print("продолжаем")
        continue
    else:
        print("закончили")
        break
print(my_dit_stud_grd)

