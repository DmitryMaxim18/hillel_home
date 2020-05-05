# def no_numbers(file_path):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         text = file.read()
#         for i in range(10):
#             if str(i) in text:
#                 text = text.replace(str(i), '')
#     with open('text_without_numbers', 'w', encoding='utf-8') as file_new:
#         file_new.write(text)
#         print('*** see changes in text_without_numbers.txt ***')
#     return file_new
#
#
# no_numbers(r"text_with_numbers.txt")


# def arabian_to_roman(data):
#     units = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
#     dozens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
#     hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
#     thousands = ["", "M", "MM", "MMM", "Mv", "v"]
#
#     thousands = thousands[data // 1000]
#     hundreds = hundreds[data // 100 % 10]
#     dozens = dozens[data // 10 % 10]
#     units = units[data % 10]
#
#     return thousands + hundreds + dozens + units
#
#
# print(arabian_to_roman(1234))


# def roman_to_arabian(data):
#     number = 0
#     rome_dict = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }
#
#     for i in range(len(data) - 1):
#         if (rome_dict[data[i]] < rome_dict[data[i + 1]]):
#             number = number - rome_dict[data[i]]
#         elif (rome_dict[data[i]] >= rome_dict[data[i + 1]]):
#             number = number + rome_dict[data[i]]
#
#     number = number + rome_dict[data[len(data) - 1]]
#
#     return number
#
#
# print(roman_to_arabian('MCCXXXIV'))

# alpha_en = [
#     'a', 'b', 'c', 'd', 'e',
#     'f', 'g', 'h', 'i', 'j',
#     'k', 'l', 'm', 'n', 'o',
#     'p', 'q', 'r', 's', 't',
#     'u', 'v', 'w', 'x', 'y',
#     'z'
# ]
#
# alpha_ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж',
#             'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
#             'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш',
#             'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
#
#
# def open_file(file_path):
#     with open(file_path, encoding='utf-8') as file:
#         text = file.read()
#         return text
#
#
# def check_en(file_data, key):
#     encoded_text = file_data[:].lower()
#     for letter in alpha_en:
#         position = alpha_en.index(letter)
#         new_position = (position - int(key)) % len(alpha_en)
#         if letter in file_data.lower():
#             encoded_text = encoded_text.replace(letter, alpha_en[new_position].upper())
#     return encoded_text
#
#
# def check_ru(file_data, key):
#     encoded_text = file_data[:].lower()
#     for letter in alpha_ru:
#         position = alpha_ru.index(letter)
#         new_position = (position - int(key)) % len(alpha_ru)
#         if letter in file_data.lower():
#             encoded_text = encoded_text.replace(letter, alpha_ru[new_position].upper())
#     return encoded_text
#
#
# def cesar_decoder(file_path, key):
#     text = open_file(file_path)
#     ready_en_text = check_en(text, key)
#     try:
#         check_en(text, key)
#         check_ru(ready_en_text, key)
#         with open('clear_text', 'w', encoding='utf-8') as new_file:
#             new_file.write(check_ru(ready_en_text, key))
#             print('*** see changes in clear_text.txt ***')
#     except ValueError:
#         print(f'wrong data key: {key} should be integer')
#     return new_file
#
#
# cesar_decoder(r'coded_text', 3)

