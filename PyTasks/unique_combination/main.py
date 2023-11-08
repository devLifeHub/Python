def merge_sorted_lists(list1, list2):
    list1.extend(list2)
    return list(set(list1))

list1 = [9, 1, 3, 7, 5]
list2 = [2, 4, 5, 6, 8, 10]
merged = merge_sorted_lists(list1, list2)
print(merged)