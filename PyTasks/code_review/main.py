students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def get_stud_info(stud):
    set_interests = set()
    total_surname_length = 0

    stud_id_and_age = [(i_id, i_age['age']) for i_id, i_age in stud.items()]
    for i_stud in stud.values():
        set_interests.update(i_stud['interests'])
        total_surname_length += len(i_stud['surname'])
    return stud_id_and_age, set_interests, total_surname_length


stud_id_age, stud_interests, total_surname_len = get_stud_info(students)

print('Список пар "ID студента — возраст":', stud_id_age)
print('Полный список интересов всех студентов:', stud_interests)
print('Общая длина всех фамилий студентов:', total_surname_len)
