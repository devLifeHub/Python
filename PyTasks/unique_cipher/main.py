def count_unique_characters(mes: str) -> int:
    mes_lower = mes.lower()
    unique_chars = len(list(filter(lambda char: mes_lower.count(char) == 1, mes_lower)))
    return unique_chars


if __name__ == "__main__":
    # Пример использования:
    message = "Today is a beautiful day! The sun is shining and the birds are singing."

    unique_count = count_unique_characters(message)
    print("Количество уникальных символов в строке:", unique_count)
