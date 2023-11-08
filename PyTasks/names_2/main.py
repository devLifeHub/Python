total_letter = 0
line_count = 0
lines = []


def added_people(num):
    with open('people.txt', 'a', encoding='utf-8') as file_a:
        for _ in range(num):
            name = input('Введите имя пользователя: ').title()
            file_a.write(name + '\n')


num_people = int(input('Введите количество пользователей: '))
added_people(num_people)

try:
    with open('people.txt', 'r', encoding='utf-8') as file_r:
        lines = file_r.readlines()
        lines.reverse()

    for i_line in lines:
        name_len = len(i_line.strip())
        line_count += 1
        try:
            if name_len < 3:
                raise Exception('Ошибка: менее трёх символов в строке {}.'.format(line_count))
        except Exception as error:
            with open('errors.txt', 'a', encoding='utf-8') as errors_w:
                errors_w.write(str(error) + '\n')
            print(error)
        total_letter += name_len

except FileNotFoundError:
    print('Файл не найден')
finally:
    print('Общее количество символов: {}.'.format(total_letter))
