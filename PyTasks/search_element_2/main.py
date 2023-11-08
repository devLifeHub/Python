def find_key(dictionary, s_key, depth=None, current_depth=0):
    if isinstance(dictionary, dict):
        if s_key in dictionary:
            if depth is None or current_depth < depth:
                return dictionary[s_key]
        elif depth is None or current_depth < depth:
            for key, value in dictionary.items():
                res = find_key(value, s_key, depth, current_depth + 1)
                if res is not None:
                    return res
    return None


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

search_key = input("Введите искомый ключ: ")
max_depth_input = input("Хотите ввести максимальную глубину? Y/N: ").strip().lower()

if max_depth_input == 'y':
    max_depth = int(input("Введите максимальную глубину: "))
else:
    max_depth = None

result = find_key(site, search_key, max_depth)

print("Значение ключа:", result)
