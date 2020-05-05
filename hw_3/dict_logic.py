# exercise_1

# number = input('enter your number')
# if number.isdigit():
#     print('your number Even') if (abs(float(number)) % 2) == 0 else print('your number is Odd')
# elif number[0] == '-' and number[1:].isdigit():
#     print('Your number Even') if (abs(float(number)) % 2) == 0 else print('your number is Odd')
# else:
#     print('not support')

# exercise_2

# values = input('enter values separated by comma')
# if (values.replace(',', '')).isdigit():
#     new_values = values.split(',')
#     if len(new_values) < 10:
#         print(sorted(new_values, key=int))
#     else:
#         print((sorted(new_values, key=int))[::-1])
# else:
#     new_values = values.split(',')
#     if len(new_values) < 10:
#         print(sorted(new_values))
#     else:
#         print((sorted(new_values))[::-1])

# exercise_3

# num_1 = input('enter first number')
# num_2 = input('enter second number')
# if num_1.lstrip('-').replace('.', '').isdigit() and num_2.lstrip('-').replace('.', '').isdigit() and num_1 > num_2:
#     print(f'{float(num_1)- float(num_2)}')
# elif num_1.lstrip('-').replace('.', '').isdigit() and num_2.lstrip('-').replace('.', '').isdigit() and num_1 < num_2:
#     print(f'{float(num_1) + float(num_2)}')
# elif num_1.lstrip('-').replace('.', '').isdigit() and num_2.lstrip('-').replace('.', '').isdigit() and num_1 == num_2:
#     print(f'{float(num_1) ** float(num_2)}')
# else:
#     print('wrong input')

# exercise_4

# a = input('enter a')
# b = input('enter b')
# c = input('enter c')
# if a.lstrip('-').replace('.', '').isdigit()\
#         and b.lstrip('-').replace('.', '').isdigit()\
#         and c.lstrip('-').replace('.', '').isdigit():
#     if (float(a) - float(b) + float(c)) == 0:
#         print('zero division')
#     else:
#         formula = 2*float(a) - 8*float(b)/(float(a) - float(b) + float(c))
#         print(formula)
# else:
#     print('wrong input')

# exercise_5

# lst = list(range(1, 9))
# count = 0
# for number in lst:
#     if number % 2 == 0:
#         count += 1
# print(f'{count} Even numbers')

# exercise_6

# lst = [5, 0, 14, -3, 6, 2, 9, 1]
# lst_new = []
# for i in range(len(lst)):
#     min_lst_item = lst.pop(lst.index(min(lst)))
#     lst_new.append(min_lst_item)
# print(lst_new)

# exercise_7

# NUM_1 = 0
# NUM_2 = 1
# length = input('enter your length')
# if length.isdigit() and int(length) != 0:
#     length = int(length)
#     while length != 0:
#         next_num = NUM_1 + NUM_2
#         NUM_1 = NUM_2
#         NUM_2 = next_num
#         length -= 1
#         print(next_num)
# else:
#     print('wrong data type')

# exercise_8

# number = input('number')
# if number != '1' and number.isdigit() and int(number) != 0:
#     if int(number) > 2 and int(number) % 2 == 0:
#         print('complex')
#     else:
#         print('simple')
# else:
#     print('must be integer number 2 and more')








