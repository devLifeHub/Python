array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]
# array_1 = [1, 2, 3, 4]
# array_2 = [2, 4]
# array_3 = [2, 3]

set_1, set_2, set_3 = set(array_1), set(array_2), set(array_3)

# task 1
print('Задача 1:')
# Решение без множеств
rep_elem = [i_el for i_el in array_1 if (i_el in array_2) and (i_el in array_3)]
result_str = ', '.join(map(str, rep_elem))
print("\t Решение без множеств:", result_str)

# Решение с множествами
set_rep_elem = set_1 & set_2 & set_3
result_str = ', '.join(map(str, set_rep_elem))
print("\t Решение с множествами:", result_str)

# task 2
print()
print('Задача 2:')
# Решение без множеств
excl_elem = [i_el for i_el in array_1 if not (i_el in array_2) and not (i_el in array_3)]
result_str = ', '.join(map(str, excl_elem))
print("\t Решение без множеств:", result_str)

# Решение с множествами
set_excl_elem = set_1 - set_2 - set_3
result_str = ', '.join(map(str, set_excl_elem))
print("\t Решение с множествами:", result_str)
