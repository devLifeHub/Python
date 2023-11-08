file_zen = open('zen.txt', 'r')
data_file_zen = file_zen.read()
file_zen.close()

data_rev = data_file_zen.split('\n')[::-1]
data_res = '\n'.join(data_rev)

file_zen_rev = open('zen_rev.txt', 'w')
file_zen_rev.write(data_res)
file_zen_rev.close()
