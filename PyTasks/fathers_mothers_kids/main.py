# Вариант №1
class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.children = []

    def add_child(self, child):
        if self.age - 16 >= child.age:
            self.children.append(child)
        else:
            print('{name} не может быть ребенком {childName}, так как у них маленькая разница в возрасте.'.format(
                name=self.name,
                childName=child.name
            ))

    def introduce(self):
        print('Меня зовут {name}, мне {age} лет.'.format(
            name=self.name,
            age=self.age
        ))

    def calm_child(self, child):
        if child in self.children:
            child.set_calm(True)
            print('{name} успокоил(-а) ребёнка {childName}.'.format(
                name=self.name,
                childName=child.name
            ))
        else:
            print('{name} не успокоил(-а) ребёнка {childName}, так как это не его(ее) ребенок.'.format(
                name=self.name,
                childName=child.name
            ))

    def feed_child(self, child):
        if child in self.children:
            child.set_hungry(True)
            print('{name} покормил(-а) ребёнка {childName}.'.format(
                name=self.name,
                childName=child.name
            ))
        else:
            print('{name} не покормил(-а) ребёнка {childName}, так как это не его(ее) ребенок.'.format(
                name=self.name,
                childName=child.name
            ))


class Child:
    def __init__(self, name, age):
        self.calm = False
        self.hungry = False
        self.name = name
        self.age = age

    def set_calm(self, value):
        self.calm = value

    def set_hungry(self, value):
        self.hungry = value

    def state_info(self):
        print('{name} имеет состояния: спокойствие - {calm}, голод - {hungry}.'.format(
            name=self.name,
            calm=self.calm,
            hungry=self.hungry
        ))


parent = Parent("Мама", 40)
child1 = Child("Сын", 10)
child2 = Child("Сын2", 40)

parent.add_child(child1)
parent.add_child(child2)

parent.introduce()
child1.state_info()
child2.state_info()

parent.calm_child(child1)
child1.state_info()
child2.state_info()

parent.feed_child(child1)
child1.state_info()
child2.state_info()

parent.calm_child(child2)
child1.state_info()
child2.state_info()


# Вариант №2
# class Parent:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def add_child(self, child):
#         if self.age - 16 >= child.age:
#             return True
#         else:
#             print('{name} не может быть ребенком {childName}.'.format(
#                 name=self.name,
#                 childName=child.name
#             ))
#             return False
#
#     def introduce(self):
#         print('Меня зовут {name}, мне {age} лет.'.format(
#             name=self.name,
#             age=self.age
#         ))
#
#     def calm_child(self, child):
#         if self.add_child(child):
#             child.set_calm(True)
#             print('{name} успокоил ребёнка {childName}.'.format(
#                 name=self.name,
#                 childName=child.name
#             ))
#
#     def feed_child(self, child):
#         if self.add_child(child):
#             child.set_hungry(True)
#             print('{name} покормил ребёнка {childName}.'.format(
#                 name=self.name,
#                 childName=child.name
#             ))
#
#
# class Child:
#     def __init__(self, name, age, parent):
#         self.calm = False
#         self.hungry = False
#         self.name = name
#         self.parent = parent
#         self.age = age
#
#     def set_calm(self, value):
#         self.calm = value
#
#     def set_hungry(self, value):
#         self.hungry = value
#
#     def state_info(self):
#         print('{name} имеет состояния: спокойствие - {calm}, голод - {hungry}.'.format(
#             name=self.name,
#             calm=self.calm,
#             hungry=self.hungry
#         ))
#
#
# parent = Parent("Мама", 40)
# child1 = Child("Сын", 10, parent)
# child2 = Child("Сын2", 40, parent)
#
# parent.introduce()
# child1.state_info()
# child2.state_info()
#
# parent.calm_child(child1)
# child1.state_info()
# child2.state_info()
#
# parent.feed_child(child1)
# child1.state_info()
# child2.state_info()
#
# parent.calm_child(child2)
# child1.state_info()
# child2.state_info()

# Вариант №3
# class Parent:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.children = []
#
#     def introduce(self):
#         print('Меня зовут {name}, мне {age} лет.'.format(
#             name=self.name,
#             age=self.age
#         ))
#
#     def calm_child(self, child):
#         child.set_calm(True)
#         print('{name} успокоил ребёнка {childName}.'.format(
#             name=self.name,
#             childName=child.name
#         ))
#
#     def feed_child(self, child):
#         child.set_hungry(False)
#         print('{name} покормил ребёнка {childName}.'.format(
#             name=self.name,
#             childName=child.name
#         ))
#
#
# class Child:
#     def __init__(self, name, age, parent):
#         self.calm = True
#         self.hungry = True
#         self.name = name
#         self.parent = parent
#         if age >= parent.age - 16:
#             raise ValueError(
#                 'Возраст ребёнка {} должен быть меньше возраста родителя хотя бы на 16 лет.'.format(self.name))
#         self.age = age
#
#     def set_calm(self, value):
#         self.calm = value
#
#     def set_hungry(self, value):
#         self.hungry = value
#
#     def state_info(self):
#         print('{name} имеет состояния: спокойствие - {calm}, голод - {hungry}.'.format(
#             name=self.name,
#             calm=self.calm,
#             hungry=self.hungry
#         ))
#
#
# def data_input():
#     parent = Parent("Мама", 40)
#     child1 = Child("Сын", 10, parent)
#     child2 = Child("Сын2", 40, parent)
#     parent.introduce()
#     child1.state_info()
#     child2.state_info()
#
#     parent.calm_child(child1)
#     child1.state_info()
#     child2.state_info()
#
#     parent.feed_child(child1)
#     child1.state_info()
#     child2.state_info()
#
#
# try:
#     data_input()
# except ValueError as e:
#     print(e)
