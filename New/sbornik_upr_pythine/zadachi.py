"""решил немного попробовать в алгоритмы так как нашел прикольный видос.
 метод пузырьков 

from random import randint
N = 10
spisok = [10,8,6,4,2,9,7,1,3,5]

for i in range(N):
    spisok.append(randint(1,10))
print(spisok)

for i in range (N-1):
    for j in range (N-1-i):
        if spisok[j] > spisok[j+1]:  #    j + 1 это следующее число в итерации.
            spisok[j], spisok[j+1] = spisok[j+1], spisok[j]  #  10 больше  8  тогда смешаем вправ


    
print(spisok)
"""


#pupil = "Оби ван"
#old = 16 
#grade = 9.2

#print("It %s %d Leveel: %f" % (pupil, old, grade))
#print("It %s %d Leveel: %f" % (old, old, old))
#print("It %s %d Leveel: %f" % (grade, old, pupil))
#v s, d, f обозначают типы данных – строку, целое число, вещественное число. 
#Если бы требовалось подставить три строки, то во всех случаях использовалось бы сочетание 
#%s.

#print( "this is  a {1}. it is {0}" .format("ball", "red"))  # соотвесвенно ball {0} red {1}


#a = 10
#b = 1.33
#c = "Box"

#print(f"{a:5} - {c}")
#print(f"Цена - {b + 0.2:.1f}")

#name = input("Ваше имя" )
#city = input("Ваш город" )
#print(f" Вас зовут {name} Ваш город{city}")


# kolichestdo = input(" сколько нужно ?   ")
# price = input("цена одного ")

# kolichestdo = int(kolichestdo)
# price = float(price)

# summa = kolichestdo * price 

# print("заплатите", summa, "рублей")
# print(type(summa))  


# chislo_1 = input("введи чило 1:   ")
# chislo_2 = input("введи число 2:  ")
# chislo_3 = input("введи число 3:  ")
# chislo_4 = input("введи число 4:  ")
# summa_chisel_1_2 = float(chislo_1 + chislo_2)
# summa_chisel_3_4 = float(chislo_3+chislo_4)
# delenie = summa_chisel_1_2 / summa_chisel_3_4
# print("%.3f" % delenie)

# n1 = input("введи чилсо:    ")
# n2 = input("веди чилсо:     ")

# vivod = n1 > n2
# print(vivod)


# dannie = bool(input("введи число:"     ))

# if dannie == True:
#     print("ОК")

# else:
#     print("ты ничего не написал")

# # без bool типа даннных программа не работает как надо ввыводит тело else


# chixlslo = input("введи чилсо:     ")
# print(type(chixlslo))  string
# переобрзаовать str в int

# if int(chixlslo) > 0:
#     print (1)
# else:
#     print(2)

# try:
#     n1= int(input("введи только число"))
#     n2= int(input("введи только число"))
#     n3= n1+n2
#     print(n3)
# except:
#     n1= str(input())
#     n2= str(input())
#     n3= n1+n2
#     print(n3)
# finally:
#     print("конец программы")


#  a_str = input("Первое значение: ")
#  b_str = input("Второе значение: ")
#  try:
#     a_num = float(a_str)
#     b_num = float(b_str)
#     print("Результат:", a_num + b_num)
#  except ValueError:
#     print("Результат:", a_str + b_str

#можно создать переменную в начале и потом ее преобразовать в другой тип данных 

# ...
#  try:
#     a = int(a)
#     b = int(b)
#  except ValueError:
#     pass # ничего не делать
#  if type(a) == int and type(b) == str:
#     a = str(a)
#  print("Результат:", a + b)


# можно с помощю функции type() ставить условия на типы данных.


# # Условия matc case
#  Здесь значение переменной sign проверяется не на вхождение в какой-либо диапазон, а на 
# точное соответствие заданным строковым литералам

#  sign = input('Знак операции: ')
#  a = int(input('Число 1: '))
#  b = int(input('Число 2: '))
#  match sign:
#  case '+':
#  print(a + b)
#  case '-':
#  print(a - b)
#  case '/':
#  if b != 0:
#  print(round(a / b, 2))
#  case '*':
#  print(a * b)
#  case _:
#  print('Неверный знак операции')


