# a = [1, 5, 3]
# b = [1, 5, 1, 5]
# c = [1, 3, 1, 5, 3, 3]
# for i in b:
#     a.append(i)
# t = 0
# for i in a:
#     if i == 5:
#         t += 1
# print(t)
# d = []
# for i in a:
#     if i != 5:
#         d.append(i)
# for i in c:
#     d.append(i)
# t = 0
# for i in d:
#     if i == 3:
#         t += 1
# print(t)
# print(d)


list1 = [1, 5, 3]
list2 = [1, 5, 1, 5]
list3 = [1, 3, 1, 5, 3, 3]

def find_del_num(num, list):
    count = 0
    i = 0
    while i < len(list):
        if list[i] == num:
            count += 1
            del list[i]
        else:
            i += 1
    return count

list1.extend(list2)
count_five = find_del_num(5, list1)
list1.extend(list3)
count_three = find_del_num(3, list1)

print('Кол-во цифр 5 при первом объединении:', count_five)
print('Кол-во цифр 3 при втором объединении:', count_three)
