import _sqlite3

# name = input("Введите Имя:      ")
# age = input("Введите Возраст:   ")
# mail = input("Введите почту:    ")
# product = input("Введите товар: ")

# print(name,age,mail,product)


conn = _sqlite3.connect("shop_data_baz.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER
)
''')

cursor.execute("INSERT INTO users(name, age) VALUES('oleg',25)") # execute() -подготовить выполнить insert-вставить.
conn.commit() # сохр изменрения

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()  # fetchall - выборка метод извлечения строк и возврат кортежа.


print("Содержимое таблицы:")
for row in rows: # row - ряд row in rows ряд за рядом.
    print(row)


cursor.close # закарыть курсор
conn.close # закрыть соеденение
#  это важно что бы ресурсы не тратились.


