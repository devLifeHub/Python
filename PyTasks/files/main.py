file_name = input("Название файла: ")
sym = "@№$%^&*()"
sym_tuple = tuple(sym)

if file_name.startswith(sym_tuple):
    print("Ошибка: название начинается на один из специальных символов.")
elif not file_name.endswith((".txt", ".docx")):
    print("Ошибка: неверное расширение файла. Ожидалось .txt или .docx.")
else:
    print("Файл назван верно.")
