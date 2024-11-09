from enum import Enum


class Rarity(Enum):
    Common = 1
    Uncommon = 2
    Rare = 3
    Epic = 4
    Legendary = 5
    Mystical = 6
    Godlike = 7


class BaseItem:
    def __init__(self):
        self.name: str = 'baseitem'
        self.rarity: Rarity = Rarity.Godlike
