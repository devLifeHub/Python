list_name = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
list_name_sort = []

for name in range(0, len(list_name), 2):
    name_sort = list_name[name]
    list_name_sort.append(name_sort)

print('Первый день:', list_name_sort)