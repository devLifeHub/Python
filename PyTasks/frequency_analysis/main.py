def file_text(text):
    open('text.txt', 'w').write(text)
    result = count_letter()

    analysis = open('analysis.txt', 'w')
    for i_elem in result:
        analysis.write('{} {} \n'.format(i_elem[0], i_elem[1]))
    analysis.close()


def count_letter():
    text_r = open('text.txt', 'r')
    text_line = text_r.readline()
    count_dict = {}

    for letter in text_line.lower():
        if letter.isalpha():
            if letter in count_dict:
                count_dict[letter] += 1
            else:
                count_dict[letter] = 1

    total_letters = sum(count_dict.values())
    count_dict = {i_key: round(i_value / total_letters, 3) for i_key, i_value in count_dict.items()}
    sorted_items = sorted(count_dict.items())
    sorted_list = sorted(sorted_items, key=lambda x: x[1], reverse=True)
    return sorted_list


text_input = input('Введите текст: ')
file_text(text_input)
