# 1. написать функцию, принимающую строку и проверяющая, палиндром ли это (читается ли справа-налево и слева-направо одинаково)def   
# def palindrome(word):
#     p_word = word[::-1]
#     if word == p_word:
#         print('Da')
#     else:
#         print('no')    

# palindrome('ngnf')
# palindrome('abba')
# palindrome('dfgd')
# palindrome('1221')

# #2. написать функцию, разбивающую строку на слова и выводящую в списке число букв в каждом слове типа "жаль, что ты лох" - [4, 3, 2, 3] знаки препинания и пробелы не считаем
# def dlina_slov(stroka):
#  words = stroka.split('')


# outhood = []

# dlina_slov('жаль что ты ,лох')


# text = 'жаль ,что ты лох?'
# text2 = text[:-1].replace(',','').split()
# print(text2)




# text = 'жаль ,что ты лох?'
# text = text.replace(',','')   
# text = text.replace('?','')
# text = text.split()

# print(text)



# text = "жаль. что! -ты лох?"
# import re
# text1 = re.sub('[.,?!-_' ']', "", text)
# print(text1)
# text2 = text1.split()
# print(text2)

# text = "жаль. что! -ты лох?"
# import re
# text1 = re.sub('[.,?!-_' ']', "", text)
# print(text1)
# text2 = text1.split()
# print(text2)
# for word in text2:
#     print(f"'{word}':{len(word)}")

def chislo_bukv(text):
    import re
    text1 = re.sub('[.,?!-_' '0-9]', "", text)
    #print(text1)
    text2 = text1.split()
    #print(text2)
    for word in text2:
        # print(f"{'в слове:'} '{word}' {len(word)} {'буквы'}")
        print(f'в слове: {word} {len(word)} буквы')
    
chislo_bukv('жаль. ч76то! -ты лох?')
chislo_bukv('пидор, т23ы! или. -твой _рот?[]]')