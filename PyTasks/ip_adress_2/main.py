def is_valid_ip(ip):
    list_ip = ip.split('.')

    if len(list_ip) == 4:
        for el in list_ip:
            if not el.isdigit():
                print('{} — это не целое число.'.format(el))
                break
            elif int(el) > 255:
                print('{} превышает 255.'.format(el))
                break
        else:
            print('IP-адрес корректен.')
    else:
        print('Адрес — это четыре числа, разделённые точками.')


ip_address = input('Введите IP: ')
is_valid_ip(ip_address)
