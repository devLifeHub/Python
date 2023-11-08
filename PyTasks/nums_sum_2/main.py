input_file = open('numbers.txt', 'r')
file_data = input_file.read()
input_file.close()

lines = file_data.split('\n')

total = 0

for line in lines:
    numbers = line.strip().split()

    for num in numbers:
        total += int(num)

output_file = open('answer.txt', 'w')
output_file.write(str(total))
output_file.close()
