import json
grades = {}

def add_student(name,marks):
    grades[name]=marks
    return grades

def add_marks(name,new_marks):
    if name in grades:
        grades[name].extend(new_marks)

def save_file(filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(grades, file, ensure_ascii=False, indent=4)
    print("Данные успешно сохранены")

def load_file(filename):
     with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
  

# name_st = input("введите имя:    ")
# grades_st = list(input("введите оценки: "))
# add_student(name_st,grades_st)

# grades_1 = list(input("введите оценки: "))


# save_file("test01")
zagruzka = load_file("test01")
print(zagruzka)
# print(grades)