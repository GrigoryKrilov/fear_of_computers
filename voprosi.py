1.Какие три основных типа данных используются в компьютере для представления величин реального мира? Привести один-два предмета или его свойства, представленного с помощью каждого из типа данных.
целое число numbers (int)
дробное число  float
слово  string
bool true false

2. Что делает функция type()?
выводит тип данных функция

3. Что делает функция len()?
функция с помощью ее мы можем узнать длину слова

#4. Какое ключевое слово и какой символ используется для вставки переменной в указанное место строки?
 format( {} {} ) последовательно переменные 

5. Одинаковые ли строки '2023-03-11' и '2023-03-11 '?
нет там есть пробел он тоже считается

6. Ко всем ли типам данных можно обращаться с помощью индекса (операции []) и функции len()? обращаемся по индексу
Да 
 к строке и листу и словарю

7. С помощью какого ключевого слова проверяется условие? Как проверить, что переменная строго равна определенному значению?
if else  == 

8. Где применяются и как работают ключевые слова and и or?
в цикле после if  true false  and должны быть выполнены два условия or  или одно или дргугое


9. С помощью какой функции можно быстро сделать интервал чисел от 0 до 100?
range(100)

10. С помощью какой функции можно дать пользователю ввести значение переменной с клавиатуры во время запуска программы?
input()

11. С помощью какой функции можно моментально выйти из программы?
exit()

12. С помощью какого ключевого слова можно по очереди получить каждый элемент списка или каждый символ строки?
for переменная  in list

13. С помощью какого ключевого слова мы создаем функцию? Зачем у функции скобки?
def название функции на англ яз (переменная)  скобки нужны чтобы вызвать функцию
 
14. Зачем используется двоеточие и в каких случаях оно ставится в Python?
дает интервал к примеру от 1 до 10 1:10
после цикла что бы его запустить и начать с кр строки
в функциях 

15. Зачем в Python используется табуляция (начало строки не с красной, а с одним или несколькими отступами)?
мы ставим таб что следущие значение были в цикле

16. Как работают ключевые слова break и continue? В любом ли участке кода можно использовать эти слова?
да  в любом но только в цилке break прерывает  цикл но не выходит из программы continue пропускает итерацию в цикле

17. Как работает и где используется ключевое слово return? 
в функции def  возвразает переменную  то есть выходит из функции и передает данные


#8. Как вывести несколько переменных с помощью функции print(), не используя форматирование через ''.format?



 19. Как проверить наличие симлова в строке или списке?
isalpha()  выведет  False ecли будет символ 

 20. Как проверить, что символы в тексте являются числами?
isnumeric() 

 21. С какого значения считается первый индекс элемента в строке? Возможна ли отрицательная индексация text[-3] и что она обозначает?
с 0  да  отсчет пойдет с конца

22. Методы keys(), values() позволяющий получить значения словаря. , items() позволяющий получить пары "ключ-значение" словаря словаря

 23. Как добавить новый ключ в словарь?
 указать имя словаря, а затем в квадратных скобках [ ] указать новый ключ и значение.
  Словарь с параметрами мужчины
man = {"age": "30", "sex": "Мужской", "weight": "90"} 
 Добавляем в словарь новую пару
man["height"] = "200"
Выводим обновлённый словарь
print(man)
 Финальный результат в консоли
{'age': '30', 'sex': 'Мужской', 'weight': '90', 'height': '200'}
 
 24. Как проверить наличия ключа в словаре?
 key in dict
key in dict.keys()
ждем значение fool true

# 25. Как найти самое часто встречающееся слово в тексте?
# 26. Что вернется в переменную, если обратиться к несуществующему в словаре ключу?