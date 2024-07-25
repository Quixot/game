"""
1. Интерфейс объекта
2. Конкретные объекты
"""

from abc import ABC, abstractmethod
from gametypes import Movement


class GameObject(ABC):
    """
    Интерфейс объекта, наследуется всеми объектами
    Должны быть имплементированы такие методы:
    Инициализация: 
        Тип: что за объект
        Жизни: к-во жизней (в случае препятствий, которые разрушаются и не должны быть воссозданы, может быть 1)
        Здоровье: в процентах (в том числе у неодушевленных предметов)
        Свойства:
    Действие: Бег
    Действие: Прыжок
    Действие: Приседание
    События: Соприкосновение        
    """

    @abstractmethod
    def __init__(self):
        """
        Инициализация объекта
        """


    @abstractmethod
    def __repr__(self):
        """
        Описание объекта
        """


    @abstractmethod
    def run(self, direction: Movement):
        """
        Движение вправо - влево
        """
        # TODO Нужно ли задавать тип Movement или достаточно int?


    @abstractmethod
    def jump(self):
        """
        Прыжок
        """


    @abstractmethod
    def squat(self):
        """
        Приседание
        """


    @abstractmethod
    def touch(self, type):
        """
        Соприкосновение
        """



"""
Конкретные Объекты игры:
Герой
Враг
Бонус
Препятствие (может быть стеной, бордюром или ямой)
"""

class Hero(GameObject):
    """
    Герой. Персонаж управляемый пользователем
    """

    # TODO сделать декоратор для синглтонов с реестром
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance in None:
            cls._instance = super().__new__(cls)
        
        return cls._instance

    def __init__(self):
        pass



    def __repr__(self):
        """
        Описание объекта
        """
        return f"{self}"


    def run(self, direction: Movement):
        """
        Движение вправо - влево
        """
        return direction


    def jump(self):
        """
        Прыжок
        """

    
    def squat(self):
        """
        Приседание
        """

    
    def touch(self, type):
        """
        Соприкосновение
        """
    