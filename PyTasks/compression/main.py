def encode_string(s):
    encoded = ''
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded += s[i - 1] + str(count)
            count = 1

    encoded += s[-1] + str(count)

    return encoded


input_string = input('Введите строку: ')
encoded_string = encode_string(input_string)
print('Закодированная строка:', encoded_string)
