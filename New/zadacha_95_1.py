text = "привет.пока"

result = text[0].upper() + text[1:]


for i in range(len(text)-1):
    

    if result[i] == ".":

        next_char = result[i+1]
        next_char_up = result[i+1].upper() + result[i+2:]
        final = result[:7]+ next_char_up
        print(final)
        