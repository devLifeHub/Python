guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    print(f'Сейчас на вечеринке {len(guests)} человек: {guests}')
    action = input('Гость пришёл или ушёл? ')
    if action == 'пришел':
        name = input('Имя гостя: ')
        if len(guests) < 6:
            guests.append(name)
            print(f'Привет, {name}!')
        else:
            print(f'Прости, {name}, но мест нет.')
    if action == 'ушел':
        name = input('Имя гостя: ')
        if name in guests:
            guests.remove(name)
            print(f'Пока, {name}!')
        else:
            print(f'{name} на вечеринке нет!')
    if action == 'Пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break