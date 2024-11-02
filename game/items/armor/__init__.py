from enum import Enum

from game.base.item import BaseItem
from game.items.armor.menu import ArmorContextMenu


class ArmorType(Enum):
    head = 1
    hands = 3
    chest = 2
    legs = 4
    feet = 5


class Armor(BaseItem):
    def __init__(self):
        super().__init__()
        self.name = 'armor'
        self.context_menu = ArmorContextMenu(self)

        self.type: ArmorType = ArmorType.head
        self.durability: int = 0
        self.max_durability: int = 100
        self.protect_factor: int = 10

    def equip(self): ...

    def on_hit(self): ...

    def __str__(self):
        return f'[{self.durability} / {self.max_durability}] {self.get_name()}'
