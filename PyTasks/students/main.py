class Student:
    def __init__(self, surname, name, number, progress):
        self.surname = surname
        self.name = name
        self.number = number
        self.progress = progress

    def progress_gpa(self):
        return sum(self.progress) / len(self.progress)


def group_students():
    num_students = int(input('Введите количество студентов: '))
    for i_num in range(1, num_students + 1):
        grade_list = []
        surname_students = input('Введите фамилию {}-го студента: '.format(i_num))
        name_students = input('Введите имя {}-го студента: '.format(i_num))
        num_group = int(input('Введите номер группы {}-го студента: '.format(i_num)))

        for i_grade in range(1, 6):
            grade = int(input('Введите {}-ю оценку: '.format(i_grade)))
            grade_list.append(grade)

        student_info = Student(surname_students, name_students, num_group, grade_list)
        students.append(student_info)


students = []
group_students()
sorted_students = sorted(students, key=lambda stud: student.progress_gpa())

for student in sorted_students:
    print('Студент: {surname} {name}, Группа: {group}, Средний балл: {gpa}'.format(
        surname=student.surname,
        name=student.name,
        group=student.number,
        gpa=student.progress_gpa()
    ))
