input_1 = '1b.2'
input_2 = '2a.3'
print(input_1)
print(input_2)
print(len(input_1))
print(len(input_2))
numbers = [0,1,2,3,4,5,6,7,8,9,'.',]
for i in range(len(numbers)):
    numbers[i] = str(numbers[i])
is_input_1_correct = True
for i in range(len(input_1)):
    print()
    print('{} of {}'.format(i, len(input_1)))
    print('current:', input_1[i])
    current = input_1[i]
    if current not in numbers:
        is_input_1_correct = False
        print()
        print('ne chislo')
        print()
print()

numbers = [0,1,2,3,4,5,6,7,8,9,'.']
for i in range(len(numbers)):
    numbers[i] = str(numbers[i])
is_input_2_correct = True
for i in range(len(input_2)):
    print()
    print()
    print('{} of {}'.format(i, len(input_2)))
    print('current:', input_2[i])
    current = input_2[i]
    if current not in numbers:
        is_input_2_correct = False
        print()
        print('ne chislo')
        print()
        

print('program finish')




