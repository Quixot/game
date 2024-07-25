# Словарь хранит функциональную структуру уровня

import copy

level = []

# TODO Создать отдельный тип данных под каждый элемент пространства уровня
for _ in range(100):
    level.append(
        [
            {"symbol": None, "color": None},
            {"symbol": None, "color": None},
            {"symbol": None, "color": None},
            {"symbol": None, "color": None},
        ]
    )

def draw_level(base, template):
    base = copy.copy(base) # Это надо?

    for index, value in enumerate(template):
        if value:
            base[index] = value

    return base