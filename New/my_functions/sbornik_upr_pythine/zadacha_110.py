list = []
datchik = True

while datchik:
        
    text_usr = int(input("ввидете число, 0 чтобы выйти: "))
    list.append(text_usr)
    if text_usr == 0:
        datchik = False
print(list)
list.sort(reverse=False)
print(list[1:])
