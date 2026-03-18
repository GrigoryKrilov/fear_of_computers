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


