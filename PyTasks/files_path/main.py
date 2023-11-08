import os
from typing import Any


def find_dir(dir_name: str, dir_root: str = '/') -> Any:
    for dir_path, dir_names, _ in os.walk(dir_root):
        if dir_name in dir_names:
            return os.path.join(dir_path, dir_name)
    return None


input_dir_name = '02_files_path'
find_dir_path = find_dir(input_dir_name, '/')

if find_dir_path:
    print('Директория {} найдена по пути: {}'.format(input_dir_name, find_dir_path))
else:
    print('Директория {} не найдена в файловой системе.'.format(input_dir_name))
