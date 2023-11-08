import os


def calculate_directory_size(path):
    total_size = 0
    total_files = 0
    total_dirs = 0

    for dirpath, dirnames, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
            total_files += 1

        total_dirs += len(dirnames)

    return total_size, total_files, total_dirs


catalog = 'Module14'
directory_path = os.path.abspath(os.path.join('..', '..', catalog))

size, files, dirs = calculate_directory_size(directory_path)
size_kb = size / 1024

print('Размер каталога (в Кб): {}'.format(size_kb))
print('Количество подкаталогов: {}'.format(dirs))
print('Количество файлов: {}'.format(files))

# def main():
#     catalog = 'Module14'
#     directory_path = os.path.abspath(os.path.join('..', '..', catalog))
#
#     try:
#         total_size, total_files, total_dirs = calculate_directory_size(directory_path)
#         size_in_kb = total_size / 1024
#
#         print(f"Размер каталога (в Кб): {size_in_kb}")
#         print(f"Количество подкаталогов: {total_dirs}")
#         print(f"Количество файлов: {total_files}")
#     except FileNotFoundError:
#         print("Каталог не найден.")
