list_skates = []
list_feet = []
resemblance = 0

def comparison_size(count, size_text, size_list):
    for i in range(count):
        if size_text == 'skates':
            pair_size = int(input(f'Размер {i + 1}-й пары: '))
        if size_text == 'feet':
            pair_size = int(input(f'Размер {i + 1}-й пары: '))
        size_list.append(pair_size)

count_skates = int(input('Кол-во коньков: '))
comparison_size(count_skates, 'skates', list_skates)

count_feet = int(input('Кол-во людей: '))
comparison_size(count_feet, 'feet', list_feet)

list_skates_dup = list_skates[:]
for i_feet in list_feet:
    if i_feet in list_skates_dup:
        resemblance += 1
        print(i_feet)
        list_skates_dup.remove(i_feet)

print('Наибольшее кол-во людей, которые могут взять ролики:', resemblance)

