import re
import requests
from typing import List


def search_tag_html(text: str) -> List[str]:
    return re.findall(r'<h3>(.*?)</h3>', text)


if __name__ == "__main__":
    print('Выберете:\n \t1 - поиск через get запрос\n \t2 - поиск в html-файле')
    choice = int(input('Введите 1 или 2: '))

    if choice == 1:
        response = requests.get("https://webref.ru/html/h3")
        html_text = response.text
        print(search_tag_html(html_text))

    elif choice == 2:
        with open('examples.html', 'r') as f:
            html_text = f.read()
        print(search_tag_html(html_text))
