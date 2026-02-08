import json
grades = {}


def add_student(name,marks):
    grades[name]=marks
    return grades

# name_st = input("введите имя:    ")
# grades_st = list(input("введите оценки: "))
# add_student(name_st,grades_st)

def add_marks():
    name = input("Введите имя:   ")
    new_marks = list(input("Введите оценки:   "))
    if name in grades:
        grades[name].extend(new_marks)
        print("Оценки обновленны")
        
# add_marks()

def save_file(filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(grades, file, ensure_ascii=False, indent=4)
    print("Данные успешно сохранены")

# save_file("test01")
    
def load_file(filename):
     with open(filename, 'r', encoding='utf-8') as file:
            global grades
            grades = json.load(file)
            print("Данные успешно загруженны")
            return grades
  
# load_file("test01")
# print(grades)


# load_file("test01")
# print(grades)

# add_marks()
# print(grades)

# save_file("test01")


def menu():
     while True:
        print("1 Загрузить")
        print("2 Добавить")
        print("3 Сохранить")
        print("4 Выход")
        
        choice= input("Ввод:  ")

        if choice == "1":
            name = input("введите имя файаладля загрузки:  ")
            load_file(name)
        elif choice == "2":
            add_marks()
        elif choice == "3":
            save =input("Введите имя для сохранения:    ")
            save_file(save)
        elif choice == "4":
            break

menu()
# print(grades)