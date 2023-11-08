def sum_and_dif():
    num = int(input('Введите число: '))
    count = 0
    num_sum = 0
    while num != 0:
        count += 1
        rest_num = num % 10
        num_sum += rest_num
        num //= 10
    num_dif = num_sum - count
    return num_sum, count, num_dif

result_sum, result_count, num_dif = sum_and_dif()
print('Сумма чисел:', result_sum)
print('Количество цифр в числе:', result_count)
print('Разность суммы и количества цифр:', num_dif)
