contacts_dict = {}


def added_contact(contacts):
    new_person = input('Введите имя и фамилию нового контакта (через пробел): ').split()
    contact = (new_person[0].capitalize(), new_person[1].capitalize())

    if contact in contacts:
        print('Такой человек уже есть в контактах.')
    else:
        new_number = int(input('Введите номер телефона: '))
        contacts[contact] = new_number
        print("Текущий словарь контактов:", contacts)


def find_contact(contacts):
    find_surname = input('Введите фамилию для поиска: ').capitalize()
    list_contact = [(name, surname, number) for (name, surname), number in contacts.items() if surname == find_surname]

    if not list_contact:
        print('Такого контакта нет в словаре!')
    else:
        for name, surname, number in list_contact:
            print(name, surname, number)


while True:
    print('Введите номер действия: ')
    print('\t 1. Добавить контакт')
    print('\t 2. Найти человека')
    action = input()

    if action == '1':
        added_contact(contacts_dict)
    elif action == '2':
        find_contact(contacts_dict)
    else:
        print('Неправильно введено действие! Попробуйте еще раз!')
