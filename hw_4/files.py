with open('cesar', 'r', encoding='utf-8') as file:
    text = file.read()

alpha_en = [
    'a', 'b', 'c', 'd', 'e',
    'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y',
    'z'
]

alpha_ru = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж',
            'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п',
            'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш',
            'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

key = input('input int key')
new_text = ''

try:
    for index, value in enumerate(text.lower()):
        original_text_letter = text[index]
        if value.isalpha() and value not in alpha_ru:
            position = alpha_en.index(value)
            new_position = (position + int(key)) % len(alpha_en)
            new_text += alpha_en[new_position] if value == original_text_letter else alpha_en[new_position].upper()
        elif value in digits:
            position = digits.index(value)
            new_position = (position + int(key)) % len(digits)
            new_text += digits[new_position]
        elif value in alpha_ru:
            position = alpha_ru.index(value)
            new_position = (position + int(key)) % len(alpha_ru)
            new_text += alpha_ru[new_position] if value == original_text_letter else alpha_ru[new_position].upper()
        else:
            new_text += value
    with open('clear_text', 'w', encoding='utf-8') as new_file:
        new_file.write(new_text)
        print('*** see changes in clear_text.txt ***')
except ValueError:
    print(f'wrong data key: {key} should be integer')


