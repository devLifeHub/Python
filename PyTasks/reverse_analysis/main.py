numbers_list = [7, 14, 3, 18, 21, 10, 9, 6]
print('Изначальный список:', numbers_list)

for num in numbers_list:
    if num % 2 != 0:
        numbers_list.remove(num)

for i in range(len(numbers_list) - 1, -1, -1):
    numbers_list.append(numbers_list[i])
    numbers_list.remove(numbers_list[i])

print('Отсортированный список:', numbers_list)