#  sign = input('Знак операции: ')
#  match sign:
#  case '+' | '-' | '*':
#  a = int(input('Число 1: '))
#  b = int(input('Число 2: '))
#  print(eval(f'{a} {sign} {b}'))
#  case _:
#  print('Неверный знак операции')


# num=input("введи число: ")

# try:
#     num_int=int(num)
#     print("вы ввели")
#     print(num_int)

# except:
#     print("не число")
#     exit()

#     if num_int >= 1:
#         print("положительное чилсо")
#     elif num_int == 0:
#         print("ноль")
#     elif num_int<=0:
#         print("отрицательное число")

# finally:
#     print("конец")


        
# tot = 10
# chislo= int(input())
# tot_2 = tot-chislo
# if tot_2 <= -0:
#     print("всё")
#     exit()
# else:
#     print(tot_2)




# tot=10
# while tot > 0:
#     print("введи чилсо")
#     num=int(input())
#     tot=tot-num

#     if tot <0:
#         print(" все конец")
#         exit()


# tot=10
# while tot > 0:
#     print("введи чилсо")
#     num=int(input())
#     print("ваше число")
#     print(num)
#     tot=tot-num
 
# if num > tot:
#     print("конец")



# tot=10
# while tot > 0:
#     text = "у вас осталось {} единиц".format(tot)
#     print(text)
#     num=int(input())
#     print("ваше число")
#     print(num)
#     if num <= tot:
#         tot=tot-num
#         print("осталось")
#         print(tot)
    
#     else:  
#         print("у тебя 10 едеиниц, нельзя вычесть" , num, "из", tot)
#         print("осталось", tot)
#         break


# num=2
# grade=1
# while grade < 10 :
#     num=num*2
#     grade=grade+1
#     print("2 в степени",grade ,"будет равно", num)
# print("конец")









#задача 1 ввод от пользователя и сложение двух переменных.

#a = input('введи сколько банок пива у тебя есть')
#print (type(a))
#b = input('введи сколько принес друг')
#print (type(b))
#c = int(a) + int(b)
#print (type(c))

#print (c)

#print (type(c))


#Что мы сделали в этой задачи.

# В этой задаче мы при вводе команды получаем 5 типом данных "str",  если сложить 'str' и 'str' выйдет фигня типо 55 вместо 10.
#по этому когда мы складываем две переменные "а" и "б" то мы приводим к типу данных "int" то есть целое число. такоим образом
#все прекрасно сложиться вместе и даст результат 10 вместо 55 с типом "str".

#Чему я научился
# в этой хадаче я научился функции ввод от пользователся, перевод данных в другой тип,  сложение данных и вывод данных.

#3адача 2 среднее арефметическое (не получилось)
#что я туту понял это то что в переменную можно положить только одно значение, переменная запонминала только последнее значение.
#и делила его на число в другой переменной. гипотеза переменная i передает значение кол во раз итераций. если мы вводим цифру 2 получаем 1
# если цифру 1 то 0 итак далее. или она просто считает от 0 до того числа к которому итерируеться то есть мы даем 3 она считает 0 1 2
# получаеться 3 да так и есть скорее всего.

#a = int(input('введите число'))
#print(type(a))

#for i in range(a):
    #a1 = int(input('{} Число:' .format(i+1)))
#print(a1)
#print(a)
#a1 /= a
#print(a1)
#print(i)

#Задача 3
#вывести все елементы которые меньше 5
#[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#cifri = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 8]
#print(type(cifri))
#for element in cifri:
    #if element < 5:
        #print(element)
# я создал переменную "cifri" тип данных 'list' по сути это список в котором храняться данные по очереди их добавления.
# я узнал об этом принтанув тип данных переменную
# в списке может храниться и тип данный 'str' к примеру x = [abc, bcd, cda] в списке x 3 элемента с типом данных 'str'
# млжно узнать длинну списка применив функцию len()
# открыл цикл 'For' создал переменную " element" "in" это тоже часть цикла "For" после нее идет переменная по которой будет
# итерироваться циклом первая переменная.

#Задача 3 нужно вернуть список где  элементы обще для двух списков

#a = [3,1,2,3,5]

