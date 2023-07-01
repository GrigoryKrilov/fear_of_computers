input_1 = '123a.456b'
input_2 = '098c.765x'
numbers = [0,1,2,3,4,5,6,7,8,9,'.']
for i in range(len(numbers)):
    numbers[i] = str(numbers[i])
is_input_1_correct = True
input_1_float = '0'
input_1_str = '0'
for i in range(len(input_1)):
    print()
    print('proverka na pidora')
    print()
    print('{} of {}'.format(i, len(input_1)))
    print('chislo:', input_1[i])
    current = input_1[i]
    print()
    if current not in numbers:
        is_input_1_correct = False
        print()
        print('pidr')
        print()
    if current in numbers:
        input_1_float = input_1_float + str(input_1[i])

numbers = [0,1,2,3,4,5,6,7,8,9,'.']
for i in range(len(numbers)):
    numbers[i] = str(numbers[i])
is_input_2_correct = True
input_2_float = '0'
input_2_str = '0'
for i in range(len(input_2)):
    print()
    print('proverka na pidora')
    print()
    print('{} of {}'.format(i, len(input_2)))
    print('chislo:', input_2[i])
    current = input_2[i]
    print()
    if current not in numbers:
        is_input_2_correct = False
        print()
        print('pidr')
        print()
    if current in numbers:
        input_2_float = input_2_float + str(input_2[i])
if current in numbers:
        input_2_float = input_2_float + str(input_2[i])
input_1_float = float(input_1_float[1:])
input_2_float = float(input_2_float[1:])
input_1_str = input_1_str[1:]
input_2_str = input_2_str[1:]
print()
print('input_1_float',(input_1_float))
print('input_2_float',(input_2_float))
print('float sum', (input_1_float + input_2_float))
print()
print('program finish')

