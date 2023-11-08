text = input('Введите строку: ').split(' ')

max_word = max(text, key=len)
num_word = len(max_word)

print('Самое длинное слово:', max_word)
print('Длина этого слова:', num_word)