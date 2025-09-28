def len_data (d,m):

    m = m
    dlina_m = m * 30
    print("колво дней до текущего месяца",dlina_m)
    d = d
    dlina_d = d
    print("уоличество дней в текущем месяце", d) 
    dlina_all = dlina_m+dlina_d
      
    return "количество дней всего",dlina_all


print(len_data(0,0))
    