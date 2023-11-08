num = int(input('Введите число: '))
num_even = []

for i in range(1, num + 1, 2):
    num_even.append(i)
print('Список из нечётных чисел от одного до N:', num_even)