#b = [3,2,1,3,4,6,5]

#result = [el1 for el1 in a if el1 in b]
#print(result)

#result = list(filter(lambda elem: elem in b, a))
#print(result)

#эту задачу я не понял вообщем потом разобрать 

#задача с условиями.

#chislo = int(input('введи что нибудь '))
#if chislo < 3:
    #print('a0')
#if chislo < 1:
    #print('а1')
# в таком случае он выведет все два значение если сработает второе улсовие потому что оно будет равно и первому тоже.
    
# chislo = int(input('введи число'))
# if chislo <10:
#     print('это число меньше 10')
# if chislo >10:
#     print('это число больше 10')
# if chislo == 10:
#     print('число равно 10')

# number = int(input('введи число'))
# if number >10:
#     print('больше 10')
# else:
#     print('меньше 10')

# num = int(input('ВВЕДИ ЧИСЛО'))
# if num >0:
#     print('положительное число')
# elif num == 0:
#     print ('ЭТО НОЛЬ')
# else:
#     print('отрицательное число')

# вложенные конструкции, в нутри любого if elif else может быть сколько угодно if elif else

# num = float(input("Введите число: "))
# if num >= 0:
#     if num == 0:
#         print("Ноль")
#     else:
#         print("Положительное число")
# else:
#     print("Отрицательное число")


#  все else срабатывают под своими if.

# логика это задачи
# первый if число больше нуля  если отцательное срабатывает   false и идет к последнему else и выпляняеться print
# отрицательное число 
# # если в первом if срабатывает true то выполняеться его тело и ведет к второму if
# второй if условие если число равно нулю true ноль false  положительноу потому что
# уже существует условие что число не отрицательное.

# но это легче решить с помощью elif

# далее попробовать с большим количесвтом условий.


# Цикл For изучаю отдельно
# цикл for по сути это просто перебор определнных значений жо тех пор пока не будет достигнут последний элемент- 
# на этом цикл закончиться

#  numbers это переменная с типом данных list в котором храняться значения.
# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11, 12]
# можно задавать переменные с нулем и потом туда записывать разное значение.
# sum = 0
# Итерация цикла  for где value это переменная.
# Тут цикл for говорит что для value которая пока ноль в переменной numbers в которой цифры отдельно тип данных list 
#  мы перебираем и записываем значения
#  мы уже сказали что for будет перебирать в numbers цирфы а тело цикла говорит что мы бдуем не только перебирать но еще и складывать их.

# for value  in numbers:
#     sum = sum+value
# print(sum)

# Как бы возможно удобнее чистать цикл for  с конца типо цифры в значении перебираються и кладуться в сумму 
# или дадже так  цифры перебираються  становяться значением путем сложения  и записываються в сумму



# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11, 12]
# sum = 0
# for sum  in numbers:
#     print(sum)
# тут в sum положили все циры по порядку

# по пробовал сложить без переменной Value
# numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11, 12]
# sum = 0
# for sum  in numbers:
#     sum = sum+numbers    
# print(sum)

# тут он не даст сложить sum  где тип данных int с numbers гже тип данных list, по этому и нужна прослойка?
# что бы  привести к одному типу данных ? 

# sum = sum+value вот тут я понял что sum равно значение sum + value  т.е 0 + value а это ни что иное как перебор numbers  с помощью For
# и получаеться уровнение 0 + цифра1 + цифра2 и т.д

# так же For это как условие что ли как будет работать его тело ка кто так 

# для value 0  в numbers 123 
# sum будет  sum 0 + value 1 = 1  1+2=3  3+3=6  

# Следущая задача  + функцию range()  и играемся с ней
# Программа для итерации списка с использованием индексации

# genre = ['поп', 'рок', 'джаз']

# for i in range(len(genre)):
# 	print((genre[i]))
#  без len range не сработает просто а на оборот будет не тот тип данных. э то работает как  связка.
	# говрит что тип данных int по нему не может итерироваться. это будет если убрать range.

# функция len считает длинну переменной. 

# peremennai = ['pop', 'rock', 'jazz']
# print(len(peremennai))
# print(type(peremennai))

#  тут лен восприняла переменную  длинной 3 тип данных лист.

