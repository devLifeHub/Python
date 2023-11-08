import re


def check_phone_numbers(phone_list):
    for i, num in enumerate(phone_list):
        if re.match(r'^[89]\d{9}$', num):
            print('{}-й номер: всё в порядке'.format(i + 1))
        else:
            print('{}-й номер: не подходит'.format(i + 1))


phone_numbers = ['9999999999', '999999-999', '99999x9999']

check_phone_numbers(phone_numbers)
