text = input('Введите текст: ')
list_vowel = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

list_text_vowel = [letter for letter in text if letter in list_vowel]
count = len(list_text_vowel)

print(list_text_vowel)
print('Количество гласных букв:', count)