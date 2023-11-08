# list_num = [1, 4, -3, 0, 10]
# print('Изначальный список:', list_num)
# list_num.sort()
# print('Отсортированный список:', list_num)
def selection_sort(my_list):
    for i_mn in range(len(my_list)):
        for curr in range(i_mn, len(my_list)):
            if my_list[curr] < my_list[i_mn]:
                my_list[curr], my_list[i_mn] = my_list[i_mn], my_list[curr]

nums = [1, 4, -3, 0, 10]

print('Изначальный список:', nums)
selection_sort(nums)
print('Отсортированный список:', nums)
