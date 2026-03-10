def centr (a):
    w = 80
    text = a 
    len_text = len(text)
    dif_w_len =  w - len_text
    # print(dif_w_len)
    print(dif_w_len*" ",text)


print(centr("что то "))