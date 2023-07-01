calls_number = 148
current_week_day = 'monday\ttuesday'
average_calls = 243 
calls_percent = calls_number / average_calls
print(type(calls_number))
print(type(calls_percent))
print(type(current_week_day))
print(current_week_day)
# exit()
print('day progress:{:.2f}'.format(calls_percent))
# ebanaiya_sms = input('vvedui:') # нас пытаются наебать гуки
# ebanaiya_sms = 'sasi1suka0sasi'
# ebanaiya_sms = ''
# ebanaiya_sms = 'si'
ebanaiya_sms = 'acab2.9acab21312.123'
corrected_sms_left = ''
corrected_sms_right = ''
is_dot_found = False

# for symbol in ebanaiya_sms:# другой способ итерации
for i in range(len(ebanaiya_sms)):
    symbol = ebanaiya_sms[i]
    print(i, symbol)

    if symbol == '.': 
        is_dot_found = True
    if symbol in '0123456789':
        if not is_dot_found:
            corrected_sms_left += symbol 
        else: 
            corrected_sms_right += symbol
        print('passed')
corrected_sms = '{}.{}'.format(corrected_sms_left, corrected_sms_right)

calls_from_sms = str(corrected_sms)
print(ebanaiya_sms, corrected_sms)
full_calls_number = calls_number + calls_from_sms
print('calls number:', full_calls_number)  
