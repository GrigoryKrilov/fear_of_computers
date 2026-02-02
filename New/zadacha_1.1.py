import json

grades = {}

def add_student(name,marks):
    grades[name]=marks
    return grades

# def add_marks(name,new_marks):
#     if name in grades:
#         grades[name].extend(new_marks)

def save_file(filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(grades, file, ensure_ascii=False, indent=4)
    print("Данные успешно сохранены")


name_st = input("введите имя:    ")
grades_st = list(input("введите оценки: "))
add_student(name_st,grades_st)

# grades_1 = list(input("введите оценки: "))


print(grades)
save_file("test01")