#  на будующее спросить почему сейчас не хочу думать об этом. видимо как то меняться тип данных.

# For может быть  использован с else, else выполняеться если цикл был не выполним. тут нет студента выводит false 
# значит выполняеться Else. 

# Программа выводит на экран оценку студента
# student_name = 'Артем'

# marks = {'Роман': 90, 'Максим': 55, 'Артур': 77}

# for student in marks:
#     if student == student_name:
#         print(marks[student])
#         break
# else:
#     print('Студент не найден.')





#  break нужен что бы программа дальше не игралась иначе выведет данные по переменной Артем и сыграет else
# #  и выведет 13 стедент не найден.

# student_name = 'Артем'

# marks = {'Роман': 90, 'Максим': 55, 'Артур': 77,  'Артем' : 13}

# for student in marks:
#     if student == student_name:
#         print(marks[student])
#         break
# else:
#     print('Студент не найден.')


#  функция format()
#   >>> x = 5; y = 10
# >>> print('Значение х = {}, а y = {}'.format(x,y))
# Значение x = 5, а y = 10

#  Функиция простой пример и как ее можно переименовать 

# def printHello():
#     print("Привет!")

# a = printHello

# a()

# алгоритм сортировка пузырьком.

# from random import randint
# N = 10
# spisok = [10,8,6,4,2,9,7,1,3,5]

# for i in range(N):
#     spisok.append(randint(1,10))
# print(spisok)

# for i in range (N-1):
#     for j in range (N-1-i):
#         if spisok[j] > spisok[j+1]:  #    j + 1 это следующее число в итерации.
#             spisok[j], spisok[j+1] = spisok[j+1], spisok[j]  #  10 больше  8  тогда смешаем вправ


    
# print(spisok)


# sorted() 
# функция которая принимает в себя оргумент в виде спискка строки кортежа множества и словаря и возвращает список.
#  в функции еть три аргумента 1 это обект 2 это key 3 reverse. есть встроенные фунции к примеру в key усть len() и можно сортануть 
# по длинне.
#  так же функция sorted() подерживает написание своих функций.


# Факториал числа
# n = int(input('введи чилсо:    '))
# f = 1

# for i in range(2,n+1):
#     f*=i
# print(f)

# range задаеться тремя аргументами  первый от какого числа будет идити, второй до которого он идет не включая его, третий с каким шагом.
# переменная f  будет равнться 1 что бы мы  потом смогли то что получим в цикле умножить на 1 и вывести это, если print(i) то получаеться что нам выведут по очереди числа от 2 до n+1


# числа фибоначи

# fib1 = fib2 = 1 
# n = int(input('Введи число:_____'))  #  я ввел 10 

# print(fib1, fib2, end=' ')

# for i in range(2,n): # range() генерирует от 2 до 10 и выводит 8 чисел.
#         fib1, fib2 = fib2, fib1 + fib2  # f а то что это за символы определены этой формулой
        
#         print(fib2, end=' ')  # print() должен быть в теле  цикла иначе будет выводить только конечную цифру.

# # мы определили переменные  как единицы потом они складываються и перезаписывают одну из них и продолжают N раз.
        
#  # f 1  будет f 2 а f2 будет сумма f1 b f2  так они замещаються и по
        


#расстояние левенштейна  (чувствителен к ригистру)

# slovo_1 = 'парик'
# slovo_2 = 'карлик'

# n = len(slovo_1) 
# m = len(slovo_2)
# #  длина слова
# if n>m:
#     slovo_1,slovo_2 = slovo_2,slovo_1
#     n,m = m,n
# # это переворачивает слова  метсами если одно из них длинее хуйхнает зачем.
    
# # print(n)
# # print(m)

# # print(slovo_1)
# # print(slovo_2)
# # принтую для проверки


