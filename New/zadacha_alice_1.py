# задача с словарем.
my_dit_stud_grd = {}
i=True

while i: 
    new_student = input("введите имя студента: ")
    new_grades =  int(input ("введите его оценки:   "))
    my_dit_stud_grd[new_student]=new_grades
    qua = input("прод n нет: ")
    if qua == "n":
        i = False
    else:
        continue



print(my_dit_stud_grd)
