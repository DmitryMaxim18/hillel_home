# exercise_1

# data_array = [1, 3, 5, 'abc', [1, 0]]
# last_element = data_array.pop()
# print(last_element)

# exercise_2

# data_array = [1, 3, 5, 'abc', [1, 0]]
# first_number = int(input('enter first number'))
# second_number = int(input('enter second number'))
# array_elements = data_array[first_number:second_number]
# print(array_elements)

# exercise_3

# user_string = input('type your string')
# print(list(set(user_string)))

# exercise_4

# first_set = {1, 2, 4, 5, 6, 7}
# second_set = {4, 2, 3, 5, 6, 7}
# result = set.intersection(first_set, second_set)
# print(f"intersection {result}\n"
#       f"difference between first element and second element is {list(result)[0]-list(result)[-1]}")

# exercise_5

# first_array = [1, 2, 5, 4, 2]
# second_array = [1, 3, 4, 8]
# result_array = list(set(first_array + second_array))
# print(result_array)

# exercise_6

# data_tuple = (1, 2, 5, 4, 2)
# data_list = [1, 3, 4, 8]
# result = set(data_tuple).intersection(data_list)
# print(str(list(result)[0:]).strip('[]'))

# exercise_7

# text = "Lorem Ipsum - это текст-'рыба', часто используемый в печати и вэб-дизайне. " \
#         "Lorem Ipsum является стандартной 'рыбой' для текстов на латинице с начала XVI века. " \
#         "В то время некий безымянный печатник создал большую коллекцию размеров и форм шрифтов," \
#         " используя Lorem Ipsum для распечатки образцов."
# print(text.count('.'))

# exercise_8

# seq = [1, 3, 5, 9, 15]
# first_index, last_index = seq[0], seq[-1]
# missed_element = sorted(set(range(first_index, last_index + 1, 2)).difference(seq))
# print(f"{str(missed_element).strip('[]')} missing")