# tekuciaia_stroka =  range(n+1) # текщая строка  это число длины слова n + 1
# print('ткушая строка ',tekuciaia_stroka)
# for i in range(1, n+1):   # функция range()  запишет в i диапазон от 1 до длины слова n  + 1
#     print('i ',i)
#     predidishaia_stroka, tekuciaia_stroka = tekuciaia_stroka,[i] + [0] * n
#     print('пердыдушая строка ',predidishaia_stroka)
#     print('ткушая строка',tekuciaia_stroka)
# # итерируеться в i колисество раз равное длине слова. и записывает это в списосок.
#     for j in range(1, n+1):
#         print('j',j)
#         add,delete, change = predidishaia_stroka[j] + 1, tekuciaia_stroka[j-1] + 1, predidishaia_stroka [j-1]
#         print('add',add)
#         print("delete",delete)
#         print("change",change)
#         if slovo_1[j-1] != slovo_2 [i-1]:
#             change+=1
#         tekuciaia_stroka[j] = min(add,delete,change)
#         print(tekuciaia_stroka[j])


# print('вывод',tekuciaia_stroka[n])

# min() возвращает минимальное  число из группы чисел 
# что я пока что понял это, мы находим длину слова, сравниваем две длины слова, делаем матрицу и берем минимальное значение.
# при заполнении матрицы нужно ссылаться на формулу, и конечнй символ на пересечении N и M и будет расстоянием Левенштейна.
# минус еденица потому что в пайтоне индексация идет с нуля.
# квадратные скобки начит двигаем индекс а не значение числа
# все остальное это формула ливенштейна.
# первый фор создает  счписок второй фор заполняет.
# ну и мин функция выводит конечное значение 




#class - позволяет обеденить в себе несколько функций и упорядочить их, что бы было легче использовать в дальнейшем.
# К примеру для отвертки и гаечного ключа, кейс не нужен т.к. два истумента незачем хранить в коробке.
#  а если есть шуруповерт 3 ключа 4 ответки 10 насадок  то нужен некий комплект который будет это хранить.
#  это и есть class
#  в нутри класса храняться его атрибуты и методы

# Node - узел
#  self - сылка на текущий экземпляр класса
# все методы которые записываються таким образом , относиться к работе  с class __delattr__
#  dir () возвращает список переменных. как раз тут она и  перечесляет все атрибуты класса  в данном сулчае выводит в список с атрибутами в алфавитном.
#  порядке без него выведеться  __main__ 
#  __init__ - создает новые обекты класса  и иннициализирует его атрибуты, позваляет задавать начальные  значение переменных  

# class DemoClass:
#     def sample_method():
#         print ("This is the demo method")
# the_object=DemoClass
# print(dir(the_object))

#class Person:

    #def __init__(self):
       # tom = Person () # создвние обекта Person()
#  для вызова конструктора __init__ в аргумент подаеться класс к примеру текщий то есть __init__(self)
    

# print(Person)
        
# атрибуты хранят состояние обекта  для их установки  используеться слово self.






#Samash_faktor

# speed_bool= 23232
# speed_club= 12321

# smash_factor= speed_bool / speed_club
# print(float("%.99999f" % smash_factor))


# Bridgу

# bridge="+ ++++ "
# x= bridge.find(" ")
# print(x+1)


# bridge_broken = "++ ++++ + "
# for bridge in bridge_broken:
#     search=bridge.find(" ")
    
# if search != -1:
#         new_bridge = bridge_broken.replace(" ","+" )
#         print(new_bridge)


# bb = "+ + + + +"
# nb=bb.replace(" ","+")
# print(nb)


# years = float(input("введи год:        "))

# if years%400 == 0:
#     print(years)
#     print("год високостный")

# elif years %100 == 0 :
#     print(years)
#     print("не високостный")
# elif years %4  == 0:
#     print("не високотсный")
# else:
#     print("не я вляеться виск годом")


# y=int(input("Введите год: "))
 
# # проверка года
# if y%400==0 or y%4==0 and y%100!=0:
#     print("Год високосный")
# else:
#     print("Год не високосный")


# try:
#     num_1 = int(input("введи номер 1: "))
#     num_2 = int(input("введи номер 2: "))

#     if num_1 == num_2:
#         print("равны")

#     elif num_1 >= num_2:
#         print("большее число num_1 ",num_1)

#     elif num_2>= num_1:
#         print("большее число num_2 " ,num_2)

# except:
#     print(" не число ")
#     exit



# a=int(input())
# b=int(input())
# g = a if a>b else b
# print(g)

# try:

