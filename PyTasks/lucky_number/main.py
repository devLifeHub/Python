import random


def write_file(num, f_name):
    with open(f_name, 'a') as file_a:
        file_a.write(str(num) + '\n')


file_name = 'out_file.txt'

total_sum = 0

while total_sum < 777:
    try:
        number = int(input('Введите число: '))
        write_file(number, file_name)
        total_sum += number
        if random.randint(1, 13) == 13:
            raise Exception("Вас постигла неудача!")
    except ValueError:
        print('Вы ввели некорректное число. Попробуйте снова.')

print('Вы успешно выполнили условие для выхода из порочного цикла!')

with open(file_name, 'r') as file_r:
    print("\nСодержимое файла {}: ".format(file_name))
    print(file_r.read())
