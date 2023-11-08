# Вариант №1
# word = input('Введите слово: ').lower()
# word_revers = word[:: -1]
#
# if word == word_revers:
#     print('Слово является палиндромом')
# else:
#     print('Слово не является палиндромом')

# Вариант №2
word = input('Введите слово: ').lower()
word_revers = []

for letter in word:
    word_revers.insert(0, letter)
word_revers = ''.join(word_revers)

if word == word_revers:
    print('Слово является палиндромом')
else:
    print('Слово не является палиндромом')