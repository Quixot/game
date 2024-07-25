"""
Типы данных
"""

from dataclasses import dataclass
from enum import Enum, auto


# Направление движения
class Direction(Enum):
    LEFT = -1
    RIGHT = 1


# TODO Нужен ли класс Movement, чтобы задавать движение сразу на несколько шагов?
# @dataclass
# class Movement:
#     """
#     Пример использования:
#     movement = Movement(direction=Direction.LEFT, distance=10)
#     """
#     direction: Direction
#     distance: int