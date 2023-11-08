def caesar_cipher(string, user_shift):
    char_list = [(alphabet[(alphabet.index(sym) + user_shift) % len(alphabet)] if sym != ' ' else ' ') for sym in string]
    new_str = ''
    for i_char in char_list:
        new_str += i_char
    return new_str

alphabet = 'абвгдеëжзийклмнопрстуфхцчшщъыьэюя'
print(len(alphabet))
input_str = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

output_str = caesar_cipher(input_str, shift)

print('Зашифрованное сообщение:', output_str)


