
def text_upper(text):

    result = text[0].upper() + text[1:]

    for i in range(len(text)-1):
        
        if result[i] == ".":
            len_for_dot = len(result[:i+1])
            next_char = result[i+1]
            next_char_up = result[i+1].upper() + result[i+2:]
            final = result[:len_for_dot]+ next_char_up

            return final
        

print(text_upper("я ни кто иной.как бэтмен "))