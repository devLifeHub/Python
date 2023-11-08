from typing import Any


class File:
    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self) -> Any:
        try:
            self.file = open(self.filename, self.mode)
        except FileNotFoundError:
            self.file = open(self.filename, 'w')
        return self.file

    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> bool:
        if self.file:
            self.file.close()
        if exc_type is not None:
            print(f"Произошла ошибка: {exc_type} - {exc_value}")
            return True


with File('example.txt', 'r') as f:
    file = f.read()
