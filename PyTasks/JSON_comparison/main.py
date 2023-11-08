import json
from typing import Any, Dict


def compare_dict(old_dict: Dict[str, Any], new_dict: Dict[str, Any], path: str = "") -> None:
    global result
    for key in old_dict:
        if key in diff_list:
            if old_dict[key] != new_dict[key]:
                result[key] = new_dict[key]
        if isinstance(old_dict[key], dict) and key in new_dict and isinstance(new_dict[key], dict):
            compare_dict(old_dict[key], new_dict[key], path + key + "/")


if __name__ == "__main__":
    with open('json_old.json', 'r', encoding='utf-8') as old_file:
        data_old = json.load(old_file)

    with open('json_new.json', 'r', encoding='utf-8') as new_file:
        data_new = json.load(new_file)

    diff_list = ["services", "staff", "datetime"]
    result = {}

    compare_dict(data_old, data_new)
    print(result)

    with open('result.json', 'w', encoding='utf-8') as result_file:
        json.dump(result, result_file, ensure_ascii=False, indent=4)
