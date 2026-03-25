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
    results = cursor.fetchone()
    print(results)
    cursor.close()
    conn.close()

# search_user_data_number("1_baza.db","3")