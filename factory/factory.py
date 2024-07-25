"""
1. Интерфейс фабрики объектов игры
2. Конкретная фабрика объектов игры
"""

from abc import ABC, abstractmethod


class ObjectFactory(ABC):
    """
    Интерфейс фабрики основных объектов

    Должны быть имплементированы следующие объекты:

    Герой
    Враг
    Бонус
    Препятствие

    """

    @abstractmethod
    def make_hero(self):
        """
        Игрок
        """

    @abstractmethod
    def make_enemy(self):
        """
        Враг
        """

    @abstractmethod
    def make_bonus(self):
        """
        Бонус
        """

    @abstractmethod
    def make_let(self):
        """
        Препятствие
        """


class ConcreteObjectFactory(ObjectFactory):
    def make_hero(self):
        """
        Игрок
        """



    def make_enemy(self):
        """
        Враг
        """
    def make_bonus(self):
        """
        Бонус
        """
    def make_let(self):
        """
        Препятствие
        """    
