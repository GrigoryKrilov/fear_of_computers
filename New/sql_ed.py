import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('baza.db')
cursor = conn.cursor()
print("Подключенно")

def check_data():
    
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
        conn.close()
    print("Соединение закрыто")
    



# Пример добавления одной записи
def add_single_record():

    cursor.execute("""
        INSERT INTO users (name, age, email) 
        VALUES ('Иван', 25, 'ivan@example.com')
    """)
    conn.commit()
    print("Запись успешно добавлена")



add_single_record()
check_data()