num = int(input('Введите число: '))
def least_divisor(num):
    for n in range(2, num + 1):
        if num % n == 0:
            return n
    return num

divisor = least_divisor(num)
print(divisor)