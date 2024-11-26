from dataclasses import dataclass
from typing import Optional, Callable

from game.base.item import Item, Armor, Weapon, Usable
from game.core.bodypart import BodyPart
from game.core.settings import Settings


@dataclass
class Equipment:
    head: Optional[Armor] = None
    hands: Optional[Armor] = None
    chest: Optional[Armor] = None
    legs: Optional[Armor] = None
    feet: Optional[Armor] = None

    right_hand: Optional[Weapon] = None
    left_hand: Optional[Usable] = None

    def __getitem__(self, bodypart: BodyPart):
        return getattr(self, bodypart.name)

    def equip(self, item: Item, add_method: Callable[[Item], None]):
        bodypart = 'left_hand'
        if isinstance(item, Armor):
            bodypart = item.bodypart.name
        elif isinstance(item, Weapon):
            bodypart = 'right_hand'

        if prev := getattr(self, bodypart):
            add_method(prev)
        setattr(self, bodypart, item)

    def __repr__(self):
        string = ''
        for value in self.__dict__.values():
            if not value: continue
            if isinstance(value, Armor):
                string += f'    {value.bodypart.value}: '.ljust(Settings.ljust_item)
            elif isinstance(value, Weapon):
                string += f'    Правая рука: '.ljust(Settings.ljust_item)
            elif isinstance(value, Usable):
                string += f'    Левая рука: '.ljust(Settings.ljust_item)
            string += f'{value}\n'
        return string
