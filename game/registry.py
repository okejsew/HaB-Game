from typing import Type

from game.base.item import Weapon, Armor, Interactable


class ItemRegistry:
    @staticmethod
    def register_weapon(item: Type[Weapon]):
        pass

    @staticmethod
    def register_armor(item: Type[Armor]):
        pass

    @staticmethod
    def register_usable(item: Type[Interactable]):
        pass