#     num = int((input("сколько денег:    ")))
#     if 0 < num <= 5000:
#         num_2 = num*(1-0.05)
#         print("ваша цена с учетом скидки",num_2)
#     elif 5001 < num <= 15000:
#         num_2 =num*(1-0.10)
#         print("ваша цена с учетом скидки",num_2)
#     elif 15001 < num <= 25000:
#         num_2 = num*(1-0.15)
#         print("ваша цена с учетом скидки",num_2)
#     elif num > 25001:
#         num_2 = num*(1-0.25)
#         print("ваша цена с учетом скидки",num_2)
#     else:
#         print("это как так ?")
    

# except:
#     print("числа ,а не буквы")




# while с иснстрцкцие true будет исполняться бесконечно пока его не прервут.
# либо создать булевую переменную за пределами цикла в начале
# а = true 


# num_1=int(input("введи число_1   "))
# num_2=int(input("введи число_2   "))

# while True:
#     print(num_1+num_2)
#     str=input("вы хотите заверщить программу: ")
#     if (str == "y"):
#         print("программа завершена") 
#         break

# while True:
#     num_1=int(input("введи число_1   "))
#     num_2=int(input("введи число_2   "))
#     print(num_1+num_2)
#     str=input("вы хотите заверщить программу: ")
#     if (str == "y"):
#         print("программа завершена") 
#         break
#     elif (str == "n"):
#         print("программа не завершена") 
        

#  в данном случае если while находиться в сам верху цикл продолжиться с запроса вход, если в верху будет (как в предыдушем варианте) находиться доугая команда
#  то цикл за стрянет в посленецй исполняемой команде.

# через булевую переменную a


# a = True
# while a:
#     num_1=int(input("введи число_1   "))
#     num_2=int(input("введи число_2   "))
#     print(num_1+num_2)
#     str=input("вы хотите заверщить программу: ")
#     if (str == "y"):
#         print("программа завершена")
#         a = False 

#     elif (str == "n"):
#         print("программа не завершена")     


# /n новая строка, делает пробелы.
# 
# end = " "  выводит доп символ на этойже строке и в одну гаризонт. строку.

#  два цыкла  for на каждый i он делает 10 j b затем снова i.

# star = "*"
# balls = "0"
# for i in range (0,11,):
#     print(star,end="")
#     for j in range (0,11):
#         print(balls, end="")

    
    
# h = 10
# for i in range (1, h+1):
#     spaces = "" * (h+2)
#     stars = "+" * (2*i-1)
#     print(spaces+stars)
    

#     for j in range (1, h-1):
#         spaces = "" * (h-2)
#         stars = "+" * (2 * j+1)
#         print(spaces+stars)


# Елеочка с обеснением длинная версия

# h = 5
# # первый фор всегда + 1 в переменную i  с начала нового цыкла.
# for i in range(1,h+1):
#     # print(i) делает уровни в зависимости от высоты. у на сполучаеться 5 итераций
#     for j in range(h-i):
#         #  он делает 4  прбела в первой итерации, в пкрвый раз i  будет равен 1  h равен 5.  5-1 = 4 пробела. 
#         # print(j)
#         print("_",end="")
#         # print(j,end="") делает пробелы  в начале

#     for j in range(2*i-1):
#         #  2 умножить на 1 и минус 1 будет 1 звездочка
#         # print(j, end="") наполняет прирамидку.
#         print("*", end="")
#         #  последниий принт делает отступы в конце.
#     print("-")
# #  один цикл это одна горизонтальная прямая , потому что всегда срабатывает последний принт, кол во циклов это высота.


# Елочка короткая версия код


# h = 5

# for i in range(1,h+1):
    
#     for j in range(h-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("+", end="")
        
#     print(" ")


# for i in range(1,7):
#     print("=",end="")

#     for j in range(1,10):
#         print("*",end="")
#         for j in range(1,5):
#             print(j,end="")
    
#     print("_")


