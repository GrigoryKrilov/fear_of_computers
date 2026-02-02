""" забракованнно 
# черновик задачи со словарем

dict={}
while True:
    qua_1 = input("начнем выполнение  программы: 1-да:    ")
    if qua_1 == "1":
        print("начали!")
    else:
        print("конец!")
        break
    while True:
            print("начало цикла")
            stud = input("введите имя студента:         ")
            while True:
                    grades =int(input("введите его оценку:    "))
                    dict[stud]= []
                    dict[stud].append(grades)
                    qua = input("все?:1-да: ")
                    if qua == "1":
                        break
                    else:
                        continue
            qua_3 = input("хотите добавить еще оценку?: да-1:")
            if qua_3 == "1":
                new_grades = int(input("введите новую оценку: "))
                dict[stud].append(new_grades)
                

            print("конец!")
            break
        

print(dict)

