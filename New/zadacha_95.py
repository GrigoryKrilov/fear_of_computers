# def up_letter (text):
#     result = text[0].upper() + text[1:]
#     return result


# print(up_letter("привет"))




text = "привет.пока"
result = text[0].upper() + text[1:]
for i in range(len(text)-1):
    if result[i] == ".":
        next_char = result[i+1]
        next_char_up = result[i+1].upper() + result[i+2:]
        len_nextcharup = len(next_char)
        
        final = result+ next_char_up
        print(final)
        
