import string
import collections

def read_text_from_file(path):
    with open(path, 'r') as text:
        text = text.read()
    return text

def text_to_words(text):
    words = text.translate(str.maketrans('', '',string.punctuation ),).split()
    return words

def words_count_by_dict(words):
    words_dict = {}
    for word in words:
        word_caps = word.upper()
        if word_caps not in words_dict.keys():
            words_dict[word_caps] = 0
        words_dict[word_caps] += 1
    return words_dict

def select_value_from_pair(pair):
    return pair[1]

def sort_dict(dict_to_sort, is_reversed=True):
    sorted_dict = dict(sorted(dict_to_sort.items(), key = select_value_from_pair, reverse = is_reversed))
    # sorted_dict = dict(sorted(dict_to_sort.items(), key=lambda x: x[1], reverse = is_reversed))
    return sorted_dict

file_path = '/Users/ilpech/luckydog/dz_3_dict.txt'

text = read_text_from_file(file_path)
words = text_to_words(text)
words_dict = words_count_by_dict(words) 

#print(words_dict.values())

values = words_dict.values()

print(min(values))
for k , v in words_dict.items():
    if v == min(values):
        print(k)
exit()

sorted_dict = sort_dict(words_dict)
print(sorted_dict)


print()
print('samoe 4astoe slovo - "', max(sorted_dict, key=sorted_dict.get), '", kol-vo povtorenii -', sorted_dict['{}'.format(max(sorted_dict, key=sorted_dict.get))])
print()
# word_check = input('kogo proverit? ')
word_check = 'the'
word_check = word_check.upper()
if word_check in words_dict:
    print('vstre4alos', words_dict.get(word_check), 'raz')
else:
    print('ne bylo')
# for word in words_dict:
#     current = words_dict[word]
#     print(current)
#     if 'current' in words_dict:
#         print('vstre4alos', words_dict['current'], 'raz')
#         break
#     else:
#         print('ne bylo')