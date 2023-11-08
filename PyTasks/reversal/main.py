# Вариант 1
text = input('Введите строку: ')

if 'h' in text:
    first = text.index('h')
    second = text.rindex('h')
    text_result = text[first+1:second][::-1]
    print('Развёрнутая последовательность между первым и последним h:', text_result)
else:
    print('В строке отсутствует буква h :(((')

# Вариант 2
# text = input('Введите строку: ')
# separator = ''
#
# if 'h' in text:
#     text_index_left = text.index('h')
#     text_index_right = text[::-1].index('h')
#
#     list_rev = list_rev[::-1] = [text[l] for l in range(text_index_left + 1, len(text) - text_index_right - 1)]
#     print(f'Развёрнутая последовательность между первым и последним h: {separator.join(list_rev)}')
# else:
#     print('В строке отсутствует буква h :(((')
