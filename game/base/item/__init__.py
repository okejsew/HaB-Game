from enum import Enum

from localization import Locale


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

    def get_name(self) -> str:
        return Locale.get(self.name)

    def get_description(self) -> str:
        return Locale.get(self.name + '_desc')
