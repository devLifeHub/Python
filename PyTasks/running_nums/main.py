initial_list = [1, 2, 3, 4, 5]
shifted_list = initial_list[:]

shift_num = int(input('Введите сдвиг: '))

for shift in range(shift_num):
    last_num = shifted_list[-1]
    shifted_list.remove(shifted_list[-1])
    shifted_list.insert(0, last_num)

print('Изначальный список:', initial_list)
print('Сдвинутый список:', shifted_list)
