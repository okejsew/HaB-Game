from typing import Any

import json5


def loader(name: str) -> dict[Any, ...]:
    """
    Грузит json5 из папки prefabs

    Args:
        name (str): Имя файла без '.json5'
    Returns:
        dict: Словарь из файла
    """
    with open('prefabs/' + name + '.json5', 'r', encoding='utf-8') as file:
        return json5.load(file)
