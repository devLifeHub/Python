list_num = list(range(int(input('Введите число: '))))
list_res = [[n for n in range(i + 1, len(list_num) + 1, 4)] for i in range(len(list_num) // 3)]
print(list_res)