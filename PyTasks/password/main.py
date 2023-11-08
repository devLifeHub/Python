while True:
    password = input('Придумайте пароль: ')

    contains_upper = any(letter.isupper() for letter in password)
    contains_digits = sum(1 for letter in password if letter.isdigit()) >= 3

    if len(password) >= 8 and contains_upper and contains_digits:
        print('Это надёжный пароль!')
        break
    else:
        print('Пароль ненадёжный. Попробуйте ещё раз.')

