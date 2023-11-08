def print_numbers(num):
    if num > 0:
        print_numbers(num - 1)
        print(num)


print_numbers(int(input('Введите num: ')))
