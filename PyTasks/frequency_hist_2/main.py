text = input('Введите текст: ').capitalize()

text_dict = dict()
for sym in text:
    if sym in text_dict:
        text_dict[sym] += 1
    else:
        text_dict[sym] = 1

print()
print('Оригинальный словарь частот:')
for letter, freq in text_dict.items():
    print(letter, ':', freq)

inverted_dict = dict()
for key, value in text_dict.items():
    if value in inverted_dict:
        inverted_dict[value].append(key)
    else:
        inverted_dict[value] = [key]

print()
print('Инвертированный словарь частот:')
for key, value in inverted_dict.items():
    print('{}:{}'.format(key, value))