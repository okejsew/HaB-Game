from enum import Enum

from game.item import BaseItem


class ArmorType(Enum):
    head = 1
    hands = 3
    chest = 2
    legs = 4
    feet = 5


class Armor(BaseItem):
    def __init__(self):
        super().__init__()
        self.name = 'Броня'

        self.type: ArmorType = ArmorType.head
        self.durability: int = 0
        self.max_durability: int = 100
        self.protect_factor: int = 0

    def __str__(self):
        return f'[{self.durability} / {self.max_durability}] {self.name}'
