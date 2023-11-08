import os
from typing import Generator


def error_log_generator(data_dir: str) -> Generator[str, None, None]:
    for path_dir, _, files in os.walk(data_dir):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(path_dir, file)
                error = "ERROR"

                try:
                    with open(file_path, 'r', encoding='utf-8') as file_r:
                        print(file_path)
                        for line in file_r:
                            if error in line:
                                yield line
                except FileNotFoundError:
                    print('Файл {} не найден.'.format(path_dir))
                except Exception as e:
                    print('Произошла ошибка при чтении файла {}: {}'.format(file_path, str(e)))


curr_dir = os.path.abspath(os.getcwd())
input_file_path = os.path.join(curr_dir, 'data')

output_file_path = 'error_file.txt'

with open(output_file_path, 'w', encoding='utf-8') as output:
    for error_line in error_log_generator(input_file_path):
        output.write(error_line)

print("Файл успешно обработан.")
