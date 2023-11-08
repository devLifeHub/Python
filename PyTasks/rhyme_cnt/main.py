
num_persons = int(input('Количество человек: '))
index_persons = int(input('Какое число в считалке? '))

list_persons = list(range(1, num_persons + 1))
current_person = 0

while len(list_persons) > 1:
    print('Текущий круг людей:', list_persons)
    print('Начало счёта с номера',list_persons[current_person])
    current_person = (current_person + index_persons - 1) % len(list_persons)
    removed_person = list_persons.pop(current_person)
    print('Выбывает человек под номером', removed_person)
    current_person %= len(list_persons)
    print()

print('Остался человек под номером', list_persons[0])