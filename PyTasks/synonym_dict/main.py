num_pair_word = int(input("Введите количество пар слов: "))

synonyms_dict = {}

for i_pair_word in range(num_pair_word):
    pair = input('Введите {}-ую пару слов через тире: '.format(i_pair_word + 1))
    words = pair.split(" — ")
    if len(words) == 2:
        word1, word2 = words
        synonyms_dict[word1.lower()] = word2
        synonyms_dict[word2.lower()] = word1
    else:
        print('Неверный формат пары слов. Введите пару снова.')

while True:
    word = input("Введите слово: ").lower()
    if word in synonyms_dict:
        synonym = synonyms_dict[word]
        print("Синоним: {}".format(synonym))
        break
    else:
        print("Такого слова в словаре нет.")
