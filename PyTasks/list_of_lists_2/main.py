nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

res_list = [num for fst_list in nice_list for sec_list in fst_list for num in sec_list]
print('Ответ:', res_list)