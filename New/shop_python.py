import sqlite3

name = "Фреег"#input("Введите Имя:      ")
age = 33 #input("Введите Возраст:   ")
email = "grff@яндексюру" # input("Введите почту:    ")
product = "нож"#nput("Введите товар: ")

print(name,age,email,product)


conn = sqlite3.connect("1_baza.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS orders (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER,
email TEXT NOT NULL UNIQUE,
product TEXT
)
''')

cursor.execute(
    "INSERT INTO orders (name, age,email,product) VALUES(?, ?, ?, ?)", 
    (name, age,email,product)
) 
# execute() -подготовить выполнить insert-вставить.
conn.commit() # сохр изменрения

cursor.execute("SELECT * FROM orders")
rows = cursor.fetchall()  # fetchall - выборка метод извлечения строк и возврат кортежа.


print("Содержимое таблицы:")
for row in rows: # row - ряд row in rows ряд за рядом.
    print(row)


cursor.close() # закарыть курсор
conn.close() # закрыть соеденение
#  это важно что бы ресурсы не тратились.



# помоему это то что нужно  пускай тут лежит

import sqlite3

def prosmotr_baza(name_baza):
    
    conn=sqlite3.connect(str(name_baza))
    cursor = conn.cursor()
    cursor.execute("SELECT*FROM orders")
    rows = cursor.fetchall()
    print("содержимое талицы")
    for row in rows:
        print(row)
    cursor.close()
    conn.close()

# prosmotr_baza("1_baza.db")

def add_new_ueser(name_baza,data_user):
    print("Создание нового пользователя.")
    new_data_user=data_user.split()
    name,age,email,product = new_data_user[0],new_data_user[1],new_data_user[2],new_data_user[3]
    print(name,age,email,product)
    conn=sqlite3.connect(str(name_baza))
    cursor=conn.cursor()
    cursor.execute("INSERT INTO orders(name,age,email,product) VALUES(?,?,?,?)",(name,age,email,product,))
    conn.commit()
    cursor.close()
    conn.close()
    prosmotr_baza(name_baza)

# add_new_ueser("1_baza.db","фенрир 41 титан щит")

def search_user_data_number(name_baza,number_user):
    print("редактирование данных в базе",name_baza,"пользователя номер",number_user)
    conn=sqlite3.connect(name_baza)
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM orders where id = ?",(number_user))
    results= cursor.fetchone()
    # results=str(results)
    print(results)
    cursor.close()
    conn.close()

# search_user_data_number("1_baza.db","3")

def change_user_data(name_baza,number_user):
    conn=sqlite3.connect(name_baza)
    cursor=conn.cursor()
    cursor.execute("SELECT name,age,email,product FROM orders where id = ?",(number_user))
    results= cursor.fetchone()
    print(results)
    q = input("изменить данные пользователя:")
    if q == "1":
        print("старые данные:",results)
        new_data= input("новые данные:")
        split_new_data = new_data.split()
        print(split_new_data)
        name,age,email,product = split_new_data[0],split_new_data[1],split_new_data[2],split_new_data[3]
        cursor.execute("UPDATE orders SET name=?,age=?,email=?,product=? WHERE id = ?", (name,age,email,product,number_user,))
        conn.commit()
        cursor.close()
        conn.close()
        prosmotr_baza(name_baza)
    else:
        print("ничего не именили.")
    
change_user_data("1_baza.db","2")