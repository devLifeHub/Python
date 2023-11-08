def is_prime(num):
    if num <= 1:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True


def crypto(text):
    return [elem for index, elem in enumerate(text) if is_prime(index)]


print(crypto(list(range(10))))
print(crypto('О Дивный Новый мир!'))


# def is_prime(num):
#     if (not (num <= 1) and
#             not (num % 2 == 0 or num % 3 == 0 or num % 5 == 0 or num % 7 == 0)
#             or (num == 2 or num == 3 or num == 5 or num == 7)):
#         return True
#     else:
#         return False
#
#
# def crypto(text):
#     return [elem for index, elem in enumerate(text) if is_prime(index)]
#
#
# print(crypto(list(range(10))))
# print(crypto('О Дивный Новый мир!'))
