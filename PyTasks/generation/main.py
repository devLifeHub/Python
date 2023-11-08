list_len = int(input('Введите длину списка: '))
list_num = list(range(list_len))

list_sort = [(num % 5 if i % 2 != 0 else 1) for i, num in enumerate(list_num)]
print('Результат:', list_sort)
