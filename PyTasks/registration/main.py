def registration_check(line):
    try:
        list_line = line.split()
        name, email, age = list_line
        age = int(age)

        if not len(list_line) == 3:
            print(line)
            print(len(line))
            raise IndexError('НЕ присутствуют все три поля')

        if not name.isalpha():
            raise NameError('Поле «Имя» содержит НЕ только буквы')

        if not ('@' in email) and not ('.' in email):
            raise SyntaxError('Поле «Имейл» НЕ содержит @ и . (точку)')

        if age < 10 or age > 99:
            raise ValueError('Поле «Возраст» НЕ является числом от 10 до 99')

        with open('registrations_good.log', 'a') as file_good:
            file_good.write(line + '\n')

    except (IndexError, NameError, SyntaxError, ValueError) as e:
        error_message = '{:<40} --> {:<40}{}'.format(line.strip(), str(e), '')
        with open('registrations_bad.log', 'a') as file_bad:
            file_bad.write(error_message + '\n')


with open('registrations.txt', 'r') as file:
    for i_line in file:
        registration_check(i_line)
