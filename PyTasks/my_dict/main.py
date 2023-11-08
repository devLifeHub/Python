# Вариант 1
class MyDict(dict):
    def __getitem__(self, key):
        return super().get(key, 0)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)


my_dict = MyDict()
my_dict['a'] = 42
my_dict['b'] = 56

print(my_dict['a'])
print(my_dict['c'])
print(my_dict['e'])
print(my_dict['b'])
print(my_dict['d'])
print(my_dict)


# Вариант 2
# class MyDict:
#     def __init__(self):
#         self.__data = {}
#
#     def get(self, key, default=0):
#         return self.get(key, default)
#
#     def __getitem__(self, key):
#         return self.__data.get(key, 0)
#
#     def __setitem__(self, key, value):
#         self.__data[key] = value
#
#     def __repr__(self):
#         return repr(self.__data)
#
#
# my_dict = MyDict()
# my_dict['a'] = 42
# my_dict['b'] = 56
#
# print(my_dict['a'])
# print(my_dict['c'])
# print(my_dict['b'])
# print(my_dict['d'])
# print(my_dict)


