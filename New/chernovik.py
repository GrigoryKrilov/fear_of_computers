class Treebonsay: # создаем класс, называем его Treebonsay с заглавной буквы без нижнего прочерка.
    def __init__(self,name,height): # инит значит определить / создать экземпляр с параметрами  name и heitht имя и рост соотвесвенно.
        self.name=name
        self.height=height
        print("дерево создано","название",name,"Рост",height)
# грубо говоря это тело  "функции"


# создаем новые эксемляры с названием и парамнтром роста и сохранеям в переменную.
new_tree= Treebonsay("elm",10)
new_tree_1= Treebonsay("maple",5)  
# тут мы как бы вызваем эту  "функцию"


# class bugs:
#     def __init__(self,name,hazard):
        




# juniper = tree_bonsay()
# maple = tree_bonsay()

# aphid = bugs()
# scale = bugs()
# mite = bugs()

