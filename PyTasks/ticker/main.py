str1 = input("Первая строка: ")
str2 = input("Вторая строка: ")

if len(str1) != len(str2):
    print("Первую строку нельзя получить из второй с помощью циклического сдвига.")
else:
    extended_str2 = str2 + str2
    if str1 in extended_str2:
        shift = extended_str2.index(str1)
        print("Первая строка получается из второй со сдвигом {}.".format(shift))
    else:
        print("Первую строку нельзя получить из второй с помощью циклического сдвига.")
