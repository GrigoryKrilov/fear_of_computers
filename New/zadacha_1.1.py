import json
grades = {}


def add_student(name,marks):
    grades[name]=marks
    return grades


def add_marks():
    name = input("Введите имя:   ")
    new_marks = list(input("Введите оценки:   "))
    if name in grades:
        grades[name].extend(new_marks)
        print("Оценки обновленны")
        return print(grades)
        
def save_file(filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(grades, file, ensure_ascii=False, indent=4)
    print("Данные успешно сохранены")
    return print(grades)
    
def load_file(filename):
     with open(filename, 'r', encoding='utf-8') as file:
            global grades
            grades = json.load(file)
            print("Данные успешно загруженны")
            return print(grades)
     
def del_stud():
    name_del = input("введите Имя которое хотите удалить:    ")
    del grades[name_del]
    print("удаление",name_del,"успешно")
    return print(grades)

def menu():
     while True:
        print("1 Создать нового")
        print("2 Загрузить")
        print("3 Добавить")
        print("4 Сохранить")
        print("5 Удалить")
        print("6 Выход")
        
        choice= input("Ввод:  ")
        if choice =="1":
            name_1= input("Введите имя нового студента: ")
            marks = list(input("введите его оценки:        "))
            add_student(name_1,marks)

        elif choice == "2":
            name = input("введите имя файаладля загрузки:  ")
            load_file(name)
            print(grades)
        elif choice == "3":
            add_marks()
        elif choice == "4":
            save =input("Введите имя для сохранения:    ")
            save_file(save)
        elif choice =="5":
            del_stud()
        elif choice == "6":
            print(grades)
            break

menu()