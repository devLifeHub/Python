import os
import re
from typing import Generator


def count_str_files(dirs: str) -> Generator[str, None, None]:
    comm_patt = re.compile(r'#.*')
    for _, _, files in os.walk(dirs):
        for file_py in files:
            if file_py.endswith('.py'):
                with open(file_py, 'r', encoding='utf-8') as f:
                    line_count = 0
                    for line_f in f:
                        lines = line_f.strip()

                        if not lines or comm_patt.match(lines):
                            continue

                        line_count += 1

                    yield file_py, line_count


curr_dir = os.path.abspath(os.getcwd())
for file, line in count_str_files(curr_dir):
    print('Python файл: {}, количество строк: {}'.format(file, line))