# n=5 # высота
# k=1 # 
# counter=1 #   k и caunter это две переменные которые задают цифры и звездочки
# # и в цикле плюсут то в один то в другой.
# for i in range(n):
#     # print(i) колво итераций, и высота.
#     for j in range(n):
#         # print(j) # часть цифр 
#         if k % 2 == 0:  # % возвращает остаток от деления от двух чисел,будет последовательность из 0 1 0. разделение на четные и не четные цифры.
#             # print(k, end=" ")
#             print(counter, end ="  ")
#             #  counter отвечает за значение цифр
#             counter+=1 # если в cauner не будет добавлена единица то он всегда будет возвращать 1 во всем кубе
#         else: print("*",end="  ")
#         k+=1 # если не будет прибавлен к K единица, то будут одни звезды везде.     
#     print()

# n = 6
# k = 1
# c = 1
# for q in range(n):
#     for i in range (n):
#         if k % 2 == 0:
#             print(k,end=" ")
            
#         else:
#             print(" ",end=" ")
        
#         c+=1    
#         k+=1
#         print("*",end=" ")    
#     print()

#сммысл в 3 счетчиках которые идут в разнобой к1 к2 и с , нужно просто правильно щаменить цыфры в матрице что бы получилась правильная последовательность цифр и символов.
    


# for i in range(21):
#     k = i % 2 # это условие создает порядок цыфр не только из 0 и 1 но и больше и только целые цифры.
#     print(k,end=" ")


    

# n = 10
# for i in range (0,n):
    
#     for j in range(0,n):
#         if i ==0 or i ==n-1:
#             print(i,end="")
#         elif j==i or j== n-i-1:
#             print(j,end="")
#         else: print(" ", end="")
#     print(" ")

# h = 7 
# w = h+2
# m=w//4 # цело численное деление будет 2

# for i in range(1,h+1):
#     # print(i)
#     if i <=m:
#         print(" " * (m-i) + "*" * (2*i) + " " * (w-2*i-2*m) + "*" *(2*i) + " " * (m-i))
#     else:
#         print(" " * (i - 2*m+1) + "*" * (w-2*(i-2*m+1)) + " " * (i - 2*m+1))




# -------------------------------------------------------------
# m= 2
# for i in range (7):
#     print("*"*(m-i))
# когда из меньшего вычетаешь большее то значение уходит в минус  
#когда умножаем на символ к примеру "*" то количество символом отображает значение цифры, но вместо. 0 и отрицательных цифр будет  стоять пропуск " "  


# h = 10
# w = 4
# for i in range(h):
#     print(i)

#     for q in range (w):
#         print(q *"*",end=" ")
        

# упражнение из др уч. упр 35

# try:
#     num = int(input("введи число:     "))
#     # print(num)
#     if num % 2 == 0:
#         print(num)
#         print("четное число")
#     else:
#         print(num)
#         print("не ччетное")

# except:
#     print("число")

# упр 36 


# dog = 10.5, 10.5, 4,4,4
# man = 1

# man_vozrast = 21 (- 2) * 4



# man = int(input("введи те возраст человека   "     ))
# man_2 = man*4 + 19
# print(man_2)

# try:
#     man = int(input("введи те возраст человека   "     ))
#     if man <0:
#         print("отрицательное число")
#     elif man <=2:
#         man_2 = man + 19
#         print(man_2)
#     elif man > 2:
#         man_2= ((man-2)*4)+21
#         print(man_2)
# except:
#     print("цифры")


# text = input("введите букву:   ")
# vowels = "aeiou"

# for i in text:
#     if   i in  text == "y":
#         print("может быть там и там")
            
#     elif i in vowels:
#         print("гласные")
#     else:
#         print("согласные")
# print("конец программы")




# text = "yyy"
# for i in range(len(text)):
#     # print(i+1)
#     if i >= 2: 
#         print("может быть и там и там")
    
# использовать рендж лен 
# не льяз сравнивать количество букв с цифрами это разные типы данных  стр и инт.





# sides = int(input("введи количество сторон:     "))
# if sides ==0: print("круг")
# elif sides ==3: print("трегольник")
# elif sides == 4: print("квадрат")
# elif sides == 5: print("пентагон")
# elif sides == 6: print("гексагон")
# elif sides == 7: print("правильный семиугольник")
# elif sides == 8: print("октагон")
# else: print("больше нету")
# print("end")


