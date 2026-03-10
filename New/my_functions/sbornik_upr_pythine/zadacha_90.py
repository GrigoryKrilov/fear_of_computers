my_dict = {"0":"в первый","1": "На (sn+1) день рождества моя любовь подарила мне ","2":" Куропатку на грушевом дереве","3":"Двух горлиц","4":"Трехфаверолей" }
# print(my_dict.values())

def stix (nmbr_k):

    if nmbr_k == 1:
        print(my_dict.get("0"))
        print(my_dict.get("1"))
        print(my_dict.get("2"))
    elif nmbr_k == 2:
            print(my_dict.get("1"))
            print(my_dict.get("2"))
            print(my_dict.get("3"))
    elif nmbr_k == 3:
            print(my_dict.get("1"))
            print(my_dict.get("2"))
            print(my_dict.get("3"))
            print(my_dict.get("4"))
    else:
            print("пока только 3 куплета готовы")

    return "конец работы"

print(stix(3)) 