# mouns = input("количество месяцев:   ")
# if mouns == "may": print("30")
# elif mouns == "aprl": print("29")
# print("конец программы")



# text ="c4"
# print("вы велли:",text)

# c4 = 261,63
# d4 = 293,66
# e4 = 329,63
# f4 = 349,23
# g4 = 392,00
# a4 = 440,00
# b4 = 493,88


# if text == "c4":
#     print(c4)
# if text == "d4":
#     print(d4)




# c4 = 261.63
# d4 = 293.66
# e4 = 329.63
# f4 = 349.23
# g4 = 392.00
# a4 = 440.00
# b4 = 493.88

# name =input("введите название ноты: ")
# print(type(name))

# note = name[0]
# octava = int(name[1])


# my_list = ["a",2, True, 5.56]
# # print(my_list[0:2]) # чрез в списке
# print(len(my_list))


# сложить два значение в списке можно так? да
#так же внутри списка можно скалдывать между собой значения так же как и вне его, по тем же правилам.
# my_list=[1,2,3+3]
# print(my_list[2])

# my_list=[1,2,"a"+ "b"]
# print(my_list[2])

# если принимаешь с4 то это два разных значения или одно   в списке

# text = "с4"
# note =text[0]
# octava = int(text[1])

# text = "с4"
# print(text[0])


# name = input("введите ноту: ")
# note = name[0]
# oct= int(name[1])

# c4 = 261.63
# d4 = 293.66
# e4 = 329.63
# f4 = 349.23
# g4 = 392.00
# a4 = 440.00
# b4 = 493.88

# if note == "c":
#     freg = c4
# elif note == "d":
#     freg = d4
# elif note == "e":
#     freg = e4
# elif note == "f":
#     freg = f4
# elif note == "g":
#     freg = g4
# elif note == "a":
#     freg = a4
# elif note == "b":
#     freg = b4

# freg = freg / 2**(4-oct)

# print("частота ноты",name,"равна",freg)




# seasons = []
# summer= []
# winter = []
# antmunt= []
# spring=[]
# seasons.append(summer)
# seasons.append(winter)
# seasons.append(antmunt)
# seasons.append(spring)

# for num in range(1,31):
#     summer.append(num)
#     winter.append(num)
#     antmunt.append(num)
#     spring.append(num)



# print(type(seasons))


# text = float(input("vvedi cifru: "))

# if text >= 10.0:
#     print("разрушительно")
# elif text >=8.0:
#     print("опасно")
# elif text >=3.0:
#     print("умеренно")
# elif text >=1.0:
#     print("едва ощутимо")
# else:
#     print("ничего")

# логика работает от большего к меньшему

# забавно что  нужно ставить знак больше или меньше но не равно.
# потому что если поставить равно то цикл будет ожидать сразу выполнение.
# тогка как если поставить знак меньше то он будет ожилать постепенное увеличение.
    

# i = 0
# list_1 = []


# while i < 10  :
#     num = int(input("ведите ряд цифр:    "))
#     list_1.append(num)

#     i = i + 1
# print(list_1)
# list_1 = sum(list_1) / i
# print(list_1)






#  Упражнение 70. Биты четности.

# i = 0
# list_1 =[]
# while i < 8:
#     num = input("введите чимла из 0 и 1:   ")
#     if num != "0":
#         if num !="1":
#             print("только  0 или 1")
#             break
#     list_1.append(num)
#     i += 1
#     print(i)
# count_1 = list_1.count("1")
# print(count_1)
# if count_1 % 2 == 0:
#     print("четное число")
# else:
#     print("не четное")
# медод каунт считввает количество входжений в него и выдет число.
# как функция задает в скобках то что ищет и возвращает количество искомого обекта в переменной.

# import random
# max_value= []
# number_list = []

# i=0

# while i < 100:
#     random_numbers = random.randint(1,100)
#     number_list.append(random_numbers)
#     i += 1
# max_value = (max(number_list))
# for num in number_list:
#     if num == max_value:

# print(number_list)
# print(max_value)

# суть задачи что бы код генерил число  и добавил его в список макс значение.
# после этого генерил другое число и сравнивал его с списком макс значение.
# если оно больше первого числа он его добовляет если нет то генерит следующее
# и так 100 раз.

